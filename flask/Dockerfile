# docker container image
FROM python:3.11.0

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
ADD . /app

# install the dependencise
RUN pip install -r requirements.txt

# run the command to start waitress
CMD python run.py
