pipeline {

  agent any

  environment {
    CI = 'true'
    imagename = '/yks/yks-inner/assessing-floor'
    REGISTRY = 'registry.gitlab.com'
    registryCredential = 'gitlab-user'
  }

  options {
    buildDiscarder(logRotator(numToKeepStr: '2', artifactNumToKeepStr: '2'))
  }

  stages {

    stage('Debug') {
      steps {
        sh 'printenv'
        sh 'node -v || true'
        sh 'docker -v || true'
        sh 'docker info || true'
        sh 'docker-compose -v || true'
      }
    }

    stage('Build image & push in registry') {
      steps {
        script {
          docker.withRegistry('https://' + REGISTRY + imagename, registryCredential) {

            def customImage = docker.build("${REGISTRY}${imagename}/${GIT_BRANCH}:${BUILD_NUMBER}")

            customImage.push()
            customImage.push('latest')

          }
        }
      }
      post {
        cleanup {
          sh 'docker rmi ${REGISTRY}${imagename}/${GIT_BRANCH}:${BUILD_NUMBER} || true' // untaget
          sh 'docker rmi ${REGISTRY}${imagename}/${GIT_BRANCH}:latest || true' // rmi
          sh 'docker rmi $(docker images -f "dangling=true" -q) || true' // remove all dangling=true
        }
        success {
          sendTelegram(" ${REGISTRY}${imagename}/${GIT_BRANCH}:${BUILD_NUMBER} :: ${currentBuild.currentResult}")
        }
        unstable {
          sendTelegram(" ${REGISTRY}${imagename}/${GIT_BRANCH}:${BUILD_NUMBER} :: ${currentBuild.currentResult}")
        }
        failure {
          sendTelegram(currentBuild.currentResult)
        }
      }
    }

  }
}


// Отправляет сообщение в телеграм чат (бот)
Object sendTelegram (String message) {
  str = """
    curl --silent --location --request POST 'https://tg-bot.ykdev.ru/send' \
    --header 'access-token: CluN8RoMrvFNSqxX7pl7nifRQty42zus' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "message": "${BUILD_DISPLAY_NAME} :: ${GIT_URL} :: ${JOB_BASE_NAME} :: ${STAGE_NAME} :: ${message}"
    }'
  """
  return sh(
    script: str,
    returnStdout: true
  )
}
