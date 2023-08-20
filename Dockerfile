# Python framework image
FROM python:3.8-slim


# Setting up working directory
WORKDIR /code

# Copy requirements
COPY src/requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code
COPY src/app/ /code/app

# Command to run the application
CMD ["python", "api.py"]
