pipeline {
    agent any
    environment {
    	DOCKER_IMAGE_TAG = "covid19_srv_img"
    	DOCKER_CONTAINER_NAME = "covid19_api_service"
    }
    parameters {
        text(name: 'COUNTRIES', defaultValue: 'Israel\nItaly\nFrance', description: 'List of countries to be queried')
    }
    stages {
    	stage('Build') {
    		steps {
    			sh "docker build . -t ${env.DOCKER_IMAGE_TAG}"
    		}
    	}
    	stage('Run') {
    		steps {
    			sh "docker run -d --name ${env.DOCKER_CONTAINER_NAME} -p 8081:8080 ${env.DOCKER_IMAGE_TAG}"
    		}
    	}
        stage('Query') {
            steps {
                sh '''#!/bin/bash
                	countries_string=$(echo "${COUNTRIES}" | tr '\n' ' ')
                	country_list=\\(${countries_string}\\) 
                	docker run --rm --network host curlimages/curl:latest http://localhost:8081/newCasesPeak?country=
                	echo ":: Initial API Service Status Check ::"
                	STATUS=$(docker run --rm --network host curlimages/curl:latest http://localhost:8081/status)
                	echo "=> Result:"
                	echo "$STATUS"
                	for country in \\"${country_list[@]}\\"; do 
                		country=`echo $country | sed 's/[^a-zA-Z]//g'`
                		if [[ ! -z "$country" ]]; then
	    					echo ""
	                		echo "::Quering COVID-19-Service for country $country ::"
	                		echo "=> Running Queries:"
	                		echo "1. Querying Endpoint: /newCasesPeak"
	                		NEWCASESPEAK=$(docker run --rm --network host curlimages/curl:latest http://localhost:8081/newCasesPeak?country=$country)
	                		echo "2. Querying Endpoint: /recoveredPeak"
		                	RECOVEREDPEAK=$(docker run --rm --network host curlimages/curl:latest "http://localhost:8081/recoveredPeak?country=$country")
		                	echo "3. Querying Endpoint: /deathsPeak"
		                	DEATHSPEAK=$(docker run --rm --network host curlimages/curl:latest "http://localhost:8081/deathsPeak?country=$country")
			            	echo ""
		                	echo ""
		                	echo "=> Results:"
		                	echo "1. /newCasesPeak:"
		                	echo "$NEWCASESPEAK"
		                	echo "2. /recoveredPeak:"
		                	echo "$RECOVEREDPEAK"
		                	echo "3. /deathsPeak:"
		                	echo "$DEATHSPEAK"
		                	echo ""
	                	fi
                	done
                '''
            }
        }
    }
    post {
    	always {
    		// Stop and Remove all related containers
    		sh "docker rm -f ${env.DOCKER_CONTAINER_NAME}"
		}
     }
}