pipeline {
  agent { docker { image 'python:3.9.4' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest --junitxml=results.xml'
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
