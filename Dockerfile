# Use an official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install the dependencies from requirements.txt

RUN pip install django
RUN pip install django-embed-video

# Expose port 8000 for the Django app
EXPOSE 8000

# Set the environment variable for Django to prevent buffering of logs
ENV PYTHONUNBUFFERED 1

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
