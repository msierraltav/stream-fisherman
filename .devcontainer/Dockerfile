# Usa una imagen base de Python
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Crea un directorio de trabajo
WORKDIR /workspace

# Copia los archivos de tu proyecto al contenedor
COPY . /workspace

# Instala las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG USERNAME=vscode

# RUN mkdir /videos \
#     && chown -R $USERNAME /videos

# Configura el contenedor para usar bash como shell predeterminado
SHELL ["/bin/bash", "-c"]
