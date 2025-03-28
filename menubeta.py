from tkinter import *

def menu():
    #création de la fenêtre principale
    fenetre = Tk()
    fenetre.title("Snake Project")
    # fenetre.iconbitmap("grand_devoreur.ico")
    fenetre.config()
    fenetre.geometry("800x650")

    #titre du jeu
    titre = Label(fenetre, text="SNAKE", font=("Helvetica", 50, "bold"), fg="green")
    titre.pack(pady=20)

    #choix des carreaux
    Label(fenetre, text="Taille des carreaux", font=("Helvetica", 14), fg="white").pack()
    ListCar = ["30", "40", "50"]
    varCar = IntVar(fenetre)
    varCar.set(ListCar[0])
    car = OptionMenu(fenetre, varCar, *ListCar)
    car.config(width=30, font=("Helvetica", 12))
    car.pack(pady=10)

    #choix de la musique
    Label(fenetre, text="Musique", font=("Helvetica", 14), fg="white").pack()
    ListMu = ["Ninjago saison 5", "Geometry Dash"]
    varMu = StringVar(fenetre)
    varMu.set(ListMu[0])
    mu = OptionMenu(fenetre, varMu, *ListMu)
    mu.config(width=30, font=("Helvetica", 12))
    mu.pack(pady=10)



    #choix du mode de jeu
    Label(fenetre, text="Mode de jeu", font=("Helvetica", 14), fg="white").pack()
    ListMo = ["Solo", "Multijoueur"]
    varMo = StringVar(fenetre)
    varMo.set(ListMo[0])
    mo = OptionMenu(fenetre, varMo, *ListMo)
    mo.config(width=30, font=("Helvetica", 12))
    mo.pack(pady=10)

    varNB = IntVar(fenetre)

    #frame pour IA ou joueurs (permet de les afficher/supprimer facilement)
    frame_options = Frame(fenetre)
    frame_options.pack()

    #Fonction pour afficher dynamiquement l'option correcte
    def update_options(*args):
        #Supprime les widgets actuels dans frame_options
        for widget in frame_options.winfo_children():
            widget.destroy()

        if varMo.get() == "Solo":
            Label(frame_options, text="Nombre d'IA", font=("Helvetica", 14), fg="white").pack()
            ListIA = ["0","1", "2", "3", "4", "5"]
            varNB.set(ListIA[0])
            ia = OptionMenu(frame_options, varNB, *ListIA)
            ia.config(width=30, font=("Helvetica", 12))
            ia.pack(pady=10)
        else:
            #renvoie du nombre de joueurs
            Label(frame_options, text="Nombre de joueurs", font=("Helvetica", 14), fg="white").pack()
            ListJp = ["2", "3"]
            varNB.set(ListJp[0])
            jp = OptionMenu(frame_options, varNB, *ListJp)
            jp.config(width=30, font=("Helvetica", 12))
            jp.pack(pady=10)


    #Choix de la vitesse
    Label(fenetre, text="Vitesse du snake", font=("Helvetica", 14), fg="white").pack()
    varSpeed = IntVar(fenetre)
    Scala2 = Scale(fenetre, from_=1, to=8, length = 250,tickinterval = 1, orient=HORIZONTAL, sliderlength = 15, variable=varSpeed)
    Scala2.pack(padx=5)

    #Bouton de lancement
    def lancer():
        fenetre.destroy()
    start=Button(fenetre,text="Lancer le Jeu",font=("Helvetica", 14),command=lancer)
    start.pack(padx=0, pady=40)


    closing=[False]
    #Bouton de fermeture
    def fermer():
        closing[0]=[True]
        fenetre.destroy()

    close=Button(fenetre,text="Quitter le Jeu",font=("Helvetica", 14),command=fermer)
    close.pack(padx=0, pady=0)


    #Lier la fonction à tout changement de mode de jeu
    nombre = varMo.trace("w", update_options)
    update_options()

    #Lancement de la fenêtre
    fenetre.mainloop()

    if not closing[0] :
        return varCar.get(), varMu.get(), varMo.get(), varNB.get(), varSpeed.get()






def end(number_size):
    name=["Alain Berro","Laurent Marsan","Bénédicte Alziary"]
    #création de la fenêtre principale
    finish = Tk()
    finish.title("Snake Project")
    # fenetre.iconbitmap("grand_devoreur.ico")
    finish.config()
    finish.geometry("800x600")

    #titre du jeu
    titre = Label(finish, text="* Jeu Perdu *", font=("Helvetica", 60, "bold"), fg="red")
    titre.pack(pady=20)

    titre2 = Label(finish, text="Voici les scores :", font=("Helvetica", 30, "bold"), fg="green")
    titre2.pack(pady=5)

    result=[Label(finish, text=f"Le Snake {name[i]} est de taille {number_size[i]}", font=("Helvetica", 14), fg="white") for i in range(len(number_size))]
    for i in range(len(number_size)):
        result[i].pack(pady=10)

    varJeu=[0]

    def finit(value):
        varJeu[0]=value
        finish.destroy()
    
    #Bouton pour recommencer
    Button(finish, text='Relancer le jeu',command=lambda *args: finit(True)).pack(pady=50)

    #Bouton pour finir le jeu 
    Button(finish, text='Finir le jeu',command=lambda *args: finit(False)).pack(pady=50)

    finish.mainloop()

    return varJeu[0]

# print(menu())
# print(end([5,6]))
