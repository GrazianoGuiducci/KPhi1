import os
import json
import sys

# CONFIGURAZIONE
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DNA_FILE = os.path.join(ROOT_DIR, "DNA.md")
MEMORY_FILE = os.path.join(ROOT_DIR, "memory", "session_context.json")

def check_dna_integrity():
    """Verifica che il DNA esista e non sia corrotto."""
    if not os.path.exists(DNA_FILE):
        print("[SENTINEL] CRITICAL: DNA.md non trovato! Il sistema ha perso la sua identità.")
        return False
    
    with open(DNA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        if len(content) < 100: # Controllo euristico
            print("[SENTINEL] WARNING: DNA.md sembra troppo breve o corrotto.")
            return False
            
    print("[SENTINEL] DNA Integrity: OK")
    return True

def check_memory_integrity():
    """Verifica la validità del file di memoria."""
    if not os.path.exists(MEMORY_FILE):
        print("[SENTINEL] WARNING: Memoria non trovata. Creazione nuova istanza.")
        return False
        
    try:
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            json.load(f)
        print("[SENTINEL] Memory Integrity: OK")
        return True
    except json.JSONDecodeError:
        print("[SENTINEL] CRITICAL: Memoria corrotta (JSON invalido).")
        return False

def system_health_check():
    """Esegue tutti i controlli."""
    print("--- SENTINEL DIAGNOSTIC START ---")
    dna_ok = check_dna_integrity()
    mem_ok = check_memory_integrity()
    
    if dna_ok and mem_ok:
        print("[SENTINEL] STATUS: HEALTHY")
        return True
    else:
        print("[SENTINEL] STATUS: COMPROMISED")
        return False

if __name__ == "__main__":
    system_health_check()
