from tkinter import *

def menu():
    #création de la fenêtre principale
    fenetre = Tk()
    fenetre.title("Snake Project")
    fenetre.iconbitmap("grand_devoreur.ico")
    fenetre.config(bg="black")
    fenetre.geometry("800x600")

    #titre du jeu
    titre = Label(fenetre, text="SNAKE", font=("Helvetica", 50, "bold"), fg="green", bg="black")
    titre.pack(pady=20)

    #choix des carreaux
    Label(fenetre, text="Taille des carreaux", font=("Helvetica", 14), fg="white", bg="black").pack()
    ListCar = ["20", "40", "60"]
    varCar = StringVar(fenetre)
    varCar.set(ListCar[0])
    car = OptionMenu(fenetre, varCar, *ListCar)
    car.config(width=30, font=("Helvetica", 12))
    car.pack(pady=10)

    #choix de la musique
    Label(fenetre, text="Musique", font=("Helvetica", 14), fg="white", bg="black").pack()
    ListMu = ["Ninjago saison 5", "Geometry Dash"]
    varMu = StringVar(fenetre)
    varMu.set(ListMu[0])
    mu = OptionMenu(fenetre, varMu, *ListMu)
    mu.config(width=30, font=("Helvetica", 12))
    mu.pack(pady=10)

    #choix du mode de jeu
    Label(fenetre, text="Mode de jeu", font=("Helvetica", 14), fg="white", bg="black").pack()
    ListMo = ["Solo", "Multijoueur"]
    varMo = StringVar(fenetre)
    varMo.set(ListMo[0])
    mo = OptionMenu(fenetre, varMo, *ListMo)
    mo.config(width=30, font=("Helvetica", 12))
    mo.pack(pady=10)

    varNB = StringVar(fenetre)

    #frame pour IA ou joueurs (permet de les afficher/supprimer facilement)
    frame_options = Frame(fenetre, bg="black")
    frame_options.pack()

    #Fonction pour afficher dynamiquement l'option correcte
    def update_options(*args):
        #Supprime les widgets actuels dans frame_options
        for widget in frame_options.winfo_children():
            widget.destroy()

        if varMo.get() == "Solo":
            Label(frame_options, text="Nombre d'IA", font=("Helvetica", 14), fg="white", bg="black").pack()
            ListIA = ["1", "2", "3", "4", "5"]
            varNB.set(ListIA[0])
            ia = OptionMenu(frame_options, varNB, *ListIA)
            ia.config(width=30, font=("Helvetica", 12))
            ia.pack(pady=10)
        else:
            Label(frame_options, text="Nombre de joueurs", font=("Helvetica", 14), fg="white", bg="black").pack()
            ListJp = ["1", "2", "3", "4"]
            varNB.set(ListJp[0])
            jp = OptionMenu(frame_options, varNB, *ListJp)
            jp.config(width=30, font=("Helvetica", 12))
            jp.pack(pady=10)

    #renvoie du nombre de joueurs

    #Lier la fonction à tout changement de mode de jeu
    nombre = varMo.trace("w", update_options)
    update_options()

    #Lancement de la fenêtre
    fenetre.mainloop()

    return varCar.get(), varMu.get(), varMo.get(), varNB.get()

print(menu())