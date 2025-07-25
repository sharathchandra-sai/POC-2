pipeline {
    agent any

    stages {
        stage('Checkout Repo') {
            steps {
                echo 'Cloning the repo...'
                git url: 'https://github.com/your-username/poc-2.git', branch: 'main'
            }
        }

        stage('Run Hello Script') {
            steps {
                echo 'Running hello.sh script...'
                sh 'bash hello.sh'
            }
        }

        stage('Check Web Page Message') {
            steps {
                echo 'Running Python script to check web page...'
                sh 'python3 check_web.py'
            }
        }
    }
}
