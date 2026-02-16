# src/analyzer/entropy.py

import math

def calculate_entropy(file_path):
    """Calcule l'entropie de Shannon d'un fichier"""
    with open(file_path, "rb") as f:
        data = f.read()

    if not data:
        return 0

    freq = {}
    for byte in data:
        freq[byte] = freq.get(byte, 0) + 1

    entropy = 0
    for count in freq.values():
        p = count / len(data)
        entropy -= p * math.log2(p)

    return entropy
