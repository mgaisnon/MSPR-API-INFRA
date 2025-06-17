#!/bin/bash

HOSTS_FILE="/etc/hosts"
NEEDED_HOSTS=("traefik.localhost" "grafana.localhost" "prometheus.localhost" "rabbitmq.localhost" "kibana.localhost")

for HOST in "${NEEDED_HOSTS[@]}"; do
  if ! grep -q "$HOST" "$HOSTS_FILE"; then
    echo "[INFO] Ajout des entrées dans /etc/hosts..."
    echo "127.0.0.1 $HOST" | sudo tee -a "$HOSTS_FILE" > /dev/null
  fi
done