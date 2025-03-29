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

    • Ajout de la musique (lignes 213 à 242) :
    Nous avons ajoutée de nouvelles métdodes à l'aide de Pygame. Nous créons une méthode qui appelle elle même une fonction de Pygame.Plus précisément, nous utilisons
    le mixer de Pygame. Le mixer de Pygame est un module permettant de gérer le son et la musique, incluant la lecture, le mixage et le contrôle du volume des fichiers
    audio. Ci dessous, nous faisons une liste des méthodes que nous avons créés.
    jouerMusique(musique,boucles,depart,fade) : cette méthode permet d'initialiser le mixer, de charger la musique et de la jouer
    Paramètres :
    => musique : la musique qu'on rentre, attention, quand on appelle cette fonction il faut penser à ajouter le type du fichier.
    => boucles : définit le nombre de fois que la musique doit être répétée.
    => depart : temps (en secondes) à partir duquel la musique commence.
    => fade : durée du fondu d’entrée en millisecondes (transition progressive du silence au volume normal).
    rejouerMusique : permet de rejouer la musique
    stopMusique : permet de stopper la musique
    pauseMusique : met en pause la musique
    unpauseMusique : désactive la pause de la musique
    

    
    Pour plus d'information, on peut consulter la documentation de pygame :
    https://www.pygame.org/docs/ref/music.html
    
    


        
