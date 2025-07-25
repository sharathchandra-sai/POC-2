pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning the repo...'
            }
        }

        stage('Run Hello Script') {
            steps {
                sh 'bash hello.sh'
            }
        }
    }
}
