## Snake_V1 - 07/03

from tkiteasy import *
import random 



#création de la classe du snake
class Snake():
    #Compteur de serpent pour utiliser différentes touches 
    nbr=-1

    # Associations de touches pour pouvoir jouer 
    # Haut, Bas, Gauche, Droite
    key=[["Up","Down","Left","Right"],
         ["z","s","q","d"],
         ["t","g","f","h"]]


    #Liste avec toutes les positions des snake généralisée à la classe entière 
    #-> Utilisation pour un jeu en multijoueur 
    allSnake=[]



    def __init__(self,speed=5,size=1):
            
            #On ajoute 1 au nombre de snake et on définit le numéro self du snake 
            Snake.nbr+=1
            self.nbr_snake=Snake.nbr
            Snake.allSnake.append([])
            
            #Pour l'instant on joue au maximum avec 3 snake 
            if Snake.nbr>2:
                return False

            #Partie données de position
            self.size=size
            #Transformation pour renvoyer un résultat en milisecondes qui décroit quand speed augmente
            self.speed=0.03+0.1-(speed/100)
            
            Sx=random.randint(0,plan.dim-1)
            Sy=random.randint(0,plan.dim-1)
            for i in range(size):
                while (Sx+i,Sy) in plan.mur :
                    Sx=random.randint(0,plan.dim-1)
                    Sy=random.randint(0,plan.dim-1)

            #Coordonnées du snake
            self.Spos=[[Sx+i,Sy] for i in range(size)]

            #Partie graphique avec le plan
            self.objet=[plan.g.dessinerRectangle(self.Spos[i][0]*plan.px+1,
                                                self.Spos[i][1]*plan.px+1,
                                                plan.px-1,plan.px-1,"red") for i in range(len(self.Spos))]

            #Variable de touche pressée utilisée pour la fonction déplacer
            self.jeu=None

            


### Fonction renvoie si le joueur peut se déplacer avec x,y les coordonnées du déplacement  -->(Booléen autorisant le déplacement)
    def canMove(self,x,y):
        if (x,y) in plan.mur  :
            return False
        for i in range(Snake.nbr+1):
            if [x,y] in Snake.allSnake[i] :
                return False
        if x<0 or x>plan.dim-1:
            return False
        if y<0 or y>plan.dim-1:
            return False
        return True


### Fonction qui ajoute les bonus -->(Un Booléen pour savoir si on est sur un bonus ou non)
    def isBonus(self):
        if [self.Spos[-1][0],self.Spos[-1][1]] in plan.posB:

            #On lance le programme pour générer un nouveau point
            plan.moveBonus(self.Spos[-1][0],self.Spos[-1][1])
            return True
        return False


 ######### Déplacer le joueur à l'aide des flèches du clavier ##############               
    def deplaceSnake(self):
        g=plan.g       
        #Permet de mettre de la vitesse dans le snake
        plan.g.pause(self.speed)

        Snake.allSnake[self.nbr_snake]=self.Spos

        key=g.recupererTouche()
        #on récupère la touche et on regarde si elle est dans notre liste
        if key in Snake.key[self.nbr_snake]:
            self.jeu=key
        #self.jeu est la touche cliquée pour le snake en question

        #haut en position 0 dans Snake.key
        if self.jeu==Snake.key[self.nbr_snake][0] and self.canMove(self.Spos[-1][0],self.Spos[-1][1]-1):
            
            
            #On rajoute la nouvelle tête en coordonnées
            self.Spos.append([self.Spos[-1][0],self.Spos[-1][1]-1])


            # Snake.allSnake[self.nbr_snake].append([self.Spos[-1][0],self.Spos[-1][1]-1])
            #On dessine la nouvelle tête
            self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,
                                                       self.Spos[-1][1]*plan.px+1,
                                                       plan.px-1,plan.px-1,"red"))
            

            #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandit

            if not self.isBonus():
                #On supprime l'objet
                g.supprimer(self.objet[0])
                self.objet=self.objet[1:]

                #On supprime les coordonnées
                self.Spos=self.Spos[1:]


                # Snake.allSnake[self.nbr_snake].remove([self.Spos[-1][0],self.Spos[-1][1]-1])
            # break
            
        #bas
        elif self.jeu==Snake.key[self.nbr_snake][1] and self.canMove(self.Spos[-1][0],self.Spos[-1][1]+1):
            
            
            #On rajoute la nouvelle tête en coordonnées
            self.Spos.append([self.Spos[-1][0],self.Spos[-1][1]+1])

            #On dessine la nouvelle tête
            self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,
                                                       self.Spos[-1][1]*plan.px+1,
                                                       plan.px-1,plan.px-1,"red"))
            

            #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
            if not self.isBonus():
                #On supprime l'objet
                g.supprimer(self.objet[0])
                self.objet=self.objet[1:]

                #On supprime les coordonnées
                self.Spos=self.Spos[1:]
            
            
            # break
            
        #gauche
        elif self.jeu==Snake.key[self.nbr_snake][2] and self.canMove(self.Spos[-1][0]-1,self.Spos[-1][1]):
            
        
            #On rajoute la nouvelle tête en coordonnées
            self.Spos.append([self.Spos[-1][0]-1,self.Spos[-1][1]])

            #On dessine la nouvelle tête
            self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,
                                                       self.Spos[-1][1]*plan.px+1,plan.px-1,
                                                       plan.px-1,"red"))
            

            #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
            if not self.isBonus():
                #On supprime l'objet
                g.supprimer(self.objet[0])
                self.objet=self.objet[1:]

                #On supprime les coordonnées
                self.Spos=self.Spos[1:]
            
            # break
            
        #droite
        elif self.jeu==Snake.key[self.nbr_snake][3] and self.canMove(self.Spos[-1][0]+1,self.Spos[-1][1]):
            
            
            #On rajoute la nouvelle tête en coordonnées
            self.Spos.append([self.Spos[-1][0]+1,self.Spos[-1][1]])

            #On dessine la nouvelle tête
            self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,
                                                       self.Spos[-1][1]*plan.px+1,
                                                       plan.px-1,plan.px-1,"red"))
            
            #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
            if not self.isBonus():
                #On supprime l'objet
                g.supprimer(self.objet[0])
                self.objet=self.objet[1:]

                #On supprime les coordonnées
                self.Spos=self.Spos[1:]
            
            # break

        # print(Snake.allSnake)





























#Classe Jeu du mosntre : 
class Plan():
    def __init__(self,dim):
        self.px=750/dim
        self.dim=dim
        

        self.g=ouvrirFenetre(self.px*self.dim,self.px*self.dim)
        self.initGraphique()

        #Liste de toutes les positions des murs
        self.wall(self.dim//3)

        self.initBonus()

    # Procédure qui dessine le plan avec les lignes
    def initGraphique(self):

        for i in range(self.dim):
            self.g.dessinerLigne(i*self.px,0,i*self.px,self.px*self.dim,"grey")
            self.g.dessinerLigne(0,i*self.px,self.px*self.dim,i*self.px,"grey")


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
            bonus=self.g.dessinerRectangle(self.px*item[0]+1,
                                           self.px*item[1]+1,
                                           self.px-1,self.px-1,"yellow")
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
        self.objBonus.append(self.g.dessinerRectangle(x*self.px+1,y*self.px+1,
                                                    self.px-1,self.px-1,"yellow"))

        





#Possibilité de jouer avec plusieurs joueurs
plan=Plan(30)
snake=Snake(4,2)
snake2=Snake(7,3)
while True:
    snake.deplaceSnake()
    snake2.deplaceSnake()
plan.g.attendreClic()

