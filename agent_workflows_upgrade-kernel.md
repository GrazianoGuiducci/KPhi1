---
description: Aggiorna il kernel Antigravity quando viene rilasciata una nuova versione.
---

# Workflow: Aggiornamento Kernel Antigravity

Questo workflow guida l'aggiornamento del kernel quando una nuova versione è disponibile.

## Prerequisiti
- Avere accesso alla nuova versione del kernel (es. da una cartella o repository).
- Backup della versione corrente (opzionale ma consigliato).

## Procedura

### 1. Backup (Opzionale)
```powershell
Copy-Item -Path ".\.agent" -Destination ".\.agent_backup" -Recurse
Copy-Item -Path ".\DNA.md" -Destination ".\DNA.md.bak"
```

### 2. Confronta e Merge delle Skill
Per ogni nuova skill nella nuova versione:
1. Verifica se esiste già in `.agent/skills/`.
2. Se è nuova, copiala direttamente.
3. Se esiste, confronta i contenuti e decidi se sostituire o fare merge manuale.

### 3. Aggiorna il DNA
Confronta il `DNA.md` della nuova versione con quello attuale:
- Se ci sono nuovi assiomi o principi, integrali.
- Mantieni eventuali personalizzazioni locali.

### 4. Aggiorna i Moduli Kernel
Sostituisci i file in `kernel/` con quelli della nuova versione (se presenti modifiche).

### 5. Log dell'Evoluzione
Aggiungi una entry in `evolution_path.md`:
```markdown
- **[DATA]** *KERNEL-UPDATE*: Aggiornato a v[VERSIONE]. [Note sulle modifiche].
```

### 6. Verifica
Avvia una nuova chat con l'AI e verifica che:
- [ ] L'AI legga correttamente `_AI_CONTEXT.md`.
- [ ] Le nuove skill siano riconosciute.
- [ ] Il DNA sia caricato senza errori.
