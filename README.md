# RecipeFinder  
RecipeFinder Project - OTU  
Access demo at: https://recipefinder-1rqb.onrender.com  
<br />

# Deploy on local machine  

## Run app without docker  
- pip install flask/requirements.txt to install all required libraries
- Run without hypercorn - Execute the flask/run.py 

- Run with hypercorn - Go to flask directory on terminal, execute command hypercorn "run:app" -c hypercorn.toml --bind "0.0.0.0:8000"  

## Run app with Docker  

### Build the docker image and run the docker container  
- Execute the docker_build.bat file or run the commands in the docker_build.bat file  
<br />
    
# Deploy on third-party platform  
- Deploy using Docker, select the Dockerfile file
