HOSTS_SCRIPT=./setup-hosts.sh

.PHONY: up down restart logs hosts

up:
	@echo "🚀 Ajout des entrées dans /etc/hosts (si nécessaire)..."
	@$(HOSTS_SCRIPT)
	@echo "📦 Démarrage de la stack Docker..."
	docker compose up -d

down:
	@echo "🧨 Arrêt et suppression des conteneurs..."
	docker compose down

restart: down up

logs:
	docker compose logs -f

hosts:
	@echo "🧾 Contenu de /etc/hosts (grep localhost)..."
	@grep localhost /etc/hosts
