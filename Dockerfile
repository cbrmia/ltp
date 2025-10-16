# Stage 1: Build TypeScript to JavaScript
FROM python:3.12

WORKDIR /app

# Install
RUN apt-get update -y && pip install poetry

# Copy package and install dependencies
COPY . .
RUN poetry sync
RUN poetry build

# Run the CLI
ENTRYPOINT ["poetry", "run", "python", "src/ltp_app/app.py"]

