[![Test Module Bot](https://github.com/CardinPatson/noyau_devII_2TM2/actions/workflows/test_module_bot.yml/badge.svg)](https://github.com/CardinPatson/noyau_devII_2TM2/actions/workflows/test_module_bot.yml)
[![Build](https://github.com/CardinPatson/noyau_devII_2TM2/actions/workflows/build.yml/badge.svg)](https://github.com/CardinPatson/noyau_devII_2TM2/actions/workflows/build.yml)
[![PyPI version](https://badge.fury.io/py/Bot-Externe.svg)](https://pypi.org/project/Bot-Externe/)
[![Release](https://img.shields.io/github/v/release/CardinPatson/noyau_devII_2TM2)](https://libraries.io/pypi/Bot-Externe)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

---
# ChatBot Externe 
Ce module fait partie du Projet EpheCom de la Haute-Ecole Ephec projet visant à créer une application basée sur le modèle Discord.

Il doit pouvoir répondre dans le chat aux demandes spécifiques de l'utilisateur.

Les demandes concernent la météo, les itinéraires, les actualités et la recherche d'un restaurant ou d'un cinéma.

## Requirements

- Python3 or later
- requests~=2.26.0
- urllib3==1.26.6
- pymongo
- pytest


# Usage

## Connexion à la db

Récupérer une clé de connexion à la BD, la renommer en **db_key.pem**  et la mettre dans le dossier **src/data**

## Mise en place


*NB : Le Bot devrait être fonctionnel peu importe l'OS utilisé*

### Installation depuis pypi

---

```
pip install Bot-Externe
```

Pour tester le bot veuillez tout d'abord à l'importer dans un fichier python; La liste des commandes disponible se trouve dans la section Fonctionnalité 

```
from Bot.bot import Bot

   if __name__ == "__main__":
      print(Bot("/help"))
```

### Installation depuis Github

---
Dans le cas ou vous cloné le répo veuillez à suivre les étapes suivantes suivant votre système d'exploitation 
### Configuration de la directory root

***
Dans le dossier **src/data/config.py** renommer la variable **ROOT_DIRECTORY** comme suit :
```
ROOT_DIRECTORY=nom_du_dossier_contenant_le_projet
```
### Linux

---
```
python3 -m venv env
./env/bin/activate
pip install -r requirements.txt
python main.py
```
### Windows

---
```
python3 -m venv env  
env\Scripts\Activate.ps1
pip install -r requirements.txt 
python main.py
```

## Fonctionnalités


>1. **/help** : liste de toutes les commandes et leur utilité

>2. **/weather** : température, probabilité de pluie et prévisions (par défaut : LLN)
   >* un premier paramètre ***ville*** : choix de la localité

>3. **/news** : actualités nationales (par défaut)
   >* un paramètre ***pays*** : actualités du pays défini

>4. **/itinerary** : lien openstreetmap du trajet souhaité
   >* si un seul paramètre ***adresse*** : itinéraire à partir de LLN
   >* si deux paramètres ***adresse*** : itinéraire depuis la première adresse entrée

>5. **/resto** : liste de restaurants (par défaut : LLN)
   >* si un paramètre ***ville*** : restaurants répertoriés dans la ville définie

>6. **/cine** : liste des cinémas (par défaut : LLN)
   >* si un paramètre ***ville*** : cinémas répertoriés dans la ville définie

>7. **/opinion** : mesure de la satisfaction de l'utilisateur
   >* paramètre ***positif*** ou ***négatif*** 
   >* un deuxième paramètre ***commentaire*** : avis sous forme de chaine de caractères

## Tests

*Les tests peuvent être effectués à partir du répertoire tests*
```
python -m unittest test/test.py
```

## Licence
MIT




