# 🎙️ Grand Oral NSI – Sujet : Comment un ordinateur exécute-t-il un programme écrit en Python ?

## Introduction

Bonjour,

Aujourd’hui, je vais répondre à la question :  
**Comment un ordinateur exécute-t-il un programme écrit en Python ?**

Quand on programme en Python, on a l’impression que l’ordinateur « comprend » ce qu’on écrit. Mais en réalité, un ordinateur ne comprend que des suites de 0 et de 1, ce qu’on appelle le langage binaire.

Alors, comment passe-t-on d’un code Python à quelque chose que le processeur peut exécuter ?

---

## 🧱 I – De Python au langage machine

Python est un **langage de haut niveau** : il est conçu pour être facile à lire et à écrire pour nous, les humains.

Mais pour qu’un ordinateur puisse l’exécuter, ce code doit être **traduit**.  
Cette traduction se fait grâce à un **interpréteur Python**.

L’interpréteur transforme le code source en **bytecode**, une forme intermédiaire plus proche du langage machine.  
Ce bytecode est ensuite exécuté par une **machine virtuelle Python** (PVM).

Contrairement à des langages compilés comme le C, Python est **interprété** : chaque ligne est traduite et exécutée au fur et à mesure.

---

## ⚙️ II – Le rôle du matériel : architecture de von Neumann

Une fois que le code est prêt à être exécuté, c’est le **processeur (CPU)** qui entre en action.  
Il suit le **cycle d’exécution** : *fetch*, *decode*, *execute*.

Cela signifie qu’il va :
- chercher une instruction en mémoire (**fetch**),
- la comprendre (**decode**),
- puis l’exécuter (**execute**).

Cette organisation repose sur l’**architecture de von Neumann**, où les **instructions** et les **données** sont stockées dans la **mémoire RAM**.

Pendant l’exécution, le processeur utilise aussi des **registres**, des mémoires très rapides pour les opérations temporaires.

---

## 🔗 III – Le lien entre Python et le matériel

Toutes les instructions, les nombres, les caractères, tout est **converti en binaire** (0 et 1).  
Par exemple, `x = 5` en Python devient une valeur binaire stockée dans la mémoire.

Ensuite, le processeur va exécuter des **instructions simples**, en manipulant ces bits.

Il existe donc plusieurs **couches d’abstraction** :
- le code source (Python),
- l’interpréteur,
- le système d’exploitation,
- le matériel.

Chaque couche repose sur la précédente, ce qui permet une grande **modularité**.

---

## 📌 Petit exemple pour illustrer

```python
x = 3
x = x + 2
print(x)
