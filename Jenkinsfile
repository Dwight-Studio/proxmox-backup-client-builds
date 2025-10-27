pipeline {
    agent {
        docker { image 'rockylinux:8-minimal' }
    }
    stages {
        stage('Check if need build') {
            steps {
                git 'git://git.proxmox.com/git/proxmox-backup.git'
                script {
                    VERSION = sh (
                        script: 'grep "^version =" Cargo.toml | sed -r "s/(version = |\\")//g"',
                        returnStdout: true
                    ).trim()
                }
                echo "Found version ${VERSION}"
                withCredentials([usernamePassword(credentialsId: '37caf116-0ecf-4870-b2a0-29ab0ebb0573', passwordVariable: 'GITHUB_TOKEN', usernameVariable: 'GITHUB_USER')]) {
                    script {
                        RELEASE = sh (
                            script: '''
                            curl -L \
                            -H "Accept: application/vnd.github+json" \
                            -H "Authorization: Bearer ${GITHUB_TOKEN}" \
                            -H "X-GitHub-Api-Version: 2022-11-28" \
                            https://api.github.com/repos/Dwight-Studio/proxmox-backup-client-builds/releases/tags/${VERSION}
                            ''',
                            returnStdout: true
                        ).trim()
                    }
                    echo "RES: ${RELEASE}"
                }
            }
        }
        stage('Build on Rocky Linux 8') {
            when {
                changelog '^bump version to [0-9-.]+$'
            }
            stages {
                stage('Setup') {
                    steps {
                        sh '''
                            dnf update -y &&
                            dnf install -y git gcc openssl-devel systemd-devel libacl-devel fuse3-devel libuuid-devel &&
                            curl --proto "=https" --tlsv1.2 -sSf https://sh.rustup.rs | sh &&
                            rustup override set 1.88.0
                        '''
                    }
                }
                stage('Build') {
                    steps {
                        dir('pathpatterns') {
                            git 'git://git.proxmox.com/git/pathpatterns.git'
                        }
                        dir('proxmox') {
                            git 'git://git.proxmox.com/git/proxmox.git'
                        }
                        dir('pxar') {
                            git 'git://git.proxmox.com/git/pxar.git'
                        }
                        dir('proxmox-fuse') {
                            git 'git://git.proxmox.com/git/proxmox-fuse.git'
                            sh 'sed -ri "/MAKE_ACCESSORS(noflush)/d" ./src/glue.c'
                        }
                        dir('proxmox-backup') {
                            git 'git://git.proxmox.com/git/proxmox-backup.git'
                            sh '''
                                rm -rf .cargo &&
                                sed -ri "s/^#(proxmox|pbs|pathpatterns|pxar)/\1/" Cargo.toml &&
                                cargo build --release --package proxmox-backup-client --bin proxmox-backup-client --package pxar-bin --bin pxar
                            '''
                        }
                    }
                }
            }
        }
    }
}