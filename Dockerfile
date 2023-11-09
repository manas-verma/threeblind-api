# Using a lighter base image
FROM python:3.9-slim AS base

# Set working directory
WORKDIR /src

# Copy only requirements first to leverage Docker cache
COPY ./requirements.txt /tmp/requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the PYTHONPATH to include /src which contains our app module
ENV PYTHONPATH="${PYTHONPATH}:/src"

####
## DEVELOPMENT ##
####
FROM base AS development
COPY ./app /src/app

# Use a different CMD for development if needed, like enabling reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

####
## PRODUCTION ##
####
FROM base AS production
COPY ./app /src/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]

EXPOSE 8000
