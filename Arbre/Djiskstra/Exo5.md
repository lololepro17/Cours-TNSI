# Exercice 5

```mermaid
graph TD;
    A -- 7 --> B;
    B -- 8 --> C;
    A -- 10 --> D;
    A -- 14 --> E;
    E -- 18 --> F;
    D -- 5 --> C;
    D -- 11 --> F;
    F -- 4 --> G;
    C -- 5 --> G;
    C -- 9 --> H;
    F -- 13 --> H;
```

## Tableau de l'algorithme de Dijkstra

| Étape | Noeud actuel | Distance depuis A | Chemin |
|-------|---------------|-------------------|--------|
| 1     | A             | 0                 | A      |
| 2     | B             | 7                 | A -> B |
| 3     | D             | 10                | A -> D |
| 4     | C             | 15                | A -> D -> C |
| 5     | F             | 21                | A -> D -> F |
| 6     | G             | 25                | A -> D -> F -> G |
| 7     | H             | 24                | A -> D -> C -> H |


## EXERCICE 8 : Durée et coût de trajets autoroutiers

Le tableau ci-dessous donne les durées et coût (péage) des trajets autoroutiers entre les principales villes du Sud de la France :

|            | Bordeaux | Clermont | Lyon  | Marseille | Montpellier | Brive  | Toulouse | Valence | Biarritz | Pau   | Grenoble |
|------------|---------|----------|-------|-----------|-------------|--------|----------|---------|----------|--------|----------|
| **Numéro** | 1       | 6        | 9     | 8         | 7           | 4      | 5        | 10      | 2        | 3      | 11       |
| Bordeaux   | -       | -        | -     | -         | -           | 16.80  | 18.00 €  | -       | 5,60 €   | 25 €   | -        |
| Clermont   | -       | -        | 13.80 | -         | 8.60        | 11.60  | -        | -       | -        | -      | 12,10 €  |
| Lyon       | -       | 1h58     | -     | -         | -           | -      | -        | 7.10    | -        | -      | -        |
| Marseille  | -       | -        | -     | -         | 10.80       | -      | -        | 16.20   | -        | -      | -        |
| Montpellier| -       | 3h26     | -     | 1h47      | -           | -      | 19.60    | 17,80 € | -        | -      | -        |
| Brive      | 2h08    | 2h10     | -     | -         | -           | -      | 15.10    | -       | -        | -      | -        |
| Toulouse   | 2h24    | -        | -     | -         | 2h28        | 2h09   | -        | -       | -        | 11,60  | -        |
| Valence    | -       | -        | 1h13  | 2h08      | 1h58        | -      | -        | -       | -        | -      | 8,80 €   |
| Biarritz   | 2h17    | -        | -     | -         | -           | -      | -        | -       | -        | 9,50 € | -        |
| Pau        | 2h10    | -        | -     | -         | -           | -      | 2h08     | -       | 1h32     | -      | -        |
| Grenoble   | -       | -        | 1h20  | -         | -           | -      | -        | 1h05    | -        | -      | -        |

```mermaid
graph TD;
    Bordeaux -- "2h08 / 16.80€" --- Brive;
    Bordeaux -- "2h24 / 18.00€" --- Toulouse;
    Bordeaux -- "2h17 / 5.60€" --- Biarritz;
    Bordeaux -- "2h10 / 25€" --- Pau;

    Clermont -- "1h58 / 13.80€" --- Lyon;
    Clermont -- "3h26 / 8.60€" --- Montpellier;
    Clermont -- "2h10 / 11.60€" --- Brive;
    Clermont -- "12.10€" --- Grenoble;

    Lyon -- "1h13 / 7.10€" --- Valence;
    Lyon -- "1h20" --- Grenoble;

    Marseille -- "1h47 / 10.80€" --- Montpellier;
    Marseille -- "2h08 / 16.20€" --- Valence;

    Montpellier -- "2h28 / 19.60€" --- Toulouse;
    Montpellier -- "1h58 / 17.80€" --- Valence;

    Brive -- "2h09 / 15.10€" --- Toulouse;

    Toulouse -- "2h08" --- Pau;
    Toulouse -- "11.60€" --- Pau;

    Valence -- "1h05 / 8.80€" --- Grenoble;

    Biarritz -- "1h32 / 9.50€" --- Pau;

``` 
