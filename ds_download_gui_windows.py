# -*- coding: utf-8 -*-
###################################################################
#  Programme sous licence creative commons CC0 1.0 Public Domain  #
#  https://creativecommons.org/publicdomain/zero/1.0/deed.fr      #
###################################################################

import requests, os, errno
from urllib.parse import unquote
import tkinter as tk

URL_API = 'https://www.demarches-simplifiees.fr/api/v1/'

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
    urls_pj = []
    for champ in champs:
        url = champ['value']
        if url != None and 'http' in url and 'filename' in url:
            urls_pj.append(url)        
    return urls_pj, str(numero)

# Sauvegarde des pièces jointes dans le dossier pieces_jointes/
def sauvegarde_pj(urls_pj, prefixe_pj):
    i = 1
    for url in urls_pj:
        response = requests.get(url)
        nom_piece = unquote(url[url.find('filename=') + len('filename='):])
        nom_fichier = 'pieces_jointes/' + prefixe_pj + ' piece ' + str(i) + \
                      ' ' + nom_piece.replace('&inline', '')
        with open(nom_fichier, 'wb') as f:
            f.write(response.content)
        print(nom_fichier[len('pieces_jointes/'):])
        i = i + 1
        
def lancement(procedure, token):
    # Création du dossier pièce jointe et ensuite boucle sur chaque numéro de dossier         
    etat = False
    try:
        os.mkdir('pieces_jointes')
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    try :
        for numero in get_numeros_dossiers(procedure, token):
            champs = get_champs_dossier(numero, procedure, token)
            urls_pj, prefixe_pj = get_urls_et_prefixe(numero, champs)
            sauvegarde_pj(urls_pj, prefixe_pj)
            etat = True
    except:
        pass
    return etat

# Contruction de l'interface graphique
def build_frame(titre, window, liste):
    def recupere_proc():
        if lancement(liste_entries[0].get(), liste_entries[1].get()):
            text.set('Dans le dossier du programme, regardez dans le dossier pieces_jointes.')
            etat.config(bg="green", fg="white") 
        else:
            text.set('   Le téléchargement a échoué. Vérifiez les deux champs ci-dessus.    ')
            etat.config(bg="red", fg="white")
    frame = tk.LabelFrame(window, text=titre, padx = 20, pady = 20)
    liste_labels = [tk.Label(frame, text=e + ' :') for e in liste]
    text = tk.StringVar()
    text.set('    Complétez les deux champs et soyez patient après avoir validé.    ')
    etat = tk.Label(frame, textvariable=text)
    liste_variables = [tk.StringVar() for e in liste]
    liste_entries = [tk.Entry(frame, textvariable=v, width = 29) for v in liste_variables]
    button_submit = tk.Button(frame, text = "    Valider   ", command=recupere_proc)
    for i in range(len(liste)):
        liste_labels[i].grid(row = i, column = 0)
        liste_entries[i].grid(row = i, column = 1)
    button_submit.grid(row = len(liste), columnspan = 2)
    etat.grid(row = 3, columnspan = 2)
    frame.grid(sticky="nsew")

# lancement du programme
fenetre = tk.Tk()
fenetre.title('ds download gui')
fenetre.resizable(width=False, height=False)
frame = build_frame("Configuration de la procédure",
                    fenetre, ["Numéro de procédure", "Token"])
fenetre.mainloop()
