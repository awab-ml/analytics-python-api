# Base image
FROM python:3.13-slim

# 1️⃣ Create a virtual environment
RUN python -m venv /opt/venv

# 2️⃣ Set the virtual environment as default Python
ENV PATH=/opt/venv/bin:$PATH

# 3️⃣ Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code/src  

# 4️⃣ Install OS dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5️⃣ Create working directory
RUN mkdir -p /code
WORKDIR /code

# 6️⃣ Copy Python dependencies first (for caching)
COPY requirements.txt /tmp/requirements.txt

# 7️⃣ Copy project code
COPY ./src /code/src

# 8️⃣ Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

# 9️⃣ Copy runtime script and make it executable
COPY ./boot/docker-run.sh /opt/run.sh
RUN chmod +x /opt/run.sh

# 1️⃣0️⃣ Optional cleanup to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 1️⃣1️⃣ Run the FastAPI project
CMD ["/opt/run.sh"]
