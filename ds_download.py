###################################################################
#  Programme sous licence creative commons CC0 1.0 Public Domain  #
#  https://creativecommons.org/publicdomain/zero/1.0/deed.fr      #
###################################################################

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

import requests, os, errno, platform
from urllib.parse import unquote

# Obtenir les numéros des dossiers d'une procédure
def get_numeros_dossiers(procedure, token):
    url = URL_API + 'procedures/' + procedure + '/dossiers'
    return [e['id'] for e in requests.get(url, headers={'Authorization': 'Bearer {}'.format(token)}).json()['dossiers']]

# Obtenir les informations d'un dossier
def get_champs_dossier(numero, procedure, token):
    url = URL_API + 'procedures/' + procedure + '/dossiers/' + str(numero)
    dossier = requests.get(url, headers={'Authorization': 'Bearer {}'.format(token)}).json()
    return dossier["dossier"]["champs"]

# Recherche urls des pièces jointes et création du préfixe du nom des pièces jointes
def get_urls_et_prefixe(numero, champs):
    urls_pj, prefixe_pj = [], []
    for champ in champs:
        for prefixe in PREFIXES:
            if champ['type_de_champ']['libelle'] == prefixe:
                prefixe_pj.append(champ['value'])
        url = champ['value']
        if url != None and 'http' in url and 'filename' in url:
            urls_pj.append(url)
    prefixe_pj = ' '.join([str(numero)] + prefixe_pj) if PREFIXE_NUMERO_DOSSIER else ' '.join(prefixe_pj)         
    return urls_pj, prefixe_pj

# Sauvegarde des pièces jointes dans le dossier pieces_jointes_NUMERO_PROCEDURE
def sauvegarde_pj(procedure, urls_pj, prefixe_pj):
    i = 1
    for url in urls_pj:
        response = requests.get(url)
        nom_piece = unquote(url[url.find('filename=') + len('filename='):])
        nom_fichier = 'pieces_jointes_' + procedure + '/' + prefixe_pj + ' piece ' + \
                      str(i) + ' ' + nom_piece.replace('&inline', '')
        with open(nom_fichier, 'wb') as f:
            f.write(response.content)
        print(nom_fichier[len('pieces_jointes_' + procedure + '/'):])
        i = i + 1

# Création et ouverture du dossier pièce jointe
def creation_dossier_pjs(procedure):
    dossier_pj = 'pieces_jointes_' + procedure
    try:   
        os.mkdir(dossier_pj) 
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    try:
        os_name = platform.system()
        if os_name == 'Windows':
            os.startfile(dossier_pj)
        elif os_name == 'Linux':
            os.system('xdg-open "%s"' % dossier_pj)
        elif os_name == 'Darwin':
            os.system('open "%s"' % dossier_pj)
    except:
        pass

# Lancement du programme
def lancement(procedure, token):        
    etat = False
    try :
        # boucle sur chaque numéro de dossier pour sauvegarder les pièces jointes
        numeros_dossiers = get_numeros_dossiers(procedure, token)
        if numeros_dossiers != []:
            creation_dossier_pjs(procedure)
            for numero in numeros_dossiers:
                champs = get_champs_dossier(numero, procedure, token)
                urls_pj, prefixe_pj = get_urls_et_prefixe(numero, champs)
                sauvegarde_pj(procedure, urls_pj, prefixe_pj)
                etat = True
    except:
        pass
    return etat

if __name__ == '__main__':
    if lancement(PROCEDURE, TOKEN):
        print("Le téléchargement des pièces jointes semble avoir été réalisé avec succès.")
    else:
        print("Le téléchargement a échoué. Vérifiez la configuration du fichier.")
