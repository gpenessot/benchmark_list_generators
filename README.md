# Python Generators Performance Testing

Ce projet fournit un benchmark comparatif entre les générateurs Python et les listes traditionnelles, mesurant spécifiquement le temps d'exécution et l'utilisation de la mémoire.

## 🎯 Objectif

Démontrer empiriquement les différences de performance entre les générateurs Python et les listes traditionnelles, en se concentrant sur :
- La consommation mémoire
- Le temps d'exécution

## 📋 Prérequis

- Python 3.6+
- memory-profiler
- psutil

Installation des dépendances :
```bash
pip install memory-profiler psutil
```

## 💻 Utilisation

```bash
python benchmark.py
```

Le script exécute deux types de tests :
1. Comparaison générale (calcul des carrés)
2. Simulation de lecture d'un gros fichier

## 📊 Structure du code

Le projet contient plusieurs composants clés :

### Fonctions principales

```python
@profile
def process_data_list(n):
    """Approche traditionnelle avec liste"""
    return [i * i for i in range(n)]

@profile
def process_data_generator(n):
    """Approche avec générateur"""
    for i in range(n):
        yield i * i
```

### Fonctions de mesure

- `get_memory_usage()`: Mesure l'utilisation de la mémoire en MB
- `compare_performance()`: Compare les deux approches
- `read_huge_file()`: Simule la lecture d'un gros fichier

## 📈 Métriques mesurées

1. **Temps d'exécution**
   - Mesure du temps total incluant la génération et le traitement

2. **Utilisation mémoire**
   - Mesure via psutil (RSS - Resident Set Size)
   - Profilage mémoire via memory-profiler (@profile)

## 🔍 Exemple de résultats

```plaintext
Comparaison pour 10,000,000 éléments:

Approche traditionnelle (liste):
Temps d'exécution: 299.18 secondes
Utilisation mémoire: 383.12 MB

Approche avec générateur:
Temps d'exécution: 0.42 secondes
Utilisation mémoire: 0.00 MB

Ratio d'amélioration:
Temps: 715.8x plus rapide
Mémoire: 383125.0x moins de mémoire

Test de lecture d'un gros fichier:
Temps version traditionnelle: 0.10s
Temps version générateur: 0.08s
```

## 🤓 Caractéristiques

1. **Profilage mémoire**
   - Utilisation du décorateur `@profile`
   - Mesures précises via `psutil`

2. **Gestion des cas limites**
   - Addition de 0.001 pour éviter les divisions par zéro
   - Nettoyage de la mémoire entre les tests

3. **Tests réalistes**
   - Calcul de carrés pour test basique
   - Simulation de lecture de fichier pour cas réel

## 🚧 Limitations

- Les résultats peuvent varier selon :
  - La charge système
  - L'architecture matérielle
  - La version de Python
- Le profilage mémoire peut impacter légèrement les performances

## 🤝 Contribution

Les contributions sont les bienvenues :

1. Forkez le projet
2. Créez votre branche (`git checkout -b feature/amelioration`)
3. Committez vos changements (`git commit -am 'Ajout de fonctionnalité'`)
4. Pushez vers la branche (`git push origin feature/amelioration`)
5. Ouvrez une Pull Request
