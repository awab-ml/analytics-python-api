FROM python:3.13-slim

# Create a virtual environment
RUN python -m venv /opt/venv

# Set the virtual environment as the current location
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip
RUN pip install --upgrade pip

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Add /code to PYTHONPATH so Python can find the src folder
ENV PYTHONPATH=/code

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create the code directory inside the container
RUN mkdir -p /code

# Set working directory
WORKDIR /code

# Copy the requirements file
COPY requirements.txt /tmp/requirements.txt

# Copy the project code
COPY ./src /code/src

# Install Python dependencies
RUN pip install -r /tmp/requirements.txt

# Make the runtime script executable
COPY ./boot/docker-run.sh /opt/run.sh
RUN chmod +x /opt/run.sh

# Clean up apt cache
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run the FastAPI project via the runtime script
CMD ["/opt/run.sh"]
