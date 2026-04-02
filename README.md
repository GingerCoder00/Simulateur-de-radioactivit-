# Désintégration — Simulateur de radioactivité

Une simulation Python de la **décroissance radioactive**, modélisée par un jeu de dés.  
Chaque atome instable a une probabilité fixe de **se désintégrer à chaque instant** —  
exactement comme en physique nucléaire.

---

## Principe scientifique

En radioactivité, chaque noyau instable a une **probabilité constante de se désintégrer**  
par unité de temps, indépendamment de son âge. C'est ce qu'on appelle la **loi de  
désintégration radioactive**.

Ce programme simule ce phénomène avec **1000 dés** :

- Chaque dé représente un **atome radioactif**
- Chaque lancer représente un **intervalle de temps** (une unité de temps)
- Un dé qui tombe sur **6** symbolise un atome qui **se désintègre**
- La probabilité de désintégration par unité de temps est donc **p = 1/6 ≈ 16,7 %**

La simulation s'arrête quand **tous les atomes se sont désintégrés**.

---

## Loi de décroissance

Le nombre d'atomes restants suit une **décroissance exponentielle** :
```
N(t) = N₀ × (5/6)^t
```

Avec :
- `N₀ = 1000` — nombre initial d'atomes
- `5/6` — probabilité de survie à chaque lancer
- `t` — nombre de lancers (unités de temps écoulées)

Cette formule est l'analogue discret de la loi physique `N(t) = N₀ × e^(-λt)`,  
où `λ` est la **constante radioactive** (ici λ = ln(6/5) ≈ 0,182).

---

## Lancer la simulation

**Prérequis :** Python 3.x — aucune dépendance externe
```bash
git clone https://github.com/ton-pseudo/desintegration.git
cd desintegration
python desintegration.py
```

---

## Exemple de sortie
```
Le nombre de 6 est de : 168
Il reste 832 dé(s)
Lancé suivant...
Le nombre de 6 est de : 141
Il reste 691 dé(s)
Lancé suivant...
...
Les 1000 dés ont été détruit en 24 lancé
```

---

## Paramètres modifiables

| Variable | Valeur par défaut | Signification physique |
|---|---|---|
| `dé` | `1000` | Taille de l'échantillon radioactif |
| Face éliminante | `6` (1/6) | Constante de désintégration λ |
| `time.sleep(1)` | `1 seconde` | Durée d'un intervalle de temps |

---

## 📁 Structure du projet
```
desintegration/
│
├── desintegration.py   # Script principal
└── README.md
```

---

## Licence

MIT — libre d'utilisation, de modification et de partage.
