FROM python:3.11-alpine

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Java and clean up
RUN apk add --no-cache openjdk17-jdk && \
    rm -rf /var/cache/apk/*

# Set Java environment
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk
ENV PATH=$PATH:$JAVA_HOME/bin

# Create logs directory
RUN mkdir -p logs

# Copy application code
COPY . .

EXPOSE 5002

CMD ["python", "app.py"]