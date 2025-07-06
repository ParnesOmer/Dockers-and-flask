FROM python:3.11-alpine

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create logs directory
RUN mkdir -p logs

# Copy application code
COPY . .

EXPOSE 5001

CMD ["python", "app.py"]