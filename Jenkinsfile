pipeline {
    agent any
 
    stages {
        stage('Clone Repo') {
            steps {
git credentialsId: 'your-github-creds-id', url: 'https://github.com/your-username/my-app.git'
            }
        }
 
        stage('Build') {
            steps {
                echo 'Simulating Build... (Use Maven or Gradle here)'
                sh 'cp app.war app.war' // placeholder
            }
        }
 
        stage('Deploy with Ansible') {
            steps {
                sh '''
                cd ansible
                ansible-playbook -i inventory.ini deploy.yml
                '''
            }
        }
    }
}
