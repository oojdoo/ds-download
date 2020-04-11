## ds-download sous linux
Télécharger toutes les pièces jointes sur demarches-simplifiees.fr via l'API fourni par Démarches simplifiées. 
Programme sous licence creative commons CC-Zero       


Objectif : télécharger des pièces jointes sur demarches-simplifiees.fr via l'API
Le programme télécharge les pièces jointes avec le numéro identifiant au début
du nom des pièces jointes.
Ce programme n'est pas "propre" mais je l'ai simplement rédigé pour l'usage de
mon lycée et je n'ai pas forcément l'intention de l'améliorer ou de le maintenir. 
À vous de le faire.

Pour un nouveau formulaire, il est nécessaire de modifier
le numéro de la procédure ce qui se trouve dans l'url
lorsque vous modifiez votre formulaire en tant qu'admin.

https://www.demarches-simplifiees.fr/admin/procedures/666

procedure = "666"                     # laissez les guillemets

Token
En tant d'admin, passez en mode usager ou instructeur, puis
en haut à droite cliquez l'icône représentant un buste, et enfin
cliquez sur "voir mon profil". Vous pouvez alors générer votre
token. Normalement, à ne modifier qu'une seule fois sauf si vous
pensez que votre compte a été compromis.

token = "zezezezezezzezezezezeze"      # laissez les guillemets

Mode d'emploi sous linux : placez le programme ds-download.py dans un nouveau 
dossier, ouvrez un terminal dans ce dossier, lancez le programme avec la commande
ci-dessous    

python3 ds-download.py
