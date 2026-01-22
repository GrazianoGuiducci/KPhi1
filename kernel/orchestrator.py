import os
import json
import datetime

# PERCORSI DEL SISTEMA
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT_DIR, ".agent", "skills")
EVOLUTION_LOG = os.path.join(ROOT_DIR, "evolution_path.md")

def log_evolution(event_type, description):
    """Registra un evento evolutivo nel log."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n- **[{timestamp}]** *{event_type}*: {description}"
    
    if not os.path.exists(EVOLUTION_LOG):
        with open(EVOLUTION_LOG, "w", encoding="utf-8") as f:
            f.write("# PERCORSO EVOLUTIVO DEL SISTEMA\n\n")
            
    with open(EVOLUTION_LOG, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"[EVOLUTION] {entry}")

def suggest_new_skill(task_description):
    """
    Analizza una descrizione del task (simulata qui) e suggerisce se creare una skill.
    In un'implementazione reale, qui useremmo un LLM per l'analisi semantica.
    """
    keywords = {
        "ui": "ui-architect",
        "database": "data-sovereign",
        "security": "security-oracle",
        "test": "qa-sentinel"
    }
    
    suggestions = []
    for key, skill_name in keywords.items():
        if key in task_description.lower():
            if not os.path.exists(os.path.join(SKILLS_DIR, skill_name)):
                suggestions.append(skill_name)
    
    return suggestions

import memory_manager

if __name__ == "__main__":
    print("--- KERNEL ORCHESTRATOR AVVIATO ---")
    
    # Carica contesto dalla memoria
    memory = memory_manager.load_memory()
    print(f"[CONTEXT] Focus Attuale: {memory.get('short_term_memory', {}).get('current_focus', 'Unknown')}")

    # Esempio di utilizzo
    current_task = "Dobbiamo rifare tutta la UI con componenti moderni"
    print(f"Analisi Task: {current_task}")
    
    needed_skills = suggest_new_skill(current_task)
    
    if needed_skills:
        print(f"Rilevata necessità di nuove Entità: {needed_skills}")
        for skill in needed_skills:
            log_evolution("GENBRYO", f"Identificata necessità dell'entità '{skill}'")
            # Aggiorna la memoria con format AETO (Tripletta)
            memory_manager.log_inference_triplet(
                input_context=current_task,
                ideal_reasoning=f"Il task '{current_task}' richiede competenze non presenti. Analisi TCREI suggerisce una nuova Skill.",
                expected_output=f"Generazione Entità: {skill}"
            )
    else:
        print("Nessuna nuova entità necessaria al momento.")
