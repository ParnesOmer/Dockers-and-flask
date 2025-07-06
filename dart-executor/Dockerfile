FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Dart SDK
RUN curl -fsSL https://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-linux-x64-release.zip -o dart-sdk.zip \
    && unzip dart-sdk.zip -d /usr/lib \
    && rm dart-sdk.zip \
    && ln -s /usr/lib/dart-sdk/bin/dart /usr/local/bin/dart \
    && ln -s /usr/lib/dart-sdk/bin/dartaotruntime /usr/local/bin/dartaotruntime

# Set Dart SDK path
ENV DART_SDK=/usr/lib/dart-sdk
ENV PATH=$PATH:/usr/lib/dart-sdk/bin

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create logs directory
RUN mkdir -p logs

# Copy application code
COPY . .

EXPOSE 5003

CMD ["python", "app.py"] 