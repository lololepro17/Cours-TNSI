# Grand Oral – Comment reCAPTCHA v3 utilise les probabilités pour détecter les humains ?

## Problématique

**Comment les sites web utilisent-ils reCAPTCHA v3 pour distinguer un humain d’un robot à l’aide des probabilités ?**

---

## Plan

### I. Qu’est-ce que reCAPTCHA v3 ?

- Système de Google pour protéger les sites contre les robots.
- Contrairement aux anciens CAPTCHA, **aucune interaction visuelle**.
- Il observe **le comportement de l’utilisateur** (clics, mouvements, frappe…).
- Il donne un **score entre 0 et 1** → correspond à la **probabilité d’être un humain**.

---

### II. Comment sont utilisées les probabilités ?

#### Étapes

1. **Collecte de données** comportementales :
   - Mouvement de souris, vitesse de frappe, temps passé…
2. **Modélisation mathématique** :
   - Utilisation de **modèles statistiques**, comme la **régression logistique**.
3. **Calcul du score** (fonction sigmoïde) :
   \[
   P(\text{humain}) = \frac{1}{1 + e^{-(a_0 + a_1x_1 + a_2x_2 + \dots + a_nx_n)}}
   \]
   - \(x_i\) : variables observées
   - \(a_i\) : coefficients appris à partir de données réelles
   - Le résultat est une **probabilité** entre 0 (robot) et 1 (humain)

#### Interprétation

- \( P > 0.9 \) → humain → accès au site
- \( P < 0.3 \) → robot → blocage ou vérification
- Le système apprend en continu avec de nouvelles données

---

### III. Limites et critiques

- **Respect de la vie privée** : collecte discrète de données sans consentement clair.
- **Biais possible** : utilisateurs atypiques ou en situation de handicap mal détectés.
- **Évolution des robots** : certains arrivent à imiter les comportements humains.

---

## Réponses aux questions possibles du jury

### Q : En pratique, comment utilise-t-on les probabilités ?

On observe le comportement (clics, frappes, etc.), on compare aux comportements typiques d’humains, et on calcule une **probabilité d’être humain** grâce à un modèle statistique.

---

### Q : Quels sont les calculs faits ?

On fait une **combinaison linéaire pondérée** des comportements observés, puis on applique une **fonction sigmoïde** pour transformer ce score en **probabilité entre 0 et 1**.

---

### Q : D’où vient la formule ?

Elle vient de la **régression logistique**, utilisée pour prédire la probabilité d’appartenir à une classe (ici : humain ou robot), à partir de plusieurs variables mesurées.

---

### Q : La fonction sigmoïde est-elle au programme ?

Non, pas directement, mais elle repose sur l’**exponentielle**, qui elle **est au programme**. On peut donc l’utiliser si on l’explique bien.

---

## Fonction sigmoïde (forme en S)

\[
f(x) = \frac{1}{1 + e^{-x}}
\]

- Quand \( x \to -\infty \), \( f(x) \to 0 \)
- Quand \( x \to +\infty \), \( f(x) \to 1 \)
- Idéale pour transformer un score brut en probabilité

---

## Point clé

- reCAPTCHA v3 fonctionne sans interaction visible.
- Il se base sur les **comportements en ligne**, traités par un modèle probabiliste.
- Le score de confiance est une **probabilité** calculée avec une fonction sigmoïde.
- Ce système allie **maths, probabilités, et informatique** pour sécuriser le web.
