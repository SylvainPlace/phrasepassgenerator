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

Génère une phrase de 4 mots en français séparés par des tirets.

### Options disponibles

| Option | Description | Défaut |
| -------- | ------------- | -------- |
| `-l, --language` | Langue du dictionnaire (fr, en) | fr |
| `-w, --words` | Nombre de mots | 4 |
| `-s, --separator` | Séparateur entre les mots | - |
| `-c, --count` | Nombre de phrases à générer | 1 |
| `--entropy` | Afficher les informations d'entropie | False |

### Exemples

```bash
# Générer une phrase de 5 mots en français
python phrasepass_generator.py -l fr -w 5

# Générer 3 phrases en anglais avec des espaces
python phrasepass_generator.py -l en -w 4 -s " " -c 3

# Afficher l'entropie
python phrasepass_generator.py --entropy
```

## Dictionnaires

Les dictionnaires se trouvent dans le dossier `dictionaries/` :

- `fr.txt` : Mots français
- `en.txt` : Mots anglais

**Important** : Pour une sécurité optimale, utilisez des dictionnaires contenant au moins 1000-7000 mots.

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
- L'entropie dépend de la taille du dictionnaire :
  - 1000 mots, 4 mots = ~40 bits
  - 7776 mots (diceware), 4 mots = ~51 bits
  - 7776 mots, 6 mots = ~77 bits
