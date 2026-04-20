pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat """
                python -m venv %VENV%
                %VENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install pytest pytest-html
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                %VENV%\\Scripts\\activate
                pytest --junitxml=report.xml --html=report.html --self-contained-html
                """
            }
        }
    }

    post {
        always {
            junit 'report.xml'
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}