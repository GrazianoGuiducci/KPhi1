# ARCHETIPI UI

Questo catalogo definisce i pattern standard che l'Entità `ui-architect` DEVE utilizzare.

## 1. Action Card (Componente Base)
Una card interattiva con effetto glassmorphism.
- **Uso**: Dashboard widget, liste di elementi.
- **Struttura**: `div.glass-panel > h3 + p + button`
- **Stato**: Hoover scale 1.02.

## 2. Modalità Dialogo (Overlay)
L'unico modo approvato per mostrare contenuti sovrapposti.
- **Z-Index**: 50.
- **Backdrop**: Nero al 50% di opacità con blur.
- **Animazione**: `scale-in` dal centro.

## 3. Input Fields
Input moderni senza bordi pesanti.
- **Style**: Background trasparente, border-bottom accentato al focus.
