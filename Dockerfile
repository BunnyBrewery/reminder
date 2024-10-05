FROM python:3.11-slim

# To prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# To prevent buffered output (so make it real-time output)
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for compiling some Python packages
# RUN apt-get update && apt-get install -y \
#     gcc \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

WORKDIR /fast_api_app

# COPY pyproject.toml poetry.lock /app/
COPY . /fast_api_app

RUN pip install poetry

# Configure Poetry to install packages directly into the Docker environment, without creating a virtualenv
RUN poetry config virtualenvs.create false

# Install the dependencies listed in the poetry.lock file without development dependencies
RUN poetry install --no-dev --no-interaction --no-ansi



# Expose port 8000 to allow traffic to reach your FastAPI app
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn with proper host and port
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
