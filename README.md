# PayeTonKawa - Infrastructure Microservices

## Architecture

```bash
ptk-infra/
├── docker-compose.yml
├── .env
├── monitoring/
│   ├── prometheus.yml
│   └── grafana/ (facultatif : provisioning, dashboards)
├── docs/
│   ├── architecture.md
│   ├── plan-migration.md
│   └── plan-conduite-changement.md
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md
```

## 📦 Microservices

- `clients-api` : gestion des utilisateurs
- `produits-api` : gestion du catalogue
- `commandes-api` : création et suivi de commandes

## 🔌 Communication

- Utilisation de **RabbitMQ** (AMQP) pour la communication asynchrone.
- Chaque service publie et consomme des messages via des exchanges/queues dédiées.

## 📊 Monitoring

- `Prometheus` pour la collecte de métriques
- `Grafana` pour la visualisation
- Scraping automatique des endpoints `metrics` de chaque API

## 🐳 Conteneurs

- Docker Compose orchestre tous les services
- Chaque service est buildé et poussé dans un repo Docker distinct

## 🚀 Déploiement local

```bash
docker compose up --build
```
