pipeline {
    agent { docker { image 'python:3.7.1' } }
       triggers {
        pollSCM "* * * * *"
       }
    stages {
        stage('Build Application') {
            steps {
                echo '=== Building pf-hello-flask Application ==='
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test Application') {
            steps {
                echo '=== Testing pf-hello-flask Application ==='
                sh 'python tests/test_hello.py'
            }
            post {
                always {
                    echo '=== Testing pf-hello-flask Application post action ==='
                }
            }
        }
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                echo '=== Building pf-hello-flask Docker Image ==='
                script {
                    app = docker.build("dibisis/pf-hello-flask")
                }
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