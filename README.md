# Générateur de Phrases de Passe

Un générateur de phrases de passe sécurisées avec support multilingue (français et anglais).

## Fonctionnalités

- 🔒 Génération cryptographiquement sécurisée (module `secrets`)
- 🌍 Support de plusieurs langues (français, anglais)
- ⚙️ Longueur personnalisable
- 📊 Calcul d'entropie
- 🎯 Interface en ligne de commande simple

## Installation

Aucune dépendance externe nécessaire, Python 3.6+ suffit.

```bash
git clone <votre-repo>
cd phrasepassgenerator
```

## Utilisation

### Commande de base

```bash
python phrasepass_generator.py
```

Génère une phrase de 3 mots en français avec majuscules et sans séparateur (ex: `ChevalMontagneLivre`).

### Options disponibles

| Option | Description | Défaut |
| -------- | ------------- | -------- |
| `-l, --language` | Langue(s) du dictionnaire : `fr`, `en`, ou `fr,en` pour mélanger | fr |
| `-w, --words` | Nombre de mots | 3 |
| `-s, --separator` | Séparateur entre les mots (ex: `-s "-"` pour tirets, `-s " "` pour espaces) | (vide) |
| `-c, --count` | Nombre de phrases à générer | 1 |
| `-C, --capitalize` | Mettre une majuscule au début de chaque mot | True |
| `--no-capitalize` | Désactiver les majuscules | - |
| `--entropy` | Afficher les informations d'entropie | False |

### Exemples

```bash
# Générer une phrase par défaut (3 mots, majuscules, sans séparateur)
python phrasepass_generator.py
# Résultat : ChevalMontagneLivre

# Générer avec des tirets comme séparateur
python phrasepass_generator.py -l fr -w 5 -s "-"
# Résultat : Cheval-Montagne-Livre-Fenetre-Soleil

# Générer 3 phrases en anglais avec des espaces
python phrasepass_generator.py -l en -w 4 -s " " -c 3

# Mélanger français et anglais pour plus d'entropie
python phrasepass_generator.py -l fr,en -w 6

# Sans majuscules (minuscules uniquement)
python phrasepass_generator.py -l fr -w 4 --no-capitalize -s "-"
# Résultat : cheval-montagne-livre-fenetre

# Afficher l'entropie avec les deux langues
python phrasepass_generator.py -l fr,en --entropy
```

## Dictionnaires

Les dictionnaires se trouvent dans le dossier `dictionaries/` :

- `fr.txt` : 336 054 mots français (≥ 4 lettres)
- `en.txt` : 367 522 mots anglais (≥ 4 lettres)

Les mots de moins de 4 lettres ont été filtrés pour améliorer la sécurité et la lisibilité.

### Format des dictionnaires

Un mot par ligne, en minuscules :

```bash
cheval
montagne
livre
...
```

## Sécurité

- Utilise le module `secrets` de Python pour une génération cryptographiquement sécurisée
- **Entropie avec les dictionnaires actuels :**
  
  **Français (336 054 mots) :**
  - 3 mots = **55.08 bits** ✓ Bon (défaut)
  - 4 mots = **73.43 bits** ✓ Excellent
  - 5 mots = **91.79 bits** ✓ Très sûr
  - 6 mots = **110.15 bits** ✓ Extrêmement sûr
  
  **Anglais (367 522 mots) :**
  - 3 mots = **55.46 bits** ✓ Bon (défaut)
  - 4 mots = **73.95 bits** ✓ Excellent
  - 5 mots = **92.44 bits** ✓ Très sûr
  - 6 mots = **110.93 bits** ✓ Extrêmement sûr
  
  **Français + Anglais (703 576 mots) :**
  - 3 mots = **58.27 bits** ✓ Très bon (défaut)
  - 4 mots = **77.69 bits** ✓ Excellent
  - 5 mots = **97.12 bits** ✓ Très sûr
  - 6 mots = **116.54 bits** ✓ Extrêmement sûr

- **Recommandations :**
  - Minimum 50 bits pour usage personnel
  - 70+ bits recommandé pour comptes sensibles
  - 100+ bits pour données hautement confidentielles
  - **Mélanger les langues augmente l'entropie et la résistance aux attaques par dictionnaire**
