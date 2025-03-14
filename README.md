# Snake Project
Project L1 Snake

## Identification :
Dans ce jeu graphique, les éléments ont 2 types d'identité :

    • L'identité par coordonnées :
        Snake, bonus, murs, peuvent tous être identifiés par leurs coordonnées dans un plan 
        Ceci permet ainsi de confronter les coordonnées de murs et du snake / de bonus et du snake

    • L'identité par objet graphique :
        En utilisant des objets graphiques, on peut les déplacer, les supprimer voir les modifier 
        C'est ici que nous utilisons tkiteasy




## Explication : 
Le snake est une liste de dimension n+1
L'élément 0 est la queue du serpent obtenu grâce à self.objet[0] à la position self.Spos[0] : [x,y]
L'élément n est la tête du serpent obtenu grâce à self.objet[-1] à la position self.Spos[-1] : [x,y]

Étapes pour faire avancer le serpent : 
    
    • Ajouter la nouvelle tête :
        - self.Spos.append([x,y]) --> Avec un certain déplacement au voisinnage par 4 avec la variable `dep`
        - self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0],self.Spos[-1][1],plan.px,plan.px,"red"))   
    
    --> Regarde si il n'y a pas de bonus 

    • Retirer la queue : 
        - self.Spos=self.Spos[1:]
        - self.objet=selft.objet[1:]
        - 

## Modification Tkiteasy :
Nous avons modifié Tkiteasy afin de faire le projet.
Ci dessous, vous retrouverez des explications quant à ces modifications.

    • Ajout de la musique (lignes 213 à 224) :
    Nous avons crée de nouvelles fonctions.
    chargerMusique : cette fonction initialise le mixer et charge le fichier audio qui est mis en paramètre. On utilise les fonctions de pygame mixer.init() et              mixer.music.load()
    jouerMusique : cette fonction permet de lancer la musique. On a trois paramètres. boucles, le nombre de fois qu'on rejoue la musique (0 on joue la musique une seule     fois); depart, à partir de quand on commence la musique (en secondes); fade,   
    On utilise la fonction mixer.music.play()
    Pour plus d'information, on peut consulter la documentation de py
    


        
