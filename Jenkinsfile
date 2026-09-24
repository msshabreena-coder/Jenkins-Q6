pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/msshabreena-coder/Jenkins-Q6.git'
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        bat 'python frontend_check.py'
                    }
                }

                stage('Backend Check') {
                    steps {
                        bat 'python backend_check.py'
                    }
                }
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'frontend_report.txt,backend_report.txt',
                             allowEmptyArchive: false
            }
        }
    }
}
