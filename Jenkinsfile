pipeline {
  agent { docker { image 'registry.hub.docker.com/library/python:3.10.7-alpine' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest --junitxml=junit.xml'
      }  
    }
    stage("Collect Test Resuts") {
      steps {
        archiveArtifacts "junit.xml"
        junit "junit.xml"
      }
    }

  }
}
