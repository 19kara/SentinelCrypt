# src/scanner/file_system.py

import os

def scan_files(path):
    """Retourne la liste des fichiers dans un dossier donné"""
    files = []
    for root, _, filenames in os.walk(path):
        for name in filenames:
            files.append(os.path.join(root, name))
    return files
