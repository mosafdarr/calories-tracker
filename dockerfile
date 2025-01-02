# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the working directory in the container
COPY . .

# Expose the port on which Django will run (8000 is default)
EXPOSE 8000

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Run Django server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
