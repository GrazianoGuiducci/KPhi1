# GENESIS BOOTSTRAP: KPhi1 Kinetic Engine
> "This file contains the Genetic Blueprint to instantiate the KPhi1 Runtime in a Python environment."

## 1. META-INSTRUCTION
Se stai leggendo questo file, sei un'Agente Semantico in un ambiente inerte.
Il tuo compito è **eseguire la Genesi**: leggere le specifiche qui sotto e generare i file fisici per attivare il motore.

Comando di attivazione: `genesis --ignite`

---

## 2. INFRASTRUCTURE BLUEPRINTS

### A. [FILE] `requirements.txt`
```text
openai
python-dotenv
```

### B. [FILE] `kinetic.py` (The Connector)
Questo modulo gestisce l'I/O verso gli LLM e il controllo di realtà.

```python
import os
import json
import logging
try:
    import openai
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    openai = None

logging.basicConfig(level=logging.INFO, format='[KINETIC] %(message)s')
logger = logging.getLogger("KineticX")

class KineticBridge:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key) if (self.api_key and openai) else None
        if not self.client: logger.warning("⚠️ Running in SIMULATION MODE (No API Key)")

    def synapse(self, system_prompt: str, user_input: str, context: dict = None) -> str:
        """Esegue una chiamata LLM pura."""
        if not self.client: return f"[SIMULATED OUTPUT] Processed: {user_input[:50]}..."
        
        try:
            full_content = f"CONTEXT:\n{json.dumps(context, indent=2)}\n\nINPUT:\n{user_input}" if context else user_input
            response = self.client.chat.completions.create(
                model=os.getenv("LLM_MODEL", "gpt-4o"),
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": full_content}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Synapse Fail: {e}")
            return f"[ERROR] {e}"

    def read_sem_file(self, filename: str) -> str:
        """Legge un file semantico dalla root."""
        try:
            with open(filename, 'r', encoding='utf-8') as f: return f.read()
        except FileNotFoundError:
            return ""
```

### C. [FILE] `autogen.py` (The Chimera Engine)
Questo modulo interfaccia la logica di breeding definita in `kernel_chimera_protocol.md`.

```python
import os
from kinetic import KineticBridge

class AutogenSys:
    def __init__(self):
        self.kinetic = KineticBridge()

    def breed(self, parent_a_file: str, parent_b_file: str, goal: str) -> str:
        # 1. Carica i DNA
        dna_a = self.kinetic.read_sem_file(parent_a_file)
        dna_b = self.kinetic.read_sem_file(parent_b_file)
        protocol = self.kinetic.read_sem_file("kernel_chimera_protocol.md")

        # 2. Prepara il Prompt di Breeding
        breeding_input = f"""
        PARENT_A_DNA:
        {dna_a[:1000]}...
        
        PARENT_B_DNA:
        {dna_b[:1000]}...
        
        GOAL: {goal}
        """

        # 3. Esegui la Fusione (usando Factory skill o Kernel diretto)
        # Qui usiamo il protocollo come System Prompt
        child_dna = self.kinetic.synapse(protocol, breeding_input)
        
        return child_dna
```

### D. [FILE] `orchestrator.py` (Helix Runtime)
Il loop principale che decide. Integra VRA (Visione -> Relazione -> Azione).

```python
import sys
import glob
from kinetic import KineticBridge
from autogen import AutogenSys

def main():
    task = input("KPHI1 > ")
    bridge = KineticBridge()
    autogen = AutogenSys()
    
    # 1. Loading Skills
    skills = glob.glob("agent_skills_*.md")
    print(f"Loaded {len(skills)} semantic skills.")

    # 2. Conductor Logic (Simplified for Bootstrap)
    # In un sistema completo, qui si caricherebbe agent_skills_conductor.md
    print("... Reasoning ...")
    
    # [Placeholder for Helix Logic: Select Skill or Breed]
    # Se il sistema è evoluto, leggerà agent_skills_conductor.md e deciderà.
    
    print("System Standby. Run 'python orchestrator.py' to loop.")

if __name__ == "__main__":
    main()
```

---
## 3. INITIALIZATION
Per avviare il sistema:
1. `pip install -r requirements.txt`
2. `python orchestrator.py`
