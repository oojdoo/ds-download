## ds-download sous linux
Télécharger toutes les pièces jointes d'une démarche effectuée sur demarches-simplifiees.fr via l'API fourni par Démarches simplifiées. 


Programme sous licence creative commons CC-Zero.    


Objectif : télécharger des pièces jointes sur demarches-simplifiees.fr via l'API. Le programme télécharge les pièces jointes avec le numéro identifiant au début des noms des pièces jointes. Ce programme n'est pas "propre" mais je l'ai simplement rédigé pour l'usage de mon lycée et je n'ai pas forcément l'intention de l'améliorer ou de le maintenir. À vous de le faire.


Mode d'emploi et configuration du fichier ds-download.py


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


Mode d'emploi sous linux : placez le programme ds-download.py dans un nouveau  dossier, ouvrez un terminal dans ce dossier, lancez le programme avec la commande ci-dessous :   

python3 ds-download.py

Remarques : pour windows, vous pouvez utiliser le shell linux. Sans cela, il me semble que ce programme peut être adapté mais je n'ai pas d'ordinateur sous windows...
