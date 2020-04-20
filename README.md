Télécharger toutes les pièces jointes d'une démarche effectuée sur demarches-simplifiees.fr via l'API fourni par Démarches simplifiées.
Ce programme n'est pas "propre" mais je l'ai simplement rédigé pour l'usage de mon lycée et je n'ai pas forcément l'intention de l'améliorer ou de le maintenir. À vous de le faire.

Programmes sous licence creative commons CC0 1.0 - Public Domain : https://creativecommons.org/publicdomain/zero/1.0/deed.fr
To the extent possible under law, oojdoo has waived all copyright and related or neighboring rights to ds-download. This work is published from: France. 

## ds download

Vous avez trois possibilités pour utiliser ds_download :
1) sous windows, vous pouvez utiliser ds_download_windows_gui.zip qui contient un exécutable,
2) vous modifiez le fichier ds_download.py et vous le lancez dans un terminal (voir partie "ds_download sous linux"),
3) vous utilisez l'interface graphique ds_download_gui.py qu'il suffit de lancer dans un terminal (voir partie "ds_download_gui sous linux").

Pour les deux programmes, avant tout, il est nécessaire d'installer Python 3 et de vérifier que les modules python : requests, os, errno et urllib (ainsi que tkinter pour ds_download_gui.py) sont installés. Dans le cas contraire, vous pouvez les installer en utilisant ce type de commande (en remplaçant NOM_MODULE par requests pour installer requests) :

python -m pip install NOM_MODULE

## ds_download_gui_windows sous windows

Objectif : interface graphique permettant de télécharger des pièces jointes sur demarches-simplifiees.fr via l'API. Le programme télécharge les pièces jointes avec le numéro identifiant en préfixe.

Mode d'emploi : télécharger le fichier ds_download_windows_gui.zip puis l'extraire, cliquez sur ds_download_windows_gui.exe et renseignez le numéro de la procédure qui se trouve dans l'url de votre nagigateur lorsque vous modifiez votre formulaire en tant qu'admin. Exemple de numéro de procédure égal à 666.

https://www.demarches-simplifiees.fr/admin/procedures/666

Token.
En tant d'admin, passez en mode usager ou instructeur, puis en haut à droite cliquez l'icône représentant un buste, et enfin
cliquez sur "voir mon profil". Vous pouvez alors générer votre token.

Les pièces se trouveront dans le dossier pieces_jointes à la racine du dossier du programme ds_download_windows_gui.exe.

## ds_download_gui sous linux

<img src="https://github.com/oojdoo/ds-download/blob/master/ds_download_gui_capture.png" alt="Capture ds_download_gui.">

Objectif : interface graphique permettant de télécharger des pièces jointes sur demarches-simplifiees.fr via l'API. Le programme télécharge les pièces jointes avec le numéro identifiant en préfixe.

Mode d'emploi sous linux : placez les programmes ds_download.py et ds_download_gui.py dans un nouveau dossier, ouvrez un terminal dans ce dossier, lancez le programme ds_download_gui.py  avec la commande ci-dessous :   

python3 ds_download.py

Vous devez alors renseigner le numéro de la procédure qui se trouve dans l'url de votre nagigateur lorsque vous modifiez votre formulaire en tant qu'admin. Exemple de numéro de procédure égal à 666.

https://www.demarches-simplifiees.fr/admin/procedures/666

Token.
En tant d'admin, passez en mode usager ou instructeur, puis en haut à droite cliquez l'icône représentant un buste, et enfin
cliquez sur "voir mon profil". Vous pouvez alors générer votre token.


## ds_download sous linux


Objectif : télécharger des pièces jointes sur demarches-simplifiees.fr via l'API. Le programme télécharge les pièces jointes avec le numéro identifiant au début des noms des pièces jointes. Ce programme n'est pas "propre" mais je l'ai simplement rédigé pour l'usage de mon lycée et je n'ai pas forcément l'intention de l'améliorer ou de le maintenir. À vous de le faire.

Mode d'emploi et configuration du fichier ds-download.py (ouvrez le fichier ds-download.py avec un éditer de texte tel que Notepad)

Pour un nouveau formulaire, il est nécessaire de modifier le numéro de la procédure qui se trouve dans l'url de votre nagigateur lorsque vous modifiez votre formulaire en tant qu'admin. Dans le fichier ds-download.py, modifiez 666 par le numéro de votre procédure.

https://www.demarches-simplifiees.fr/admin/procedures/666

PROCEDURE = "666"

Token.
En tant d'admin, passez en mode usager ou instructeur, puis en haut à droite cliquez l'icône représentant un buste, et enfin
cliquez sur "voir mon profil". Vous pouvez alors générer votre token. Normalement, à ne modifier qu'une seule fois sauf si vous pensez que votre compte a été compromis. Dans le fichier ds-download.py, modifiez zezezezezezzezezezezeze par le token du compte administrateur.

TOKEN = "zezezezezezzezezezezeze"


Numéro de dossier. Dans la variable booléenne PREFIXE_NUMERO_DOSSIER, vous décidez si le numéro de dossier doit apparaître dans le nom de la pièce jointe (True) ou pas (False).


Préfixes. Dans la variable PREFIXES, vous pouvez ajouter des champs de la démarche que vous souhaitez utiliser pour nommer les pièces jointes téléchargées. Par exemple, PREFIXES = ["Nom", "Prénom"] aura pour effet d'ajouter le nom et le prénom de l'usager au début du nom de la pièce jointe et après le numéro de dossier s'il est activé. PREFIXES = [] n'affichera pas de valeurs de champs dans les noms des pièces jointes; dans ce cas il faut mettre PREFIXE_NUMERO_DOSSIER à True.


URL API de démarches simplifiées. Il est possible que l'URL de l'API change lors d'une mise à jour donc au cas où vous pouvez la modifier. L'URL est indiquée sur cette page : https://doc.demarches-simplifiees.fr/pour-aller-plus-loin/api


Mode d'emploi sous linux : placez le programme ds_download.py dans un nouveau  dossier, ouvrez un terminal dans ce dossier, lancez le programme avec la commande ci-dessous :   

python3 ds_download.py

Remarques : pour windows, vous pouvez utiliser le shell linux. Sans cela, il me semble que ce programme peut être adapté mais je n'ai pas d'ordinateur sous windows... En retirant la création du dossier pieces_jointes/ et en enregistrant les pièces jointes à la racine du programme, ds-download.py devrait fonctionner à partir de l'invite de commandes (cmd).
