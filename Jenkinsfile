pipeline {
    agent {
        docker { 
            image 'rockylinux:8'
            args '-u root'
            reuseNode true 
        }
    }
    options {
        skipDefaultCheckout()
    }
    stages {
        stage('Check if need build') {
            steps {
                sh 'rm -rf * .* || true'
                dir('proxmox-backup') {
                    git changelog: false, poll: false, url: 'git://git.proxmox.com/git/proxmox-backup.git'
                    script {
                        env.VERSION = sh (
                            script: 'grep "^version =" Cargo.toml | sed -r "s/(version = |\\")//g"',
                            returnStdout: true
                        ).trim()
                    }
                }
                echo "Found version ${VERSION}"
                withCredentials([usernamePassword(credentialsId: '37caf116-0ecf-4870-b2a0-29ab0ebb0573', passwordVariable: 'GITHUB_TOKEN', usernameVariable: 'GITHUB_USER')]) {
                    script {
                        def response = httpRequest(
                            url: "https://api.github.com/repos/Dwight-Studio/proxmox-backup-client-builds/releases/tags/${VERSION}",
                            httpMode: "GET",
                            customHeaders: [[maskValue: false, name: 'Accept', value: 'application/vnd.github+json'], [maskValue: true, name: 'Authorization', value: "Bearer $GITHUB_TOKEN"], [maskValue: false, name: 'X-GitHub-Api-Version', value: '2022-11-28']],
                            validResponseCodes: "200,404"
                        )
                        if (response.status == 404) {
                            echo "Version ${VERSION} not found in releases, building..."
                        } else {
                            currentBuild.result = 'ABORTED'
                            error "Aborting early: Version ${VERSION} found, aborting build."
                        }
                    }
                }
            }
        }

        stage('Publish release on Github') {
            steps {
                withCredentials([usernamePassword(credentialsId: '37caf116-0ecf-4870-b2a0-29ab0ebb0573', passwordVariable: 'GITHUB_TOKEN', usernameVariable: 'GITHUB_USER')]) {
                    httpRequest(
                        contentType: 'APPLICATION_JSON',
                        customHeaders: [[maskValue: false, name: 'Accept', value: 'application/vnd.github+json'], [maskValue: true, name: 'Authorization', value: "Bearer $GITHUB_TOKEN"], [maskValue: false, name: 'X-GitHub-Api-Version', value: '2022-11-28']], 
                        httpMode: 'POST',
                        requestBody: '{"tag_name":"${VERSION}","name":"${VERSION}"}',
                        url: 'https://api.github.com/repos/Dwight-Studio/proxmox-backup-client-builds/releases',
                        validResponseCodes: '200'
                    )
                }
            }
        }

        stage('Run build on Copr') {
            steps {
                withCredentials([string(credentialsId: 'bc758890-fdce-4b66-981c-875025c9a254', variable: 'WEBHOOK_URL')]) {
                    httpRequest(
                        contentType: 'TEXT_PLAIN', 
                        httpMode: 'POST', 
                        requestBody: "${VERSION}", 
                        url: "${WEBHOOK_URL}",
                    )
                }
            }
        }
    }
}