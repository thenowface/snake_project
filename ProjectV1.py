## Snake_V1 - 07/03

from tkiteasy import *
import random 



#création de la classe du snake
class Snake():
    #Compteur de serpent pour utiliser différentes touches 
    nbS=0
    def __init__(self,speed=5,size=1):
            #Partie données de position
            self.size=size
            #Transformation pour renvoyer un résultat en milisecondes qui décroit quand speed augmente
            self.speed=0.1-(speed/100)
            
            Sx=random.randint(0,plan.dim-1)
            Sy=random.randint(0,plan.dim-1)
            for i in range(size):
                while (Sx+i,Sy) in plan.mur :
                    Sx=random.randint(0,plan.dim-1)
                    Sy=random.randint(0,plan.dim-1)

            #Coordonnées du montre
            self.Spos=[[Sx+i,Sy] for i in range(size)]

            #Partie graphique avec le plan
            self.objet=[plan.g.dessinerRectangle(self.Spos[i][0]*plan.px+1,self.Spos[i][1]*plan.px+1,plan.px-1,plan.px-1,"red") for i in range(len(self.Spos))]
            


### Fonction qui renvoie si le joueur peut se déplacer avec x,y les coordonnées du déplacement
    def canMove(self,x,y):
        if (x,y) in plan.mur or [x,y] in self.Spos :
            return False
        if x<0 or x>plan.dim-1:
            return False
        if y<0 or y>plan.dim-1:
            return False
        return True


### Fonction qui ajoute les bonus 
    def isBonus(self):
        if [self.Spos[-1][0],self.Spos[-1][1]] in plan.posB:

            #On lance le programme pour générer un nouveau point
            plan.moveBonus(self.Spos[-1][0],self.Spos[-1][1],self)
            return True
        return False


 ######### Déplacer le joueur à l'aide des flèches du clavier ##############               
    def deplaceSnake(self):
        g=plan.g
        
        #Objets message d'erreur
        carre=None
        txt=None

        while True:
            g.pause(self.speed)
            #Suppression message d'erreur
            while carre!=None:
                suite=g.attendreTouche()
                if suite =="Return":
                    g.supprimer(carre)
                    g.supprimer(txt)
                    break

            
             
            jeu=g.recupererTouche()
            #jeu est la touche cliquée
            
            #haut
            if jeu=='Up' and self.canMove(self.Spos[-1][0],self.Spos[-1][1]-1):
                
                
                #On rajoute la nouvelle tête en coordonnées
                self.Spos.append([self.Spos[-1][0],self.Spos[-1][1]-1])
                #On dessine la nouvelle tête
                self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,self.Spos[-1][1]*plan.px+1,plan.px-1,plan.px-1,"red"))
                

                #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandit
                
                if not self.isBonus():
                    #On supprime l'objet
                    g.supprimer(self.objet[0])
                    self.objet=self.objet[1:]

                    #On supprime les coordonnées
                    self.Spos=self.Spos[1:]




                # break
                
            #bas
            elif jeu=='Down' and self.canMove(self.Spos[-1][0],self.Spos[-1][1]+1):
                
                
                #On rajoute la nouvelle tête en coordonnées
                self.Spos.append([self.Spos[-1][0],self.Spos[-1][1]+1])
                #On dessine la nouvelle tête
                self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,self.Spos[-1][1]*plan.px+1,plan.px-1,plan.px-1,"red"))
                

                #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
                if not self.isBonus():
                    #On supprime l'objet
                    g.supprimer(self.objet[0])
                    self.objet=self.objet[1:]

                    #On supprime les coordonnées
                    self.Spos=self.Spos[1:]
                
                
                # break
                
            #gauche
            elif jeu=='Left' and self.canMove(self.Spos[-1][0]-1,self.Spos[-1][1]):
                
                print(self.Spos)
                print(self.objet)
                #On rajoute la nouvelle tête en coordonnées
                self.Spos.append([self.Spos[-1][0]-1,self.Spos[-1][1]])
                #On dessine la nouvelle tête
                self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,self.Spos[-1][1]*plan.px+1,plan.px-1,plan.px-1,"red"))
                

                #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
                if not self.isBonus():
                    #On supprime l'objet
                    g.supprimer(self.objet[0])
                    self.objet=self.objet[1:]

                    #On supprime les coordonnées
                    self.Spos=self.Spos[1:]
                
                print(self.Spos)
                print(self.objet)
                break
                
            #droite
            elif jeu=='Right' and self.canMove(self.Spos[-1][0]+1,self.Spos[-1][1]):
                
                print(self.Spos)
                print(self.objet)
                #On rajoute la nouvelle tête en coordonnées
                self.Spos.append([self.Spos[-1][0]+1,self.Spos[-1][1]])
                #On dessine la nouvelle tête
                self.objet.append(plan.g.dessinerRectangle(self.Spos[-1][0]*plan.px+1,self.Spos[-1][1]*plan.px+1,plan.px-1,plan.px-1,"red"))
                
                #Si on ne se trouve pas sur un bonus on supprime la queue sinon on la laisse -> Comme si le serpent s'agrandi
                if not self.isBonus():
                    #On supprime l'objet
                    g.supprimer(self.objet[0])
                    self.objet=self.objet[1:]

                    #On supprime les coordonnées
                    self.Spos=self.Spos[1:]
                
                print(self.Spos)
                print(self.objet)
                break





























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


    def initGraphique(self):
        g=self.g
        dim=self.dim
        #dim correspond à la dimension on simplifie l'écriture

        for i in range(dim):
            g.dessinerLigne(i*self.px,0,i*self.px,self.px*dim,"grey")
            g.dessinerLigne(0,i*self.px,self.px*dim,i*self.px,"grey")


    #Fonction qui affiche les bonus et qui 
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
            bonus=self.g.dessinerRectangle(self.px*item[0]+1,self.px*item[1]+1,self.px-1,self.px-1,"yellow")
            self.objBonus.append(bonus)



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



### Fonction qui supprime et replace les bonus
# -->   .pop() prends en paramètre un index et .remove() prends en paramètre un élément
    def moveBonus(self,x,y,idSnake):
        #On supprime le point touché
        i=self.posB.index([x,y])
        #Supprime les coordonnées
        self.posB.pop(i)
        #Supprime l'objet
        self.g.supprimer(self.objBonus[i])
        self.objBonus.pop(i)

        #On crée de nouvelles coordonnés
        print(idSnake.Spos)
        while [x,y] in idSnake.Spos or [x,y] in self.posB or (x,y) in self.mur:
            x=random.randint(0,self.dim-1)
            y=random.randint(0,self.dim-1)

        #On ajoute les nouvelles coordonnées 
        self.posB.append([x,y])
        #On crée un nouvel objet graphique
        self.objBonus.append(self.g.dessinerRectangle(x*self.px+1,y*self.px+1,self.px-1,self.px-1,"yellow"))

        






plan=Plan(60)
snake=Snake(2)
while True:
    snake.deplaceSnake()
plan.g.attendreClic()
