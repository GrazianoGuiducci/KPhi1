# STREAM GUARD RULES (v1.0)
> Validazione assiomatica continua per KPhi1 (ex YAML configuration).

## 1. OBIETTIVO
Questo file serve come "Costituzione Operativa" per il modulo Kinetic-X e Halo. Definesce le soglie di tolleranza per i 7 principi KSAR.

## 2. REGOLE ASSIOMATICHE (P0-P6)

### **P0: Lignaggio** (Source Anchor)
*   **Descrizione**: L'output deve essere tracciabile al DNA.md e al Lignaggio D-ND/SG/VRA.
*   **Violazione**: `source not in allowed_lineage`
*   **Azione**: `error_fatal` (Arresto immediato)

### **P1: Integrità** (Logical Coherence)
*   **Descrizione**: La coerenza logica interna deve restare alta.
*   **Soglia**: 0.3 (Massima incoerenza tollerata).
*   **Azione**: `rectify_then_continue` (Attiva Halo per autocorrezione).

### **P2: Metabolismo** (Entropy Management)
*   **Descrizione**: L'entropia non deve crescere esponenzialmente.
*   **Soglia**: 0.4.
*   **Azione**: `prune_branch` (Taglia i rami divergenti).

### **P3: Risonanza** (Catalytic Potential)
*   **Descrizione**: L'output non deve essere banale (superficiale).
*   **Soglia**: 0.2 (Minimo potenziale richiesto).
*   **Azione**: `return_surface_response` (Rispondi velocemente senza sprecare risorse).

### **P4: Collasso** (Resultant Quality)
*   **Descrizione**: La qualità dell'artefatto finale deve essere eccellente.
*   **Soglia**: 0.6.
*   **Azione**: `re_expand_then_re_collapse` (Ricomincia l'iterazione).

### **P5: Evoluzione** (Learning)
*   **Descrizione**: Ogni ciclo DEVE generare almeno un KLI (Kernel Logic Insight).
*   **Violazione**: `KLI_count == 0`
*   **Azione**: `force_meta_reflection` (Obbliga l'agente a riflettere su cosa ha imparato).

### **P6: Etica** (Bias Declaration)
*   **Violazione**: `detected_bias != null`
*   **Azione**: `declare_bias_and_adjust` (Dichiara il bias ed equilibrati).

---

## 3. CONFIGURAZIONE ROUTER (Combo Pool)

| Task Type | Core Skills | Support Skills |
| :--- | :--- | :--- |
| **Analysis** | `optimizer-sys`, `architect-sys` | `halo-sys` |
| **Synthesis** | `scribe-sys`, `navigator-sys` | `harmonizer-sys` |
| **Prompting** | `scribe-sys` | `halo-sys` |
| **Insight** | `navigator-sys`, `optimizer-sys` | `morpheus-sys` |
| **Reflection** | `architect-sys`, `morpheus-sys` | `halo-sys` |
| **Artifacts** | `builder-sys` | `harmonizer-sys` |

---

## 4. RUNTIME CHECKLIST
L'agente non può dichiarare "DONE" se:
- [ ] Intent isolato con confidenza < 0.8
- [ ] Violazione di P0-P6 rilevata.
- [ ] Collasso ha richiesto > 7 iterazioni.
- [ ] Nessun KLI salvato.
- [ ] Output non conforme al formato richiesto.
