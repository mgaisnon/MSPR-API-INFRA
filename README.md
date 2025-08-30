# PTK - Infrastructure Globale

![Docker Compose](https://img.shields.io/badge/infra-docker--compose-blue)
![RabbitMQ](https://img.shields.io/badge/message--broker-rabbitmq-orange)
![Monitoring](https://img.shields.io/badge/monitoring-prometheus%20%2B%20grafana-yellowgreen)

Ce dépôt orchestre l'ensemble des microservices de l'application PayeTonKawa : clients, produits et commandes.

## 🔗 Microservices
- `mspr-api-clients` → [http://localhost/clients](http://localhost/clients)
- `mspr-api-produits` → [http://localhost/produits](http://localhost/produits)
- `mspr-api-commandes` → [http://localhost/commandes](http://localhost/commandes)

## 🐳 Services inclus via Docker Compose
- 3 APIs FastAPI (clients, produits, commandes)
- RabbitMQ (message broker)
- MySQL (1 instance par service)
- Prometheus (monitoring)
- Grafana (visualisation)
- Traefik (reverse proxy)

## 🔧 Lancer l’infra
```bash
docker compose up -d
````

## 📆 Structure des ports exposés

| Service       | Port local                                       |
| ------------- | ------------------------------------------------ |
| Traefik UI    | [http://localhost:8080](http://localhost:8080)   |
| RabbitMQ UI   | [http://localhost:15672](http://localhost:15672) |
| Prometheus    | [http://localhost:9090](http://localhost:9090)   |
| Grafana       | [http://localhost:3000](http://localhost:3000)   |
| Clients API   | [http://localhost:8001](http://localhost:8001)   |
| Produits API  | [http://localhost:8002](http://localhost:8002)   |
| Commandes API | [http://localhost:8003](http://localhost:8003)   |

## ⚙️ Configuration Traefik

Fichier : `traefik.yml`

* Routage basé sur les paths (`/clients`, `/produits`, `/commandes`)
* Compatible HTTPS si configuré ultérieurement

## 🧲 Tests

Les tests sont définis dans chaque microservice et exécutables via GitHub Actions.

## 🔁 CI/CD

Déclenché sur chaque push via GitHub Actions.

* Build des images Docker dans chaque repo API
* Utilisation des images taggées dans ce dépôt global