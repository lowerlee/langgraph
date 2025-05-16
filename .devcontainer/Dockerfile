FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies required for olmOCR
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    libglib2.0-0 \
    libmagic-dev \
    libtesseract-dev \
    tesseract-ocr \
    libgl1-mesa-glx \
    poppler-utils \
    fonts-crosextra-caladea \
    fonts-crosextra-carlito \
    gsfonts \
    lcdf-typetools

# Install additional fonts as alternatives to MS fonts
RUN apt-get update && apt-get install -y \
    fonts-liberation \
    fonts-dejavu \
    fonts-noto

# Install Langgraph requirements
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && python -m ipykernel install --user --name=langgraph-env --display-name='Langgraph Python 3.11'

WORKDIR /workspaces/app
ENV PYTHONPATH=/workspaces/app
EXPOSE 8888