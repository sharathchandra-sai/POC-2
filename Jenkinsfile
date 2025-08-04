pipeline {
    agent any
 
    stages {
        stage('Clone Repo') {
            steps {
                git branch:'main' , url: 'https://github.com/sharathchandra-sai/POC-2.git'
            }
        }
 
        // stage('Build') {
        //     steps {
        //         echo 'Simulating Build... (Use Maven or Gradle here)'
        //         sh 'cp app.war app.war' // placeholder
        //     }
        // }
 
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
