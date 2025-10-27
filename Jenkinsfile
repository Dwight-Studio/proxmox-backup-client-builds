pipeline {
    agent none
    options {
        skipDefaultCheckout()
    }
    stages {
        stage('Check if need build') {
            agent {
                docker { 
                    image 'rockylinux:8-minimal'
                    reuseNode true 
                }
            }
            steps {
                git 'git://git.proxmox.com/git/proxmox-backup.git'
                script {
                    env.VERSION = sh (
                        script: 'grep "^version =" Cargo.toml | sed -r "s/(version = |\\")//g"',
                        returnStdout: true
                    ).trim()
                }
                echo "Found version ${VERSION}"
                withCredentials([usernamePassword(credentialsId: '37caf116-0ecf-4870-b2a0-29ab0ebb0573', passwordVariable: 'GITHUB_TOKEN', usernameVariable: 'GITHUB_USER')]) {
                    script {
                        def response = httpRequest(
                            url: "https://api.github.com/repos/Dwight-Studio/proxmox-backup-client-builds/releases/tags/${VERSION}",
                            httpMode: "GET",
                            customHeaders: [[maskValue: false, name: 'Accept', value: 'application/vnd.github+json'], [maskValue: true, name: 'Authorization', value: "Bearer ${GITHUB_TOKEN}"], [maskValue: false, name: 'X-GitHub-Api-Version', value: '2022-11-28']],
                            validResponseCodes: "200,404"
                        )
                        if (response.status == 404) {
                            echo "Version ${VERSION} not found in releases, building..."
                            env.RUN_BUILD = 'true'
                        } else {
                            echo "Version ${VERSION} found, aborting build."
                            env.RUN_BUILD = 'false'
                        }
                    }
                }
            }
        }
        stage('Build on Rocky Linux 8') {
            agent {
                docker { 
                    image 'rockylinux:8-minimal'
                    reuseNode true 
                }
            }
            when {
                environment name: 'RUN_BUILD', value: 'true'
            }
            stages {
                stage('Setup') {
                    agent {
                        docker { 
                            image 'rockylinux:8-minimal'
                            reuseNode true 
                        }
                    }
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
                    agent {
                        docker { 
                            image 'rockylinux:8-minimal'
                            reuseNode true 
                        }
                    }
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