# Traefik

## 🐧 macOS / Linux

Ouvre ton terminal et colle ces commandes :

```bash
# Sauvegarde du fichier hosts original
sudo cp /etc/hosts /etc/hosts.backup

# Ajout des entrées pour Traefik et tes services
echo "127.0.0.1 traefik.localhost grafana.localhost prometheus.localhost rabbitmq.localhost clients.localhost produits.localhost commandes.localhost" | sudo tee -a /etc/hosts

# Vérifie que l'entrée est bien ajoutée
tail -n 5 /etc/hosts
```

---

## 🪟 Windows

1. Ouvre **Bloc-Notes en administrateur**

   * Clique sur "Démarrer" → tape `Bloc-Notes` → clic droit → *Exécuter en tant qu’administrateur*.

2. Ouvre le fichier :

   ```
   C:\Windows\System32\drivers\etc\hosts
   ```

3. À la fin du fichier, colle cette ligne :

```
127.0.0.1 traefik.localhost grafana.localhost prometheus.localhost rabbitmq.localhost clients.localhost produits.localhost commandes.localhost
```

4. Sauvegarde le fichier (⚠️ vérifie qu’il s’appelle bien `hosts`, pas `hosts.txt`).

---

## ✅ Test

Ensuite relance tes containers :

```bash
docker compose down
docker compose --env-file .env.ci.sample up -d
```

Puis ouvre dans ton navigateur :

* [http://traefik.localhost](http://traefik.localhost)
* [http://grafana.localhost](http://grafana.localhost)
* [http://prometheus.localhost](http://prometheus.localhost)
* [http://rabbitmq.localhost](http://rabbitmq.localhost)
* [http://clients.localhost](http://clients.localhost)
* [http://produits.localhost](http://produits.localhost)
* [http://commandes.localhost](http://commandes.localhost)
