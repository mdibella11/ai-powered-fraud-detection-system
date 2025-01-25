
# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r config/requirements.txt

# Run the app (replace with your main script, e.g., train_model.py)
CMD ["python", "app/train_model.py"]
