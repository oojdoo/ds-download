###################################################################
#  Programme sous licence creative commons CC0 1.0 Public Domain  #
#  https://creativecommons.org/publicdomain/zero/1.0/deed.fr      #
###################################################################
try:
    import tkinter as tk
except:
    import Tkinter as tk
import ds_download

def build_frame(titre, window, liste):
    def recupere_proc():
        if ds_download.lancement(liste_entries[0].get(), liste_entries[1].get()):
            text.set('Les pièces jointes se trouvent dans le dossier pieces_jointes.')
            etat.config(bg="green", fg="white") 
        else:
            text.set("Le téléchargement a échoué.Vérifiez les deux champs ci-dessus.")
            etat.config(bg="red", fg="white")
    frame = tk.LabelFrame(window, text=titre, padx = 20, pady = 20)
    liste_labels = [tk.Label(frame, text=e + ' :') for e in liste]
    text = tk.StringVar()
    text.set('Complétez les deux champs et soyez patient après avoir validé.')
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

if __name__ == '__main__': 
    fenetre = tk.Tk()
    fenetre.title('ds_download_gui')
    fenetre.geometry('468x158')
    fenetre.resizable(width=False, height=False)
    frame = build_frame("Configuration de la procédure",
                        fenetre, ["Numéro de procédure", "Token"])
    fenetre.mainloop()
