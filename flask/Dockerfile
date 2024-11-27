# docker container image
FROM python:3.11.0


# Set the working directory in the container
WORKDIR /app

# Copy the files
COPY . .

COPY ../requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# CMD ["hypercorn", "--bind", "0.0.0.0:8000", "run:app"]

# run with hypercorn.toml config -> HTTP/1.1 & HTTP/2
CMD hypercorn "run:app" -c hypercorn.toml --bind "0.0.0.0:8000"

