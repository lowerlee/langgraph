FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    libgl1-mesa-glx

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && python -m ipykernel install --user --name=langgraph-env --display-name='Langgraph Python 3.11'

WORKDIR /workspaces/app

ENV PYTHONPATH=/workspaces/app

EXPOSE 8888