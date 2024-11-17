# docker container image
FROM python:3.11.0


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for HTTP/1.1
# EXPOSE 8000

CMD ["hypercorn", "--bind", "0.0.0.0:$PORT", "run:app"]

