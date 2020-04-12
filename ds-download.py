#########################################################
#        CONFIGURATION DU PROGRAMME                     #
#        VOUS DEVEZ MODIFIER CE QUI SUIT                #
#        LISEZ LE README POUR LES INSTRUCTIONS          #
#########################################################
procedure = "666"
token = "zezezezezezzezezezezeze"
prefixes = ("Champ1", "Champ2")
numero_dossier = False
numero_dossier_avant_prefixes = False
#########################################################
#     VOUS NE DEVEZ PAS MODIFIER CE QUI SUIT            #
#     SAUF SI VOUS AVEZ DES CONNAISSANCES EN PYTHON!    #
#########################################################

import json
import requests
import os
from urllib.parse import unquote

# Générateur de commandes curl pour télécharger les dossiers en JSON dans un dossier tmp/
def generateur_curl(identites):
    path1 = 'curl https://www.demarches-simplifiees.fr/api/v1/procedures/' + procedure + \
            '/dossiers/'
    path2 = '?token=' + token + ' > '
    os.system('mkdir tmp')
    for identite in identites:
        with open('mes_dossiers.sh', 'a') as f:
            f.write(path1 + str(identite) + path2 + 'tmp/' + str(identite) + '\n')

# création du préfixe à ajouter dans le nom des pièces jointes
def recuperation_prefixe(champs, identite):
    L = [champs.index(champ) for champ in champs
                             for prefixe in prefixes
                             if champ['type_de_champ']['libelle'] == prefixe]
    L = [champs[i]['value'] for i in L]
    if numero_dossier :
        L = [str(identite)] + L if numero_dossier_avant_prefixes else L + [str(identite)]
    return ' '.join(L)

# Fonction de recherche des pièces jointes dans le dossier et sauvegarde dans pieces_jointes/
def sauvegarde_pieces_jointes(champs, identite):
    i = 1
    for d in champs:
        url = d['value']
        if url != None and 'http' in url and 'filename' in url and '&inline' in url:
            response = requests.get(url)
            nom_piece = unquote(url[url.find('filename=') + len('filename='):url.find('&inline')])
            nom_fichier = 'pieces_jointes/' + recuperation_prefixe(champs, identite) + \
                          ' piece ' + str(i) + ' ' + nom_piece 
            with open(nom_fichier, 'wb') as f:
                f.write(response.content)
            i = i + 1

# téléchargements des méta-données des dossiers via une commande dans le shell
cmd_dossiers = 'curl https://www.demarches-simplifiees.fr/api/v1/procedures/' + \
               procedure + '/dossiers?token=' + token + ' > dossiers.json'
os.system(cmd_dossiers)

# récupération des id des dossiers et écriture d'un script rassemblant les commandes curl
# permettant de télécharger les dossiers
dossiers_id = []
with open('dossiers.json') as fichier:
    dossiers = json.load(fichier)
    dossiers_id = [e['id'] for e in dossiers['dossiers']]
    generateur_curl(dossiers_id)

# téléchargerment des dossiers en JSON via le shell pour exécuter les commandes du fichier
# mes_dossiers.sh
os.system('chmod +x mes_dossiers.sh')
os.system('./mes_dossiers.sh')

# création du dossier pièce jointe et ensuite boucle sur chaque identité (ie chaque dossier)         
os.system('mkdir pieces_jointes')
for identite in dossiers_id:
    intitule_dossier = 'tmp/'+ str(identite)
    with open(intitule_dossier) as json_file:
        data = json.load(json_file)
        sauvegarde_pieces_jointes(data["dossier"]["champs"], identite)        

# on est poli donc on nettoie après
os.system('rm dossiers.json mes_dossiers.sh tmp/*')
os.system('rmdir tmp')

# un message 
print("Le téléchargement des pièces jointes semble avoir été réalisé avec succès.")
print("Vérifiez qu'elles se trouvent bien dans le dossier 'pieces_jointes'.")
