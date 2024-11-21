@echo off
REM Build the Docker image
docker build -t recipefinder:latest .

REM Check if the container already exists
IF [ERRORLEVEL] NEQ 0 (
    echo Container already exists. Removing...
    docker rm -f RecipeFinder
)

echo !!Docker image built and container will run on http://127.0.0.1:8000 with name RecipeFinder, Ctrl/Control  + c to terminate job.

REM Run the Docker container with the specified name and port
docker run --name RecipeFinder -p 8000:8000 recipefinder:latest

