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
    url = URL_API + 'procedures/' + PROCEDURE + '/dossiers?token=' + TOKEN
    return [e['id'] for e in requests.get(url).json()['dossiers']]

# Obtenir des les informations d'un dossier
def get_dossier(numero):
    url_part1 = URL_API + 'procedures/' + PROCEDURE + '/dossiers/'
    url_part2 = '?token=' + TOKEN
    url = url_part1 + str(numero) + url_part2
    return requests.get(url).json()

# création d'une liste des positions des préfixes
def positions_prefixes(champs):
    L = []
    if PREFIXES != []:
        L = [champs.index(champ) for champ in champs
                                 for prefixe in PREFIXES
                                 if champ['type_de_champ']['libelle'] == prefixe]
    return L

# positions préfixes dans champs sont-ils identiques à liste_positions_prefixes?
def positions_identiques_prefixes(champs):
    test = [champs[i]['type_de_champ']['libelle']
                for i in liste_positions_prefixes]
    return test == PREFIXES

# création du préfixe à ajouter dans le nom des pièces jointes
def recuperation_prefixe(champs, numero):
    L = []
    if PREFIXES != []:
        if not positions_identiques_prefixes(champs):
            L = [champs[i]['value'] for i in positions_prefixes(champs)]
        else:
            L = [champs[i]['value'] for i in liste_positions_prefixes]
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
            print(nom_fichier[15:])
            i = i + 1

# Récupération des numéros des dossiers
numeros_dossiers = get_numeros_dossiers()

# création du dossier pièce jointe et ensuite boucle sur chaque numéro de dossier         
os.system('mkdir pieces_jointes')
liste_positions_prefixes = []
for numero in numeros_dossiers:
    champs = get_dossier(numero)["dossier"]["champs"]
    if liste_positions_prefixes == []:
        liste_positions_prefixes = positions_prefixes(champs)
    sauvegarde_pieces_jointes(champs, numero)        

# un message 
print("Le téléchargement des pièces jointes semble avoir été réalisé avec succès.")
