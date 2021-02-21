def err = null
try {
  
    node {
      
        stage('Preparation') { 
            git credentialsId: 'fef4159e-285b-45d9-80ca-5981c4576ba5', url: 'https://github.com/pondssszzz/List_app-project.git'
        }
      
        stage('Dependencies') {
                sh 'export JAVA_HOME=/opt/jdk1.8.0_131'
                sh 'export JRE_HOME=/opt/jdk1.8.0_131/jre'
                sh 'export PATH=$PATH:/opt/jdk1.8.0_131/bin:/opt/jdk1.8.0_131/jre/bin'
                sh 'echo $JAVA_HOME'
        }
        
        stage('Clean Build') {
                dir("android") {
                    
                    sh "pwd"
                    sh 'ls -al'
                    sh './chmod 755 gradlew'
                    sh './gradlew clean'
                }   
        }
        
        stage('Build release ') {
            parameters {
                credentials credentialType: 'org.jenkinsci.plugins.plaincredentials.impl.FileCredentialsImpl', defaultValue: '5d34f6f7-b641-4785-frd5-c93b67e71b6b', description: '', name: 'keystore', required: true
            }
            dir("android") {
                sh './gradlew assembleRelease'
            }
        }
      
        stage('Compile') {
            archiveArtifacts artifacts: '**/*.apk', fingerprint: true, onlyIfSuccessful: true            
        }
    }
  
} catch (caughtError) { 
    
    err = caughtError
    currentBuild.result = "FAILURE"

} finally {
    
    if(currentBuild.result == "FAILURE"){
              sh "echo 'Build FAILURE'"
    }else{
         sh "echo 'Build SUCCESSFUL'"
    }
   
}
