# 🎙️ Grand Oral NSI – Sujet : Comment un ordinateur exécute-t-il un programme écrit en Python ?

## Introduction

Bonjour à toutes et à tous,

Aujourd’hui, nous allons explorer la question suivante :  
**Comment un ordinateur exécute-t-il un programme écrit en Python ?**

Quand nous écrivons du code en Python, il peut sembler que l’ordinateur comprend ce que nous saisissons. En réalité, il ne traite que des séquences de 0 et de 1, c'est-à-dire du langage binaire.

Alors, comment passe-t-on d’un script Python à des instructions compréhensibles par le processeur ?

---

## 🧱 I – De Python au langage machine

Python est un **langage de haut niveau** conçu pour être intuitif et accessible aux humains.

Mais pour qu’un ordinateur puisse exécuter un programme Python, le code doit d’abord être **traduit**.  
Cette traduction est réalisée par un **interpréteur Python**.

L’interpréteur convertit le code source en **bytecode**, une forme intermédiaire plus proche du langage machine.  
Ce bytecode est ensuite exécuté par une **machine virtuelle Python** (PVM).

Contrairement aux langages compilés comme le C, Python est **interprété** : chaque instruction est traduite et exécutée au fur et à mesure.

---

## ⚙️ II – Le rôle du matériel : l’architecture de von Neumann

Une fois le code converti, c’est le **processeur (CPU)** qui prend le relais.  
Le processeur suit le **cycle d’exécution** composé de trois étapes : *fetch*, *decode* et *execute*.

En pratique, il :

- **Fetch** (récupère) une instruction depuis la mémoire,
- **Decode** (décode) l’instruction pour en comprendre le sens,
- **Execute** (exécute) l’instruction.

Ce fonctionnement repose sur l’**architecture de von Neumann**, dans laquelle les **instructions** et les **données** sont stockées dans la **mémoire RAM**.

Pendant l’exécution, le processeur utilise aussi des **registres**, des mémoires très rapides pour stocker temporairement des informations.

---

## 🔗 III – Le lien entre Python et le matériel

Toutes les informations — instructions, nombres, caractères — sont finalement **converties en binaire** (0 et 1).  
Par exemple, l’instruction `x = 5` en Python devient une valeur binaire enregistrée en mémoire.

Ensuite, le processeur exécute des **instructions simples** en manipulant ces bits.

On peut voir ce processus comme une série de **couches d’abstraction** :

- le code source (Python),
- l’interpréteur,
- le système d’exploitation,
- le matériel.

Chaque couche s’appuie sur la précédente, ce qui offre une grande **flexibilité**.

---

## 📌 Exemple pour illustrer

```python
x = 3
x = x + 2
print(x)
```
