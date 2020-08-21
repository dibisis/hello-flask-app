pipeline {
    agent { docker { image 'python:3.7.6' } }
       triggers {
        pollSCM "* * * * *"
       }
    stages {
        stage('Build Application') {
            steps {
                echo '=== Building pf-hello-flask Application ==='

                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'

                }
            }
        }
        stage('Test Application') {
            steps {
                echo '=== Testing pf-hello-flask Application ==='

            }
            post {
                always {
                    echo '=== Testing pf-hello-flask Application post action ==='
                }
            }
        }
        stage('Build docker image') {
            container('docker') {

                    sh "docker build -t dibisis/pf-hello-flask:latest -f ./Dockerfile ."

            }
        }
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                echo '=== Pushing pf-hello-flask Docker Image ==='
                script {
                    GIT_COMMIT_HASH = sh (script: "git log -n 1 --pretty=format:'%H'", returnStdout: true)
                    SHORT_COMMIT = "${GIT_COMMIT_HASH[0..7]}"
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerHubCredentials') {
                        app.push("$SHORT_COMMIT")
                        app.push("latest")
                    }
                }
            }
        }
        stage('Remove local images') {
            steps {
                echo '=== Delete the local docker images ==='
                sh("docker rmi -f dibisis/pf-hello-flask:latest || :")
                sh("docker rmi -f dibisis/pf-hello-flask:$SHORT_COMMIT || :")
            }
        }
    }
}