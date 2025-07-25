pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-org/poc-2.git'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package'  // Produces target/app.war
            }
        }
        stage('Deploy') {
            steps {
                sh 'ansible-playbook deploy/deploy_to_tomcat.yml -i deploy/hosts.ini'
            }
        }
    }
}
