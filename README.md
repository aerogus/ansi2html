# ansi2html

Pour une meilleure lisibilité, un journal de log peut contenir des couleurs ANSI. Il est parfois difficile de lire ce type de fichiers dans les éditeurs de texte à cause de l'ajout de caractères d'échappement.

Voici un outil pour convertir ce format en fichier HTML facilement lisible avec un navigateur.

Les dépendances sont `python3` et un module `ansi2html` installable via :

```bash
pip3 install ansi2html
```

Usage:

```bash
cat appli.log | ansi2html > appli.log.html
```

