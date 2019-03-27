pipeline {
    agent { label 'master' }
    stages {
        stage ('Build and Deploy') {
            steps {
                echo "This is Unit test stage"
            }
        }
        stage ('Unit Test') {
            steps {
                echo "This is Unit test stage"
            }
        }
        stage ('SonarCode analysis') {
            steps {
                echo "This is code analysis stage"
            }
        }
        stage ('Build and Deploy to AAT Region') {
            steps {
                echo "This is Build and Deploy stage"
            }
        }
        
        stage ('Funtional Test') {
            steps {
                input 'Approve to perform functional test?'
                echo "This is functional test stage"
            }
        }
        
        stage ('Build and Deploy to CAT Region') {
            steps {
                echo "This is Build and Deploy stage"
            }
        }
    }
}
