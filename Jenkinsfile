pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/your-username/poc-2.git', branch: 'main'
            }
        }

        stage('Build WAR') {
            steps {
                sh 'bash build/build.sh'
            }
        }

        stage('Deploy using Ansible') {
            steps {
                sh 'ansible-playbook ansible/deploy.yml'
            }
        }
    }
}
