#########################################################
#        CONFIGURATION DU PROGRAMME                     #
#        VOUS DEVEZ MODIFIER CE QUI SUIT                #
#        LISEZ LE README POUR LES INSTRUCTIONS          #
#########################################################
PROCEDURE = "666"
TOKEN = "zezezezezezzezezezezeze"
PREFIXE_NUMERO_DOSSIER = True
PREFIXES = []
URL_API = 'https://www.demarches-simplifiees.fr/api/v1/'
#########################################################
#     VOUS NE DEVEZ PAS MODIFIER CE QUI SUIT            #
#     SAUF SI VOUS AVEZ DES CONNAISSANCES EN PYTHON!    #
#########################################################

import json, requests, os
from urllib.parse import unquote

# Obtenir les numéros des dossiers d'une procédure
def get_numeros_dossiers():
    url = URL_API + 'procedures/' + PROCEDURE + '/dossiers'
    for e in requests.get(url, headers={'Authorization': 'Bearer {}'.format(TOKEN)}).json()['dossiers']:
        yield e['id'] 

# Obtenir les informations d'un dossier
def get_dossier(numero):
    url_part1 = URL_API + 'procedures/' + PROCEDURE + '/dossiers/'
    url = url_part1 + str(numero)
    return requests.get(url, headers={'Authorization': 'Bearer {}'.format(TOKEN)}).json()

# création du préfixe à ajouter dans le nom des pièces jointes
def recuperation_prefixe(champs, numero):
    L = [champ['value'] for champ in champs
                        for prefixe in PREFIXES
                        if champ['type_de_champ']['libelle'] == prefixe]
    return ' '.join([str(numero)] + L) if PREFIXE_NUMERO_DOSSIER else ' '.join(L)

# Fonction de recherche des pièces jointes dans le dossier et sauvegarde dans pieces_jointes/
def sauvegarde_pieces_jointes(champs, numero):
    i = 1
    for champ in champs:
        url = champ['value']
        if url != None and 'http' in url and 'filename' in url:
            response = requests.get(url)
            nom_piece = unquote(url[url.find('filename=') + len('filename='):])
            nom_fichier = 'pieces_jointes/' + recuperation_prefixe(champs, numero) + \
                          ' piece ' + str(i) + ' ' + nom_piece.replace('&inline', '')
            with open(nom_fichier, 'wb') as f:
                f.write(response.content)
            print(nom_fichier[len('pieces_jointes/'):])
            i = i + 1

# Récupération des numéros des dossiers sous la forme d'un générateur
numeros_dossiers = get_numeros_dossiers()

# création du dossier pièce jointe et ensuite boucle sur chaque numéro de dossier         
os.system('mkdir pieces_jointes')
for numero in numeros_dossiers:
    champs = get_dossier(numero)["dossier"]["champs"]
    sauvegarde_pieces_jointes(champs, numero)        

# un message 
print("Le téléchargement des pièces jointes semble avoir été réalisé avec succès.")
