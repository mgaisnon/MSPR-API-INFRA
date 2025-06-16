import subprocess
import os
import sys

VOLUMES = [
    "mspr-api-infra_rabbitmq_data",
    "mspr-api-infra_prometheus_data",
    "mspr-api-infra_grafana_data",
]

TAR_FILES = [
    "rabbitmq_data.tar",
    "prometheus_data.tar",
    "grafana_data.tar",
]

def run_command(command):
    """Exécute une commande shell et gère les erreurs."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e.stderr}")
        sys.exit(1)

def backup_volumes():
    """Crée des fichiers .tar pour chaque volume."""
    print("Démarrage de la sauvegarde des volumes...")
    for volume, tar_file in zip(VOLUMES, TAR_FILES):
        print(f"Sauvegarde du volume {volume} dans {tar_file}...")
        command = (
            f"docker run --rm -v {volume}:/data -v $(pwd):/backup busybox "
            f"tar cvf /backup/{tar_file} /data"
        )
        run_command(command)
    print("Sauvegarde terminée !")

def restore_volumes():
    """Restaure les volumes à partir des fichiers .tar."""
    print("Démarrage de la restauration des volumes...")
    for volume, tar_file in zip(VOLUMES, TAR_FILES):
        if not os.path.exists(tar_file):
            print(f"Erreur : Le fichier {tar_file} n'existe pas dans le répertoire courant.")
            sys.exit(1)
        print(f"Restauration du volume {volume} depuis {tar_file}...")
        # Crée le volume s'il n'existe pas
        run_command(f"docker volume create {volume}")
        # Restaure les données
        command = (
            f"docker run --rm -v {volume}:/data -v $(pwd):/backup busybox "
            f"tar xvf /backup/{tar_file} -C /data --strip-components=1"
        )
        run_command(command)
    print("Restauration terminée !")

def main():
    """Point d'entrée du script."""
    if not os.path.exists("docker-compose.yml"):
        print("Erreur : Ce script doit être exécuté depuis le répertoire contenant docker-compose.yml.")
        sys.exit(1)

    print("Script de sauvegarde et restauration des volumes Docker")
    print("1. Sauvegarder les volumes")
    print("2. Restaurer les volumes")
    choice = input("Choisissez une option (1 ou 2) : ")

    if choice == "1":
        backup_volumes()
    elif choice == "2":
        restore_volumes()
    else:
        print("Choix invalide. Veuillez sélectionner 1 ou 2.")
        sys.exit(1)

if __name__ == "__main__":
    main()