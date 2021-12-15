# Module chatBot Externe
### Ce module fait partie d'un projet visant à créer une application basée sur le modèle Discord.

Il doit pouvoir répondre dans le chat aux demandes spécifiques de l'utilisateur.
Les demandes concernent la météo, la recherche d'un itinéraire, les actualités et la recherche d'un restaurant ou d'un cinéma.
## Requirements
- Python3 or later
- requests~=2.26.0
- Kivy~=2.0.0
- OSMPythonTools~=0.3.2
- kivymd
- pymongo

## Usage
- Ligne de commande
>python3 ...***à compléter***

## Fonctionnalités
1. **/help** : liste de toutes les commandes et leur utilité
2. **/weather** : température, probabilité de pluie et prévisions (par défaut : LLN)
   * un premier paramètre ***ville*** : choix de la localité
   * un deuxième paramètre ***chiffre*** : prévisions sur le nombre de jours (de 1 à 7)
3. **/news** : actualités nationales (par défaut)
   * un paramètre ***pays*** : actualités du pays défini
4. **/itinerary** : lien openstreetmap du trajet souhaité
   * si un seul paramètre ***adresse*** : itinéraire à partir de LLN
   * si deux paramètres ***adresse*** : itinéraire depuis la première adresse entrée
5. **/resto** : liste de restaurants (par défaut : LLN)
   * si un paramètre ***ville*** : restaurants répertoriés dans la ville définie
6. **/cine** : liste des cinémas (par défaut : LLN)
   * si un paramètre ***ville*** : cinémas répertoriés dans la ville définie
7. **/opinion** : mesure de la satisfaction de l'utilisateur
   * paramètre ***positif*** ou ***négatif*** 
   * un deuxième paramètre ***commentaire*** : avis sous forme de chaine de caractères

## Tests
Les tests peuvent être effectués à partir du répertoire tests

## Licence
MIT





