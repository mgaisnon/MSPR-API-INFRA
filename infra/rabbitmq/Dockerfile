# Utilisation de l'image officielle RabbitMQ avec le plugin management
FROM rabbitmq:3.13-management

# Définition des variables d'environnement (utilisateur + mot de passe par défaut)
ENV RABBITMQ_DEFAULT_USER=mspr \
    RABBITMQ_DEFAULT_PASS=msprpass

# (Optionnel) Copie d'un fichier de configuration custom si tu veux affiner RabbitMQ
# COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

# Expose les ports nécessaires
# 5672 = AMQP
# 15672 = Dashboard web
EXPOSE 5672 15672

# Commande de démarrage par défaut
CMD ["rabbitmq-server"]
