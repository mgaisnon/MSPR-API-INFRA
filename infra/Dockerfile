FROM nginx:alpine

# Supprime la conf par défaut
RUN rm /etc/nginx/conf.d/default.conf

# Copie ta conf statique
COPY nginx.conf /etc/nginx/conf.d/

# Copie ta landing page
COPY index.html /etc/nginx/html/index.html
