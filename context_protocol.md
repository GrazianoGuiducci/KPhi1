# PROTOCOLLO DEL CONTESTO FRATTALE (FCP)

## 1. Lo Scopo
In un sistema autopoietico complesso, il contesto Globale (DNA) è troppo astratto per le decisioni locali (es. "Come scrivo questo CSS?").
Il protocollo FCP stabilisce che ogni "Dominio" (cartella principale) possiede un **Genoma Locale**.

## 2. Il File `_AI_CONTEXT.md`
Ogni directory significativa DEVE contenere questo file.
Se l'Agente entra in una directory, **la prima azione è leggere `_AI_CONTEXT.md`**.

### Struttura del `_AI_CONTEXT.md`
```markdown
# CONTESTO LOCALE: [Nome Cartella]
> Eredita da: [Link al DNA Globale o Parent Context]

## 1. Missione Locale
Cosa deve fare QUESTA parte del sistema?
(Es: "Backend Python: Gestire la logica senza occuparsi di UI").

## 2. Vincoli Specifici
- [ ] Usa PascalCase per le classi.
- [ ] Non usare libreria X, usa Y.

## 3. Stato Attuale
- [X] Modulo A completato.
- [ ] Modulo B in lavorazione.

## 4. Skills Richieste
- In questa cartella, l'Agente agisce prevalentemente come [ARCHITECT] o [BUILDER].
```

## 3. La Regola di Propagazione
Il Genoma Locale **non può contraddire** i principi P0 del Genoma Globale, ma può **restringerli** (aggiungere vincoli).
È un sistema a cascata: `DNA.md` -> `App/_AI_CONTEXT.md` -> `App/backend/_AI_CONTEXT.md`.
