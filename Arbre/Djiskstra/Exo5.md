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


|
|-------|---------------|-------------------|--------|
|
|
|