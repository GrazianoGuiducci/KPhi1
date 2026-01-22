import json
import os
import datetime

MEMORY_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "memory", "session_context.json")

def load_memory():
    """Carica la memoria dal file JSON."""
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_memory(data):
    """Salva la memoria nel file JSON."""
    data["last_update"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def update_focus(focus_text):
    """Aggiorna il focus corrente."""
    mem = load_memory()
    mem["short_term_memory"]["current_focus"] = focus_text
    save_memory(mem)
    print(f"[MEMORY] Focus aggiornato: {focus_text}")

def log_inference_triplet(input_context, ideal_reasoning, expected_output):
    """Registra una Tripletta Inferenziale (AETO Standard)."""
    mem = load_memory()
    
    # Assicuriamo che la lista esista
    if "inference_triplets" not in mem["long_term_memory"]:
        mem["long_term_memory"]["inference_triplets"] = []
        
    triplet = {
        "id": f"TRIPLET_{len(mem['long_term_memory']['inference_triplets']):03d}",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input_context": input_context,
        "ideal_reasoning_chain": ideal_reasoning,
        "expected_output": expected_output
    }
    
    mem["long_term_memory"]["inference_triplets"].append(triplet)
    save_memory(mem)
    print(f"[MEMORY] Tripletta Inferenziale registrata: {triplet['id']}")

def log_error_event(error_type, context, resolution_strategy):
    """Registra un errore come 'Passaggio Dimensionale' (D-ND)."""
    mem = load_memory()
    if "error_registry" not in mem["long_term_memory"]:
        mem["long_term_memory"]["error_registry"] = []
        
    error_event = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": error_type,
        "context": context,
        "resolution": resolution_strategy,
        "lesson_learned": "Ogni errore è un varco per una nuova strada."
    }
    mem["long_term_memory"]["error_registry"].append(error_event)
    save_memory(mem)
    print(f"[MEMORY] Errore registrato come opportunità: {error_type}")

def log_decision(decision_text):
    """(Deprecated) Wrapper per retrocompatibilità. Usa log_inference_triplet."""
    log_inference_triplet("Decision Log Wrapper", decision_text, "Action Recorded")

def activate_skill(skill_name):
    """Registra l'attivazione di una skill."""
    mem = load_memory()
    if skill_name not in mem.get("active_skills", []):
        mem["active_skills"] = mem.get("active_skills", []) + [skill_name]
        save_memory(mem)
        print(f"[MEMORY] Skill attivata: {skill_name}")

if __name__ == "__main__":
    # Test rapido
    update_focus("Testing Memory Manager")
    log_decision("Creata struttura iniziale della memoria")
