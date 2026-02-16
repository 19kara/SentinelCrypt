# src/core/engine.py

from scanner.file_system import scan_files
from analyzer.entropy import calculate_entropy
from crypto.aes_engine import encrypt_data

class Engine:
    def __init__(self):
        print("[+] Initialisation du moteur SentinelCrypt")

    def run(self):
        print("[+] Lancement du scan...")
        files = scan_files("data/logs")  # Exemple : scanner le dossier logs

        if not files:
            print("Aucun fichier trouvé.")
            return

        for f in files:
            print(f"Analyse de {f}")
            entropy = calculate_entropy(f)
            print(f" -> Entropie : {entropy:.2f}")

            # Exemple de chiffrement
            encrypted = encrypt_data(b"Hello SentinelCrypt")
            print(f" -> Données chiffrées (extrait) : {encrypted[:20]}...")
