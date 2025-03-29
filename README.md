	# Snake Project
Project L1 Snake

Dans le cadre du projet de fin de semestre de la matière Algorithmique 2 de la double licence Économie-Miashs de TSE, enseignée par Laurent Marsan, nous avons du recréer un jeu snake amélioré, comprenant par exemple des murs et des bonus...

## Fichiers 
Ce jeu est composé de 3 fichiers : 
+ `Project_Snake.py`
  - Projet principal comprenant la partie code du jeu 
+ `menu.py`
  - Code permettant d'afficher des interfaces graphiques
+ `tkiteasy.py`
  - Utilisation de la base [tkiteasy](https://github.com/LaurentMarsan/tkiteasy) produite par [@LaurentMarsan](https://github.com/LaurentMarsan/)
  - Modification multiples (voir section dédiée).

## Identification :
Dans ce jeu graphique, les éléments ont 2 types d'identité :

    • L'identité par coordonnées :
        Snake, bonus, murs, peuvent tous être identifiés par leurs coordonnées dans un plan
        -> mur dans un set pour facilité la recherche rapide
        Ceci permet ainsi de confronter les coordonnées de murs et des snake / de bonus et des snake

    • L'identité par objet graphique :
        En utilisant des objets graphiques, on peut les déplacer, les supprimer voir les modifier 
        C'est ici que nous utilisons tkiteasy






## Projet_Snake : 
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
	
    • méthode canMove(x,y) : 
    La méthode canMove(self, x, y) vérifie si le serpent peut se déplacer vers la position (x, y). Elle effectue les vérifications suivantes :
    => Si (x, y) se trouve dans un mur (plan.mur), le mouvement est impossible.
    => Si la position est occupée par un autre serpent ( Snake.allSnake[i]), le mouvement est également interdit.
    => Si les coordonnées sont en dehors des limites du plan, le serpent ne peut pas se déplacer.
    
    Si l'une de ces conditions est remplie, la méthode appelle self.supSnake() pour supprimer le serpent du jeu (si ce n'est pas une IA) et retourne False. Sinon, elle
    retourne True, autorisant le mouvement.

## Fonction game
La fonction game() gère le déroulement du jeu, en créant et en initialisant les éléments nécessaires à la partie, puis en exécutant une boucle de jeu jusqu'à ce que toutes les conditions de fin de partie soient remplies.

    • Initialisation des paramètres :
    La fonction commence par récupérer les paramètres du jeu, tels que la taille du plan (dim), le choix de la musique (song), le mode de jeu (mode), le nombre de
    joueurs (nbr), la vitesse du serpent (speed), et la présence d'une fonction bloquante (block) à partir du menu principal (menubeta.menu()).

    •  Mode de jeu Solo ou Multijoueur :
    En fonction du mode sélectionné, si le mode est "Solo", le nombre d'IA (ia) est défini comme le nombre de joueurs, et le nombre de joueurs (nbr) est réduit à 1. Si
    le mode est "Multijoueur", aucune IA n'est présente, et les joueurs sont ajoutés manuellement.

    • Création du plan de jeu :
    Un objet Plan est créé avec la dimension du terrain, et le titre et l'icône de la fenêtre sont définis à l'aide de la méthode icone_titre().

    • Création des serpents :
    Les serpents des joueurs (en nombre défini par nbr) et des IA (en nombre défini par ia) sont créés et stockés dans des listes respectives. Chaque serpent reçoit
    une vitesse et une taille initiale.

    • Musique de fond :
    La musique du jeu est lancée à l'aide de la méthode jouerMusique(), où le fichier de musique est sélectionné dynamiquement en fonction de la sélection dans le menu.

    • Boucle de jeu principale :
    La boucle while len(snake) != 0: gère l'évolution du jeu, où chaque serpent se déplace à chaque itération. Si un serpent meurt (sa position devient vide), il est
    retiré de la liste snake. Si des IA sont présentes, elles se déplacent également, et si une IA meurt, elle est retirée de la liste snakeIA. Le compteur vivarium
    assure que chaque serpent ou IA se déplace à chaque tour.

    • Fin de la partie :
    Lorsque tous les serpents sont morts, la musique est stoppé et le jeu se termine avec la fermeture de la fenêtre. Si la fonction menubeta.end() renvoie
    True, la fonction game() est appelée à nouveau pour relancer une nouvelle partie.


## Menus
Nous avons créé deux menus.

    • Le premier menu est lancé dès le début du jeu. Il permet de sélectionner certains paramètres et de lancer la partie. A la fin de la partie, un second menu de fin
    s'affiche. Il permet de relancer une partie en retournant au menu. De la musique est présente dans le menu de d'accueil et le menu de fin.
    Ces deux menus sont construits à l'aide de Tkinter afin d'avoir plus de libertés qu'avec Tkiteasy, nottament avec des boutons interractifs par exemple.
    • Le menu d'accueil est également interactif, avec des choix dynamiques qui s'ajustent en fonction des options sélectionnées. Par exemple, en mode "Solo", un
    bouton de sélection du nombre d'IA apparaît, et en mode "Multijoueur", l'option de nombre de joueurs est disponible.
    • Le menu de début offre également la possibilité de choisir la musique que l'on met pendant la partie.
    • Le menu de fin affiche la taille de chaques serpents permettant de voir les scores.

Pour plus d'information, on peut consulter la [documentation de Tkinter](https://docs.python.org/3/library/tkinter.html)

## Modification Tkiteasy :
Nous avons modifié Tkiteasy afin de faire le projet.
Ci dessous, vous retrouverez des explications quant à ces modifications.

    • Ajout de la musique et du son (lignes 213 à 242) :
    Nous avons ajoutée de nouvelles métdodes à l'aide de Pygame. Nous créons une méthode qui appelle elle même une fonction de Pygame.Plus précisément, nous utilisons
    le mixer de Pygame. Le mixer de Pygame est un module permettant de gérer le son et la musique, incluant la lecture, le mixage et le contrôle du volume des fichiers
    audio. Ci dessous, nous faisons une liste des méthodes que nous avons créés.
    jouerMusique(musique,boucles,depart,fade) : cette méthode permet d'initialiser le mixer, de charger la musique et de la jouer
        Paramètres :
        => musique : la musique qu'on rentre, attention, quand on appelle cette fonction il faut penser à ajouter le type du fichier.
        => boucles : définit le nombre de fois que la musique doit être répétée. -1 correspond à une lecture infini.
        => depart : temps (en secondes) à partir duquel la musique commence.
        => fade : durée du fondu d’entrée en millisecondes (transition progressive du silence au volume normal).
    rejouerMusique : permet de rejouer la musique
    stopMusique : permet de stopper la musique
    pauseMusique : met en pause la musique
    unpauseMusique : désactive la pause de la musique
    jouerSon(son, boucles, maxtime, fade) : On utilise pygame.mixer.Sound pour jouer des effets sonores courts de manière rapide et simultanée, sans interrompre 
    la musique de fond.
        Paramètres :
        => son : le son que l'on beut jouer
        => boucles : nombre de répétitions du son.
        => maxtime : temps maximal de lecture en millisecondes
        => fade : durée du fondu d’entrée en millisecondes.

  Pour plus d'information, on peut consulter la [documentation de pygame](https://www.pygame.org/docs/ref/mixer.html)
    
    • Ajout d'une icone et d'un titre pour la fenêtre (lignes 257 à 259) :
    icone_titre(icone,titre) : méthode qui permet de mettre une icone et un titre à la fenêtre de jeu
        Paramètres :
        => icone : fichier de l'image que l'on veut mettre (en format .ico)
        => titre : le titre de la fenêtre

    
    
    


        
