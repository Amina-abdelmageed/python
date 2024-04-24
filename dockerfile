
# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
COPY random_paragraphs.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]


