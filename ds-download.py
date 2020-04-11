#########################################################
# Programme sous licence creative commons CC-Zero       #
#########################################################

# Objectif : télécharger des pièces jointes sur demarches-simplifiees.fr via l'API
# Le programme télécharge les pièces jointes avec le numéro identifiant au début
# du nom des pièces jointes.
# Ce programme n'est pas "propre" mais je l'ai simplement rédigé pour l'usage de
# mon lycée et je n'ai pas forcément l'intention de l'améliorer ou de le maintenir. 
# À vous de le faire.

#########################################################
#        CONFIGURATION DU PROGRAMME                     #
#        VOUS POUVEZ MODIFIER CE QUI SUIT               #
#########################################################
# Pour un nouveau formulaire, il est nécessaire de modifier
# le numéro de la procédure ce qui se trouve dans l'url
# lorsque vous modifiez votre formulaire en tant qu'admin.
# https://www.demarches-simplifiees.fr/admin/procedures/666
procedure = "666"                     # laissez les guillemets

# Token
# En tant d'admin, passez en mode usager ou instructeur, puis
# en haut à droite cliquez l'icône représentant un buste, et enfin
# cliquez sur "voir mon profil". Vous pouvez alors générer votre
# token. Normalement, à ne modifier qu'une seule fois sauf si vous
# pensez que votre compte a été compromis.
token = "zezezezezezzezezezezeze"      # laissez les guillemets

# mode d'emploi sous linux : placez le programme ds-download.py dans un nouveau 
# dossier, ouvrez un terminal dans ce dossier, lancez le programme avec la commande
# suivante    python3 ds-download.py

#########################################################
#     VOUS NE DEVEZ PAS MODIFIER CE QUI SUIT            #
#     SAUF SI VOUS AVEZ DES CONNAISSANCES EN PYTHON!    #
#########################################################

import json
import requests
import os
from urllib.parse import unquote

path1 = 'curl https://www.demarches-simplifiees.fr/api/v1/procedures/' + procedure + '/dossiers/'
path2 = '?token=' + token + ' > '

# commandes dans le shell
cmd_dossiers = 'curl https://www.demarches-simplifiees.fr/api/v1/procedures/' + procedure + '/dossiers?token=' + token + ' > dossiers.json'
os.system(cmd_dossiers)

dossiers_id = []

# récupération des id des dossiers et écriture d'un script rassemblant les commandes curl
# permettant de télécharger les dossiers
with open('dossiers.json') as fichier:
    dossiers = json.load(fichier)
    dossiers_id = [e['id'] for e in dossiers['dossiers']]
    for identite in dossiers_id:
        with open('mes_dossiers.sh', 'a') as f:
            f.write(path1 + str(identite) + path2 + 'tmp/' + str(identite) + '\n')

# téléchargerment des dossiers via le shell pour exécuter les commandes du fichier mes_dossiers.sh
os.system('mkdir tmp')
os.system('chmod +x mes_dossiers.sh')
os.system('./mes_dossiers.sh')

# création du dossier pièce jointe et ensuite boucle sur chaque identité (ie chaque dossier)
os.system('mkdir pieces_jointes')           
for identite in dossiers_id:
    intitule_dossier = 'tmp/'+ str(identite)
    with open(intitule_dossier) as json_file:
        data = json.load(json_file)
        
        # Recherche des pièces jointes dans le dossier et sauvegarde. 
        i = 1
        for d in data["dossier"]["champs"]:
            url = d['value']
            if url != None and 'http' in url and 'filename' in url and '&inline' in url:
                response = requests.get(url)
                nom_piece = unquote(url[209 + len('filename='):url.find('&inline')])
                nom_fichier = 'pieces_jointes/'+ str(identite) +' piece '+ str(i)+ ' '+ nom_piece 
                with open(nom_fichier, 'wb') as f:
                    f.write(response.content)
                i = i + 1

# on est poli donc on nettoie après
os.system('rm dossiers.json mes_dossiers.sh tmp/*')
os.system('rmdir tmp')

# un message 
print("Le téléchargement des pièces jointes semble avoir été réalisé avec succès.")
print("Vérifiez qu'elles se trouvent bien dans le dossier 'pieces_jointes'.")
