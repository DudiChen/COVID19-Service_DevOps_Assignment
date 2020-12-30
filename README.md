
# Welcome to COVID-19 API Service

### Author:
David Chen <br> dudi.chen@gmail.com

| Information |
|:------------|
| This API Service is part of Fyber DevOps interview assignment.<br>The Service provides global COVID19 information regarding peaks in New Confirmed Cases, Recoveries & Deaths of the last 30 days. <br><br>The service is writen in Python with Flask, and is meant to be deployed and executed by Jenkins.<br><br>The service exposes the following Endpoints:<br><br>1. newCasesPeak - Returns the date (and value) of the highest peak of new Covid-19 cases in the last 30 days for a required country.<br>2. recoveredPeak - Returns the date (and value) of the highest peak of recovered Covid-19 cases in the last 30 days for the required country.<br>3. deathsPeak - Returns the date (and value) of the highest peak of death Covid-19 cases in the last 30 days for a required country.<br>4. status - Returns a value of success / fail to contact the backend API |


### GitHub Repository
https://github.com/DudiChen/COVID19_DevOpsAssignment.git

### COVID-19 External API used
Server-URL: https://corona.lmao.ninja/v2/ <br>Docs: https://documenter.getpostman.com/view/11144369/Szf6Z9B3?version=latest

# Usage:
## Jenkins:
Please make sure you have Jenkins server installed and ready. <br>See related info: https://www.jenkins.io/doc/book/installing/
1. In Jenkins; Create a new 'Pipeline' job with a meaningful name.
2. Under 'Advanced Project Options'; set Pipeline Definition to 'Pipeline script from SCM'.
3. In SCM field; Choose 'Git'.
4. Under 'Repository URL'; provide to above mentioned GitHub Repo URL.
6. No Credentials required as the Repo is Public.
7. Under 'Branches to build'; change '\*/master' to '\*/main'
8. Click 'Save'
9. In the project, according to the name given, click 'Build Now' to perform the initial retrieval of the Jenkinsfile from the repository. 
10. Now, refresh the project page and click the 'Build with Parameters' Option.
11. Provide the desired list of countries into the 'COUNTRIES' text parameter or use the default values. 
12. Click 'Build'.
13. Go to the Build page and watch the results under the 'Console Output' section.

# Additional Info
## Jenkinsfile
The Jenkinsfile is made out of 4 Stages:<br>1. Build : Creating the Docker image required for the app Flask server using the Dockerfile available in the GitHub repository.<br>2. Run : Executes the image container in a detached mode, forwarding host local 8081 port to the container's 8080.<br>3. Query : Performs the API queries per each country in the COUNTRIES text parameter - using a dedicated curl docker container ontop of the host network.<br> 4. Post : In addition to the above, there is a Post Stage in which the running container is stopped and host is cleaned from all traces. 
## Dockerfile
In order to deploy in an isolated environment, ensure dependencies are met and workaround the permission limitations with the jenkins user; I decided to deploy and run the application in a docker container. <br> The Dockerfile is configured to fetch requirements file and install the packages accordingly. In addition, it sets the required flask app env variable and the entrypoint command that starts the server.

### Known Issues
Due to additional obligations causing time limitation;<br>Since I couldn't find an external API that provides daily data (instead of daily accumulative), the peak data that is returned is not accurate to the exact daily but only the max by cumulative daily data.<br>For that I'de have to iterate over the data and calculate the daily stats in the following manner:<br>a. subtracting each previous day cases from current day - creating a raw daily cases dictionary - same for recovered and deaths data will give their exact daily numbers<br>b. to get each exact daily new cases I'd need to perform the following calculation per day:<br>newly-exact-daily-cases = newly-raw-daily-cases - previous-day's-raw-daily-cases - daily-deaths - daily-recovered<br>c. for each of the 3 new timeseries that were created the peak would be the max value (from it's respectful dictionary). <br><br> This is mainly technical by parsing the date string received to datetime and iterating over the dates as described.<br>My apologies for not completing this part on time. 