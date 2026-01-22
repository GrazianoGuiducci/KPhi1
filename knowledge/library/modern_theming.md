# PATTERN: Modern Theming System (CSS Variables)
> Tags: #css #ui #theming #reusable

## 1. Concetto
Invece di hard-codare i colori, usiamo variabili CSS root e classi di utilità semantiche.

## 2. Implementazione Base (`style.css`)
```css
:root {
    /* Palette Semantica */
    --color-bg-primary: #0a0a0a;
    --color-text-main: #ffffff;
    --color-accent: #00ff88; /* Neon Green */
    
    /* Spacing */
    --spacing-unit: 8px;
}

body {
    background-color: var(--color-bg-primary);
    color: var(--color-text-main);
}
```

## 3. Regola di Applicazione
- Quando applichi questo pattern, sovrascrivi qualsiasi CSS esistente che usa colori diretti (es: `background: black`).
- Genera sempre un file `theme.css` separato se possibile.
