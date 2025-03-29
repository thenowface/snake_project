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
  - Modification multiples. 



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

### Classe Snake:
Le snake est une liste de dimension n+1\
L'élément 0 est la queue du serpent -> position `[0]`\
L'élément n est la tête du serpent -> position `[-1]`\

La classe Snake détient plusieurs variables de classe permettant de généraliser des informations\
Généralisation :Toutes les positons de serpent, touches pressées, touches pressables...\


+ Génération du snake `__init__()`:
  - Point aléatoire et on ajoute `size` carrés derrière (avec vérification de ne pas être dans les mur[^1])
  - Création des objets graphiques stockés dans la liste `self.objet`


+ Fonction de possibilité de déplacement `canMove()`:
  - Reçoit un déplacement
  - Regarde si ce n'est pas dans un mur, dans un snake, ou en dehors des dimensions
  - Renvoie un booléen d'acceptation du déplacement
  - Si pas une IA renvoie à la suppression du serpent
 
+ Fonction de détection du bonus `isBonus()`:
  - Prends la position de la tête
  - Regarde si la tête est sur un bonus :
    - Renvoie à la fonction de création d'un nouveau bonus
    - Renvoie un booléen `True` pour signifier le bonus
    - Initialise les pions spéciaux
  - Regarde si la tête est sur un pion spécial :
    - Affecte la vitesse en conséquence
    - Renvoie un booléen `False` pour signifier rien

+ Fonction de recherche de bonus `closestBonus()`:
  - Reçoit une position de tête
  - Recherche le bonus le plus proche 
  - Renvoie la position du bonus le plus proche
 
+ Procédure de déplacement IA `moveIA()`:
  - Reçoit une position
  - Cherche le bonus le plus proche avec `closestBonus()`
  - Calcule la distance la plus longue entre abscisses et ordonnées pour la réduire
  - Affecte le déplacement adéquat ou un déplacement aléatoire si nécéssaire au déplacement à effectuer
  - Si serpent bloqué -> Mort 

+ Procédure de déplacement d'un Snake `deplaceSnake()`:
  - Reçoit le type de déplacement (bloquant/continu)
  - Récupère le déplacement à faire (IA ou Touche) 
  - Regarde si le déplacement est possible avec `canMove()`
  - Actualise les listes de positions et d'objets
  - Retire la queue et ajoute une nouvelle tête

 
+ Procédure de suppresion d'un Snake `supSnake()`:
  - Supprime carré par carré pour donner un effet visuel
  - Remet vide les listes de positions et d'objets




### Classe Plan:

La classe Plan permet de créer une structure sur laquelle joueur et est appelée dans la fonction `game()`\


+ Initiatlisation du plan `__init__()`:
  - Initialisation des variables de la classe `Snake()` pour pouvoir jouer
  - Initialisation des listes objets/positions pour tous les types de bonus
  - Ouverture d'une fenetre avec `tkiteasy` 

 
+ Procédure d'affichage des murs `wall()`:
  - Prends un point aléatoire
  - Choisis un nombre de déplacement aléatoire
  - Choisis une direction aléatoire et crée des paterns de murs
  - Actulise la liste position et la transforme en set pour la rapidité de recherche

 
+ Procédure d'affichage des bonus `initBonus()`:
  - Crée des positions au hasard
  - Vérifie qu'ils ne sont pas dans un mur
  - Crée des objets graphiques sur ces positions
 
 
+ Procédure de nouveau bonus `moveBonus()`:
  - Reçoit les coordonnées du bonus mangé
  - Supprime graphiquement et intérieurement le bonus
  - En crée un autre
 
 
+ Procédure d'ajout de points spéciaux `initSpoint()`:
  - Reçoit le type de point (Accélérateur/Ralentisseur)
  - Même procédure que `initBonus()` : on regarde si la case est dispo et on met un point

+ Procédure de nouveau point spécial `moveSpoint()`:
  - Reçoit les coordonnées et le type du point mangé
  - Supprime graphiquement et intérieurement le point






## Fonction game
La fonction `game()` gère le déroulement du jeu, en créant et en initialisant les éléments nécessaires à la partie, puis en exécutant une boucle de jeu jusqu'à ce que toutes les conditions de fin de partie soient remplies.

+ Initialisation des paramètres :

La fonction commence par récupérer les paramètres du jeu, tels que la taille du plan (`dim`), le choix de la musique (song), le mode de jeu (`mode`), le nombre de
joueurs (`nbr`), la vitesse du serpent (speed), et la présence d'une fonction bloquante (`block`) à partir du menu principal (`menu.menu()`).

+ Mode de jeu Solo ou Multijoueur :

En fonction du mode sélectionné, si le mode est `"Solo"`, le nombre d'IA (`ia`) est défini comme le nombre de joueurs, et le nombre de joueurs (`nbr`) est réduit à 1. Si
le mode est `"Multijoueur"`, aucune IA n'est présente, et les joueurs sont ajoutés manuellement.

+ Création du plan de jeu :

Un objet Plan est créé avec la dimension du terrain, et le titre et l'icône de la fenêtre sont définis à l'aide de la méthode `icone_titre()`.

+ Création des serpents :

Les serpents des joueurs (en nombre défini par nbr) et des IA (en nombre défini par ia) sont créés et stockés dans des listes respectives. Chaque serpent reçoit    une vitesse et une taille initiale.

+ Musique de fond :

La musique du jeu est lancée à l'aide de la méthode jouerMusique(), où le fichier de musique est sélectionné dynamiquement en fonction de la sélection dans le menu.

+ Boucle de jeu principale :

La boucle `while len(snake) != 0:` gère l'évolution du jeu, où chaque serpent se déplace à chaque itération. Si un serpent meurt (sa position devient vide), il est
retiré de la liste snake. Si des IA sont présentes, elles se déplacent également, et si une IA meurt, elle est retirée de la liste snakeIA. Le compteur `vivarium`
assure que chaque serpent ou IA se déplace à chaque tour.

+ Fin de la partie :

Lorsque tous les serpents sont morts, la musique est stoppé et le jeu se termine avec la fermeture de la fenêtre. Si la fonction `menu.end()` renvoie
True, la fonction `game()` est appelée à nouveau pour relancer une nouvelle partie.

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

+ Ajout de la musique et du son (lignes 213 à 242) :

Nous avons ajoutée de nouvelles métdodes à l'aide de Pygame. Nous créons une méthode qui appelle elle même une fonction de Pygame. 
Plus précisément, nous utilisons le mixer de Pygame. Le mixer de Pygame est un module permettant de gérer le son et la musique, incluant la lecture, le mixage et le contrôle du volume des fichiers
audio.
Ci dessous, nous faisons une liste des méthodes que nous avons créés.


`jouerMusique(musique,boucles,depart,fade)` : cette méthode permet d'initialiser le mixer, de charger la musique et de la jouer

  Paramètres :
  
- musique : la musique qu'on rentre, attention, quand on appelle cette fonction il faut penser à ajouter le type du fichier.
  
- boucles : définit le nombre de fois que la musique doit être répétée. -1 correspond à une lecture infini.
  
- depart : temps (en secondes) à partir duquel la musique commence.
  
- fade : durée du fondu d’entrée en millisecondes (transition progressive du silence au volume normal).


`rejouerMusique()` : permet de rejouer la musique


`stopMusique()` : permet de stopper la musique


`pauseMusique()` : met en pause la musique


`unpauseMusique()` : désactive la pause de la musique


`jouerSon(son, boucles, maxtime, fade)` : On utilise pygame.mixer.Sound pour jouer des effets sonores courts de manière rapide et simultanée, sans interrompre 
la musique de fond.

  Paramètres :
  
- son : le son que l'on beut jouer
  
- boucles : nombre de répétitions du son.
  
- maxtime : temps maximal de lecture en millisecondes
  
- fade : durée du fondu d’entrée en millisecondes.


Pour plus d'information, on peut consulter la [documentation de pygame](https://www.pygame.org/docs/ref/mixer.html)
    
+ Ajout d'une icone et d'un titre pour la fenêtre (lignes 257 à 259) :

`icone_titre(icone,titre)` : méthode qui permet de mettre une icone et un titre à la fenêtre de jeu
  
Paramètres :
  
- icone : fichier de l'image que l'on veut mettre (en format .ico)
  
- titre : le titre de la fenêtre

    
    
    


        
