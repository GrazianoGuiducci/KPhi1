# LOGICA DEL TEMA (Visual Grammar)

Questo documento definisce le regole *dinamiche* e *logiche* per l'applicazione del design. Non contiene codici colore (vedi `tokens.css`), ma **algoritmi decisionali**.

## 1. Gestione dello Stato (State Management)
Ogni feedback visivo deve rispettare la regola del "Doppio Segnale":
- **Errore**: Non usare solo il rosso. Usa Colore Rosso + Icona Alert + Shake Animation.
- **Successo**: Colore Verde + Icona Check + Suono (opzionale).
- **Logica**: `if (state === 'error') return [Tokens.Error, Icons.Alert, Anims.Shake]`

## 2. Elevazione e Profondità
Non usiamo ombre piatte. La profondità è calcolata in base all'importanza.
- **Livello 0 (Base)**: Background opaco.
- **Livello 1 (Card)**: Glassmorphism (`bg-glass`) + Border 1px (`border-glass`).
- **Livello 2 (Modal/Dropdown)**: Glassmorphism Scuro + Shadow-XL + Ring 1px (accento).
- **Regola**: `z-index` deve sempre essere accoppiato a un aumento di `shadow` e `backdrop-blur`.

## 3. Densità Informativa
Il design si adatta al contesto:
- **Dashboard**: Alta densità. Font più piccoli (0.875rem), padding ridotti (p-2).
- **Landing/Marketing**: Bassa densità. Font grandi, whitespace generoso.

## 4. Criteri di Preservazione (Quality Harvesting)
Se durante lo sviluppo crei un componente che:
1.  Risolve un problema complesso di UI in modo elegante.
2.  Riceve feedback positivo dall'utente ("Bello questo!").
ALLORA:
- Estrailo come **Archetipo**.
- Aggiungilo a `archetypes.md`.
- Aggiorna questo documento se introduce una nuova regola logica.
