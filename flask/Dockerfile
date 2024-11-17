# docker container image
FROM python:3.11.0


# Set the working directory in the container
WORKDIR /app

# # Install OpenSSL
# RUN apt-get update && apt-get install -y openssl

# # Generate self-signed certificate
# RUN openssl req -x509 -newkey rsa:4096 -nodes \
#     -out cert.pem -keyout key.pem -days 365 \
#     -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"


# Copy the requirements file
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for HTTP/1.1 and HTTP/2
# EXPOSE 8000

CMD hypercorn --bind "0.0.0.0:$PORT" --h2 --insecure-bind run:app