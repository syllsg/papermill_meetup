# Automatisation et paramétrage de notebooks jupyter avec Papermill
Présentation et démonstration de l'utilisation de papermill lors du meet up Python du 24/06/2025 à Grenoble.<br>
[Lien](https://docs.google.com/presentation/d/1iX4lNjmOiiK2Q27c5mWHJK-Gyp1cY0Y1s9tZoZ6qVhY/edit?usp=sharing) vers la présentation.<br>
Dans ce repo, vous trouverez les fichiers nécéssaires pour tester papermill et refaire la démonstration que j'ai réalisée lors de la présentation le 24 juin.

#Installation
Dépendances : 
[Python](https://www.python.org/downloads/release/python-3923/) 3.9
[UV](https://docs.astral.sh/uv/) comme gestionnaire de paquets
Installez UV, clonez le repo puis installez les dépandances avec : 
```bash
uv pip install -r pyproject.toml
```

# Démonstration
C'est parti pour tester papermill 💻 

## Exécuter un notebook en injectant un paramètre en ligne de commande
Exécuter le notebook date_print.ipynb pour voir la date affichée
Puis ouvrez un terminal et tappez la commande suivante:
```bash
papermill -p month 06 date_print.ipynb output.ipynb
```
Le notebook est exécuté en modifiant le mois et un notebook output.html est créé qui contient une cellule supplémentaire appelée "injected_parameters"

## Exécuter un notebook en injectant 2 paramètres en ligne de commande
Dans le terminal, tappez la commande suivante qui va exécuter le notebook output.ipynb et modifier 2 paramètres
```bash
papermill -p month 06 -p year 2026 date_print.ipynb output.ipynb
```
## Exécuter puis exporter en html un notebook en injectant un paramètre en ligne de commande
Il est possible de caster le notebook exécuté avec un paramètre modifé directement dans nbconvert qui va exporter le notebook en html. Seul le fichier report_html.html est créé, le notebook modifié n'est pas sauvegardé.
Dans le terminal, tappez la commande suivante:
```bash
papermill -p year 2030 date_print.ipynb | jupyter-nbconvert --stdin --no-input --to html --output report_html
```
## Exécuter un notebook en injectant 3 paramètres avec un script python
Inspectez le script papermill_api.py
Puis dans le terminal tappez:
```bash
python papermill_api.py 
```
Le script s'éxécute. Il éxécute le notebook en modifant la date et le notebook modifié est sauvegardé sous le nom date_print_2026.ipynb

## Exécuter tous les notebooks présents dans un dossier
Ici le dossier "execute_all_folder " contient plusieurs notebooks. 
Il est possible de tous les exécuter en exécutant le script execute_all_notebooks.py
```bash
python execute_all_notebooks.py 
```

