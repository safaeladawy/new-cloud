# Base imgae
FROM python

# Working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy The application code
COPY . .

# Expose port
EXPOSE 5000

# Set Entry point Command
CMD [ "python", "accounts_service.py" ]