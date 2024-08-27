FROM python:3.11.7-alpine AS builder

WORKDIR /app

# Installation des dépendances de build et nettoyage en une seule étape
RUN apk add --no-cache gcc musl-dev linux-headers

# Copie des fichiers de dépendances
COPY requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir --user --prefer-binary -r requirements.txt && \
    find /root/.local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' +

# Étape finale
FROM python:3.11.7-alpine

WORKDIR /app

# Copie des dépendances depuis l'étape de build
COPY --from=builder /root/.local /root/.local

# Copie du code de l'application
COPY . .

# # Création d'un utilisateur non-root
# RUN adduser -D appuser && \
#     chown -R appuser:appuser /app

# Configuration du PATH pour inclure les binaires installés par pip
ENV PATH=/root/.local/bin:$PATH

# # Passage à l'utilisateur non-root
# USER appuser

# Exposition du port
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]