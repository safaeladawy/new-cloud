# Set BaseImage
FROM python

# Set Working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Application files
COPY . .

# Expose port
EXPOSE 6000

# Set app entry point
CMD [ "python", "inventory_service.py" ]