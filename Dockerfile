# Use an official Python runtime as a parent image
FROM python:3.10.13-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run connect_db.py when the container launches
CMD ["python", "connect_db.py"]
