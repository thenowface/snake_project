## Snake_V1 - 07/03

from tkiteasy import *
import random 
import menu




################################################################################
# CLASSE DU SNAKE
################################################################################
class Snake():
    # Compteur de nombre de snake générés
    # Comprends aussi les IA
    nbr=-1

    # Associations de touches pour pouvoir jouer 
    # Haut, Bas, Gauche, Droite
    key=[["Up","Down","Left","Right"],
         ["z","s","q","d"],
         ["t","g","f","h"]]


    # Liste avec toutes les positions des snake généralisée à la classe entière 
    # -> Utilisation pour un jeu en multijoueur 
    allSnake=[]


    #Images des têtes de snake
    headSnake=["alain.png","laurent.png","benedicte.jpg"]

    jeu=[]


    def __init__(self,speed=5,size=1,isIA=False):
            
            # Est-ce que le serpent est une IA
            self.isIA=isIA

            # On ajoute 1 au nombre de snake et on définit le numéro self du snake 
            Snake.nbr+=1
            self.nbr_snake=Snake.nbr
            Snake.allSnake.append([])
            
            # Pour l'instant on joue au maximum avec 3 snake en multijoueur 
            # Poss.
            if Snake.nbr>2:
                return False

            #Partie données de position
            self.size=size
            #Transformation pour renvoyer un résultat en milisecondes qui décroit quand speed augmente
            self.speed=0.03+0.1-(speed/100)

            #Couleur vert pour serpent rouge pour IA
            if isIA :
                self.color="red"
            else:
                self.color="green"
            
            Sx=random.randint(size-1,plan.dim-size)
            Sy=random.randint(size-1,plan.dim-size)
            for i in range(size):
                while (Sx+i,Sy) in plan.mur:
                    Sx=random.randint(size-1,plan.dim-size)
                    Sy=random.randint(size-1,plan.dim-size)

            #Coordonnées du snake
            self.Spos=[[Sx+i,Sy] for i in range(size)]

            #Partie graphique avec le plan
            self.objet=[plan.g.dessinerRectangle(self.Spos[i][0]*plan.px+1,
                                                self.Spos[i][1]*plan.px+1,
                                                plan.px-1,plan.px-1,self.color) for i in range(len(self.Spos))]

            #Variable de touche pressée utilisée pour la fonction déplacer
            Snake.jeu.append(None)

            #Liste qui comprend si la vitesse est modifiée et depuis combien de déplacements
            self.isSpeed=[None,0]

            self.face=[None,None]
            


### Fonction renvoie si le joueur peut se déplacer avec x,y les coordonnées du déplacement  -->(Booléen autorisant le déplacement)
    def canMove(self,x,y):
        if (x,y) in plan.mur  :
            if self.jeu!=None and not self.isIA:
                self.supSnake()
            return False
        for i in range(Snake.nbr+1):
            if [x,y] in Snake.allSnake[i] :
                if self.jeu!=None and not self.isIA:
                    self.supSnake()
                return False
        if x<0 or x>plan.dim-1:
            if self.jeu!=None and not self.isIA:
                self.supSnake()
            return False
        if y<0 or y>plan.dim-1:
            if self.jeu!=None and not self.isIA:
                self.supSnake()
            return False
        return True


### Fonction qui ajoute les bonus -->(Un Booléen pour savoir si on est sur un bonus ou non)
    def isBonus(self):

        #Regarde si la vitesse est modifiée 
        if self.isSpeed[0]==-1:
            #Rajoute un déplacement de vitesse
            self.isSpeed[1]+=1
            #Si on atteint 100 déplacement
            if self.isSpeed[1]>100:
                self.speed+=self.isSpeed[0]*0.02
                self.isSpeed=[None,0]

        if [self.Spos[-1][0],self.Spos[-1][1]] in plan.posB:

            #On lance le programme pour générer un nouveau point
            plan.moveBonus(self.Spos[-1][0],self.Spos[-1][1])

            #On augmente la taille du serpent
            self.size+=1
        
            #Ajout des accelerateurs et les ralentisseurs
            #Accelerateur
            if self.size%2==0: 
                plan.initSPoint(2)
            #Ralentisseur
            if self.size%8==0:
                plan.initSPoint(1)

            

            return True
        
        # Si le snake passe sur un accélérateur on diminue le temps d'attente
        elif [self.Spos[-1][0],self.Spos[-1][1]] in plan.pos2:
            plan.moveSPoint(self.Spos[-1][0],self.Spos[-1][1],2)
            #Sécurité pour eviter un sleeptime négatif
            if self.speed-0.02>=0:
                self.speed-=0.02

            #On rentre le compteur de vitesse -> -1 car pour remettre normalement 
            # on augmente le temps d'attente
            self.isSpeed[0]=1
            return False
        
        # Si le snake passe sur un ralentisseur on augmente le temps d'attente
        elif [self.Spos[-1][0],self.Spos[-1][1]] in plan.pos1:
            plan.moveSPoint(self.Spos[-1][0],self.Spos[-1][1],1)
            self.speed+=0.03

            #On rentre le compteur de vitesse -> -1 car pour remettre normalement 
            # on diminue le temps d'attente
            self.isSpeed[0]=-1
            return False

        return False
    

    #Fonction qui renvoie le bonus le plus proche sx,sy position de la tete du snake bx,by position des bonus
    def closestBonus(self,sx,sy):
        #Coordonnées du bonus le plus proche
        x,y=plan.posB[0]
        dist=abs(x-sx)+abs(y-sy)
        
        # Recherche du point le plus proche 
        for bx,by in plan.posB:
            if (abs(bx-sx)+abs(by-sy))<dist:
                x=bx
                y=by

        return x,y


    #Procédure qui crée le mouvement à faire
    def moveIA(self,sx,sy):
        bx,by=self.closestBonus(sx,sy)

        #Déplacement par rapport au bonus
        depx,depy=bx-sx,by-sy

        

        #Si la distance en y est plus grande on la réduit et on regarde si le snake n'est pas sur le joueur
        if  abs(depy)>= abs(depx) and (depx,depy)!=(0,0):

            #Si il faut monter
            if depy<0 and self.canMove(sx,sy-1) :
                Snake.jeu[self.nbr_snake]=Snake.key[self.nbr_snake][0]
            
            #Sinon on descend 
            elif depy>=0 and self.canMove(sx,sy+1):
                Snake.jeu[self.nbr_snake]=Snake.key[self.nbr_snake][1]

            #Gauche
            elif self.canMove(sx-1,sy):
                Snake.jeu[self.nbr_snake]=Snake.key[self.nbr_snake][2]

            #Aléatoire
            else:
                Snake.jeu[self.nbr_snake]=Snake.key[self.nbr_snake][random.randint(0,3)]
               
        
        #Si la distance en x est plus grande on la réduit
        elif abs(depy)< abs(depx) and (depx,depy)!=(0,0):
            #Gauche
            if depx<0 and self.canMove(sx-1,sy):
                Snake.jeu[self.nbr_snake]=Snake.key[self.nbr_snake][2]
            #Droite
            elif depx >=0 and self.canMove(sx+1,sy):
                Snake.jeu[self.nbr_snake]=Snake.key[self.nbr_snake][3]

            #Haut
            elif self.canMove(sx,sy-1):
                Snake.jeu[self.nbr_snake]=Snake.key[self.nbr_snake][0]

            #Aléatoire
            else:
                Snake.jeu[self.nbr_snake]=Snake.key[self.nbr_snake][random.randint(0,3)]


        # Si le snake est bloqué on le supprime
        if not True in [self.canMove(sx,sy-1),self.canMove(sx,sy+1),self.canMove(sx-1,sy),self.canMove(sx+1,sy)]:
            Snake.jeu[self.nbr_snake]=None
            self.supSnake()










 
 ######### Déplacer le joueur à l'aide des flèches du clavier ##############       
 
    def deplaceSnake(self,type):
        g=plan.g       
        #Permet de mettre de la vitesse dans le snake
        plan.g.pause(self.speed)

        # Actualisation de la variable de classe de toutes les positions
        Snake.allSnake[self.nbr_snake]=self.Spos

        if not self.isIA:
            # Type 1 pour la fonction bloquante
            if type==1:
                key=g.attendreTouche()
            else:
                key=g.recupererTouche()

            
            #on récupère la touche et on regarde si elle est dans notre liste
            # Type 1 pour la fonction blocante
            if type==1:
                Snake.jeu[self.nbr_snake]=key

            else:
                for i in range(Snake.nbr+1):
                    if key in Snake.key[i]:
                        Snake.jeu[i]=key
            #self.jeu est la touche cliquée pour le snake en question
        else: 
            self.moveIA(self.Spos[-1][0],self.Spos[-1][1])
 


        #haut en position 0 dans Snake.key
        if Snake.jeu[self.nbr_snake]==Snake.key[self.nbr_snake][0] and self.canMove(self.Spos[-1][0],self.Spos[-1][1]-1):
            
            
            #On rajoute la nouvelle tête en coordonnées
            self.Spos.append([self.Spos[-1][0],self.Spos[-1][1]-1])


            # Snake.allSnake[self.nbr_snake].append([self.Spos[-1][0],self.Spos[-1][1]-1])
            #On dessine la nouvelle tête
            self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,
                                                       self.Spos[-1][1]*plan.px+1,
                                                       plan.px-1,plan.px-1,self.color))
            

            #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandit

            if not self.isBonus():
                #On supprime l'objet
                g.supprimer(self.objet[0])
                self.objet=self.objet[1:]

                #On supprime les coordonnées
                self.Spos=self.Spos[1:]


                # Snake.allSnake[self.nbr_snake].remove([self.Spos[-1][0],self.Spos[-1][1]-1])
            
        #bas
        elif Snake.jeu[self.nbr_snake]==Snake.key[self.nbr_snake][1] and self.canMove(self.Spos[-1][0],self.Spos[-1][1]+1):
            
            
            #On rajoute la nouvelle tête en coordonnées
            self.Spos.append([self.Spos[-1][0],self.Spos[-1][1]+1])

            #On dessine la nouvelle tête
            self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,
                                                       self.Spos[-1][1]*plan.px+1,
                                                       plan.px-1,plan.px-1,self.color))
            

            #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
            if not self.isBonus():
                #On supprime l'objet
                g.supprimer(self.objet[0])
                self.objet=self.objet[1:]

                #On supprime les coordonnées
                self.Spos=self.Spos[1:]
            
        
            
        #gauche
        elif Snake.jeu[self.nbr_snake]==Snake.key[self.nbr_snake][2] and self.canMove(self.Spos[-1][0]-1,self.Spos[-1][1]):
            
        
            #On rajoute la nouvelle tête en coordonnées
            self.Spos.append([self.Spos[-1][0]-1,self.Spos[-1][1]])

            #On dessine la nouvelle tête
            self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,
                                                       self.Spos[-1][1]*plan.px+1,plan.px-1,
                                                       plan.px-1,self.color))
            

            #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
            if not self.isBonus():
                #On supprime l'objet
                g.supprimer(self.objet[0])
                self.objet=self.objet[1:]

                #On supprime les coordonnées
                self.Spos=self.Spos[1:]
            
         
            
        #droite
        elif Snake.jeu[self.nbr_snake]==Snake.key[self.nbr_snake][3] and self.canMove(self.Spos[-1][0]+1,self.Spos[-1][1]):
            
            
            #On rajoute la nouvelle tête en coordonnées
            self.Spos.append([self.Spos[-1][0]+1,self.Spos[-1][1]])

            #On dessine la nouvelle tête
            self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,
                                                       self.Spos[-1][1]*plan.px+1,
                                                       plan.px-1,plan.px-1,self.color))
            
            #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
            if not self.isBonus():
                #On supprime l'objet
                g.supprimer(self.objet[0])
                self.objet=self.objet[1:]

                #On supprime les coordonnées
                self.Spos=self.Spos[1:]
      
        # Enlève l'ancienne tête
        if self.face!=[None,None]:
            plan.g.supprimer(self.face[0])
            plan.g.supprimer(self.face[1])

        #Programme qui affiche la tête du serpent 
        if self.Spos!=[]:
            self.face=[plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,self.Spos[-1][1]*plan.px+1,plan.px-1,plan.px-1,"black"),
                    plan.g.afficherImage(self.Spos[-1][0]*plan.px,self.Spos[-1][1]*plan.px,"pics/"+Snake.headSnake[self.nbr_snake],int(plan.px),int(plan.px))]









    #Procédure qui supprime le snake de manière élégante
    def supSnake(self):
        plan.g.pause(0.12)
        plan.g.supprimer(self.face[0])
        plan.g.supprimer(self.face[1])
        self.face=[None,None]
        for i in range(self.size,0,-1):
            plan.g.supprimer(self.objet[i-1])
            plan.g.actualiser()
            plan.g.pause(0.1)
        self.objet=[]
        self.Spos=[]




























################################################################################
# CLASSE DU PLAN
################################################################################ 
class Plan():
    def __init__(self,dim):

        # création des dimensions adéquates pour chaque cases en fonction du nombre de cases
        self.px=750/dim
        self.dim=dim
        

        self.g=ouvrirFenetre(self.px*self.dim,self.px*self.dim)

        #Liste de toutes les positions des murs
        self.wall(self.dim//3)

        self.initBonus()

        #Listes pour les accélérateurs --> notation avec un 2
        self.pos2=[]
        self.obj2=[]

        #Listes pour les ralentisseurs --> notation avec un 1
        self.pos1=[]
        self.obj1=[]

        #Liste avec les images pour les bonus
        self.imgB=[]

        #Initialisation du nombre de Snake
        Snake.nbr=-1
        Snake.allSnake=[]
        Snake.jeu=[]



    # Procédure qui déssine les bonus et qui ajoute leur coordonnées au données du plan
    def initBonus(self):
        #Liste de toutes les positions des bonus
        self.posB=[[random.randint(0,self.dim-1),random.randint(0,self.dim-1)] for i in range(self.dim//5)]

        #On vérifie que les coordonnées ne sont pas sur des murs
        for index in range(len(self.posB)):
            while (self.posB[index][0],self.posB[index][1])in self.mur:
                self.posB[index]=[random.randint(0,self.dim-1),random.randint(0,self.dim-1)]

        #On crée les objet graphiques associés aux coordonnées
        self.objBonus=[]
        for item in self.posB:
            bonus=self.g.afficherImage(item[0]*self.px,item[1]*self.px,"pics/apple_red.png",int(self.px),int(self.px))
            self.objBonus.append(bonus)

    

    # Procédure qui crée les murs de façon random <--(Nombre de murs à dessiner : n)
    def wall(self,n):
        self.mur=[]
        #n correspond au nombre de mur 
        for i in range(n):
            x=random.randint(0,self.dim-1)
            y=random.randint(0,self.dim-1)

            for j in range(self.dim//3):
                if j%3==0:
                    dep=random.choice([(0,1),(0,-1),(1,0),(-1,0)])

                while (x+dep[0],y+dep[1]) in self.mur or x+dep[0]>=self.dim or x+dep[0]<0 or y+dep[1]>=self.dim or y+dep[1]<0 :
                    dep=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
                x+=dep[0]
                y+=dep[1]

                self.g.dessinerRectangle(x*self.px,y*self.px,self.px,self.px,"grey")

                #On utilise un tuple pour les murs car ce sont des éléments non mutables
                self.mur.append((x,y))

        #Conversion en set pour optimiser le programme 
        self.mur=set(self.mur)



### Procédure qui supprime et replace les bonus <-- (position du point mangé + snake concernée) 
# -->   .pop() prends en paramètre un index et .remove() prends en paramètre un élément
    def moveBonus(self,x,y):

        #On supprime le point touché
        i=self.posB.index([x,y])

        #Supprime les coordonnées
        self.posB.pop(i)
        #Supprime l'objet
        self.g.supprimer(self.objBonus[i])
        self.objBonus.pop(i)


        # On concatene toutes les coordonnées de tous les snake 
        # pour générer un nv bonus
        snakeBonus=[]
        for i in range(Snake.nbr+1):
            snakeBonus+=Snake.allSnake[i]


        #On crée de nouvelles coordonnés
        while [x,y] in snakeBonus or [x,y] in self.posB or (x,y) in self.mur:
            x=random.randint(0,self.dim-1)
            y=random.randint(0,self.dim-1)

        #On ajoute les nouvelles coordonnées 
        self.posB.append([x,y])
        #On crée un nouvel objet graphique
        self.objBonus.append(self.g.afficherImage(x*self.px,y*self.px,"pics/apple_red.png",int(self.px),int(self.px)))

        
    ## Procédure qui initialise les points spéciaux
    def initSPoint(self,type):
        snakeBonus=[]
        for i in range(Snake.nbr+1):
            snakeBonus+=Snake.allSnake[i]
        x=random.randint(0,self.dim-1)
        y=random.randint(0,self.dim-1)
        while [x,y] in snakeBonus or [x,y] in self.posB or (x,y) in self.mur:
            x=random.randint(0,self.dim-1)
            y=random.randint(0,self.dim-1)

        #Accélérateur en pomme jaune
        if type==2:
            self.pos2.append([x,y])
            self.obj2.append(self.g.afficherImage(x*self.px,y*self.px,"pics/apple_yellow.png",int(self.px),int(self.px)))
        #Ralentisseur en pomme de terre empoisonnée 
        elif type==1:
            self.pos1.append([x,y])
            self.obj1.append(self.g.afficherImage(x*self.px,y*self.px,"pics/poison.png",int(self.px),int(self.px)))

        
        
    def moveSPoint(self,x,y,type):
        if type==2:
            #On supprime le point touché
            i=self.pos2.index([x,y])

            #Supprime les coordonnées
            self.pos2.pop(i)
            #Supprime l'objet
            self.g.supprimer(self.obj2[i])
            self.obj2.pop(i)

        elif type==1:
            #On supprime le point touché
            i=self.pos1.index([x,y])

            #Supprime les coordonnées
            self.pos1.pop(i)
            #Supprime l'objet
            self.g.supprimer(self.obj1[i])
            self.obj1.pop(i)


        
        
 








################################################################################
# FONCTION RÉCURSSIVE DE JEU
################################################################################ 
def game():

    # Exception sur cette variable globale pour utiliser le plan comme appui
    global plan
    
    # Récupération des données avec le menu
    dim,song,mode,nbr,speed,block=menu.menu()

    # ia est le nombre d'ia et nbr est le nombre de joueur solo
    if mode=="Solo":
        ia=nbr
        nbr=1
    else:
        ia=0


    # On crée sur plan sur lequel on va jouer 
    plan=Plan(dim)


    # cette méthode permet d'afficher l'icone et le titre de la fenêtre
    plan.g.icone_titre("pics/grand_devoreur.ico","Snake")


    # Création des listes d'ia et de snake
    snake=[Snake(speed,size=3) for _ in range(nbr)]
    snakeIA=[Snake(speed,isIA=True) for _ in range(ia)]


    # Liste avec les tailles de snake
    number_size=[1 for _ in range(nbr)]


    #Compteur pour passer par tous les snakes
    vivarium=0

    # on appelle la fonction pour mettre de la musique
    # on rajoute .ogg afin que le fichier soit lu.
    plan.g.jouerMusique("songs/"+ song + ".ogg",0,0,0)  


    while len(snake)!=0:


        #itération d'IA
        if ia!=0:
            num_IA=vivarium%len(snakeIA)

            snakeIA[num_IA].deplaceSnake(block)

            if snakeIA[num_IA].Spos==[]:
                snakeIA.pop(num_IA)
                ia-=1


        #itération de snake
        num_ID=vivarium%len(snake)

        snake[num_ID].deplaceSnake(block)

        if snake[num_ID].Spos==[]:

            # print("\n snake mort")
            # print(f"\nvivarium : {vivarium},len : {len(snake)}")
            # print(f"\nLe snake {vivarium%len(snake)} -> --> {snake[vivarium%len(snake)].size}")

            number_size[snake[num_ID].nbr_snake]=snake[num_ID].size
            snake.pop(num_ID)
       
        
        vivarium+=1
    
    # Musique de game over
    menu.music_over()

    plan.g.pause(1.2)
    
    plan.g.stopMusique()
    plan.g.fermerFenetre()

    #Remise à zéro de la fenetre tkiteasy
    Canevas.racine=None

    # Si on reçois l'indication de rejouer on lance la récussivité
    if menu.end(number_size):
       game()


game()


