## Jeu du monstre
from tkiteasy import *
import random 

dep={"Haut":(0,-1),"Bas":(0,1),"Gauche":(-1,0),"Droite":(1,0)}
#Classe Jeu du mosntre : 

class JeuDuMonstre():
    def __init__(self,dim):
        self.px=800//dim
        self.dim=dim
        self.posJ=[random.randint(0,dim-1),random.randint(0,dim-1)]
        self.posM=[[random.randint(0,dim-1),random.randint(0,dim-1)] for i in range(dim//5)]


        self.g=ouvrirFenetre(self.px*self.dim,self.px*self.dim)
        self.initGraphique()

        self.mur=[]
        self.wall(self.dim//3)


    def initGraphique(self):
        g=self.g
        dim=self.dim
        #dim correspond à la dimension on simplifie l'écriture

        for i in range(dim):
            g.dessinerLigne(i*self.px,0,i*self.px,self.px*dim,"grey")
            g.dessinerLigne(0,i*self.px,self.px*dim,i*self.px,"grey")

        self.J=g.dessinerRectangle(self.px*self.posJ[0]+1,self.px*self.posJ[1]+1,self.px-1,self.px-1,"red")
        self.M=[]
        for mons in self.posM:
            m=g.dessinerRectangle(self.px*mons[0]+1,self.px*mons[1]+1,self.px-1,self.px-1,"yellow")
            self.M.append(m)


    def deplaceJoueur(self):
        g=self.g
        

        # self.initGraphique()
        #Objets message d'erreur
        carre=None
        txt=None

        while True:

            #attribution des valeurs cliquables
            xJ=self.posJ[0]*self.px
            yJ=self.posJ[1]*self.px

            #Suppression message d'erreur
            while carre!=None:
                suite=g.attendreTouche()
                if suite =="Return":
                    g.supprimer(carre)
                    g.supprimer(txt)
                    print(carre,txt)
                    carre,txt=None,None
                    print(carre,txt)
                    break

            
             
            jeu=g.attendreClic()
            #jeu est le point cliqué sur le plan --> on vérifie si il est au voisinage du joueur 
            
            #haut
            if xJ <= jeu.x <= xJ+self.px and yJ-self.px<=jeu.y<=yJ:
                self.posJ[1]-=1
                g.deplacer(self.J,0,-self.px)
                
            #bas
            elif xJ <= jeu.x <= xJ+self.px and yJ+self.px<=jeu.y<=yJ+2*self.px:
                self.posJ[1]+=1
                g.deplacer(self.J,0,self.px)
                
            #gauche
            elif xJ-self.px <= jeu.x <= xJ and yJ<=jeu.y<=yJ+self.px:
                self.posJ[0]-=1
                g.deplacer(self.J,-self.px,0)
                
            #droite
            elif xJ+self.px <= jeu.x <= xJ+2*self.px and yJ<=jeu.y<=yJ+self.px:
                self.posJ[0]+=1
                g.deplacer(self.J,self.px,0)
                
            #Sinon on recommence et affiche un message d'erreur
            else:
                #Affichage message d'erreur
                carre=g.dessinerRectangle(self.dim*self.px/2-150,self.dim*self.px/2-50,300,100,"blue")
                txt=g.afficherTexte("Veuillez recliquez au voisinage\n       de la case du joueur\n\nAppuyez sur Entrer pour continuer"
                                    ,self.dim*self.px/2,self.dim*self.px/2)
                

 ######### Déplacer le joueur à l'aide des flèches du clavier ##############               
    def deplaceJoueurTouche(self):
        g=self.g
        

        # self.initGraphique()
        #Objets message d'erreur
        carre=None
        txt=None

        while True:

            #attribution des valeurs cliquables
            xJ=self.posJ[0]*self.px
            yJ=self.posJ[1]*self.px

            #Suppression message d'erreur
            while carre!=None:
                suite=g.attendreTouche()
                if suite =="Return":
                    g.supprimer(carre)
                    g.supprimer(txt)
                    break

            
             
            jeu=g.attendreTouche()
            #jeu est le point cliqué sur le plan --> on vérifie si il est au voisinage du joueur 
            
            #haut
            if jeu=='Up' and self.posJ[1]>0 and (self.posJ[0],self.posJ[1]-1) not in self.mur:
                self.posJ[1]-=1
                g.deplacer(self.J,0,-self.px)
                break
                
            #bas
            elif jeu=='Down' and self.posJ[1]<self.dim-1 and (self.posJ[0],self.posJ[1]+1) not in self.mur:
                self.posJ[1]+=1
                g.deplacer(self.J,0,self.px)
                break
                
            #gauche
            elif jeu=='Left' and self.posJ[0]>0 and (self.posJ[0]-1,self.posJ[1]) not in self.mur:
                self.posJ[0]-=1
                g.deplacer(self.J,-self.px,0)
                break
                
            #droite
            elif jeu=='Right' and self.posJ[0]<self.dim-1 and (self.posJ[0]+1,self.posJ[1]) not in self.mur:
                self.posJ[0]+=1
                g.deplacer(self.J,self.px,0)
                break
            

    def deplaceMonstre(self):
        g=self.g

        #posM -> positions des montres
        for i in range(len(self.posM)):
            #On initialise les déplacements 
            depx,   depy= self.posJ[0]-self.posM[i][0],    self.posJ[1]-self.posM[i][1]


            #Si la distance en y est plus grande on la réduit et on regarde si le monstre n'est pas sur le joueur
            if  abs(depy)>= abs(depx) and (depx,depy)!=(0,0):

                #Si il faut monter
                if depy<0 and (self.posM[i][0],self.posM[i][1]-1) not in self.mur:
                    self.posM[i][1]-=1
                    g.deplacer(self.M[i],0,-self.px)
                
                #Sinon on descend 
                elif depy>=0 and (self.posM[i][0],self.posM[i][1]+1) not in self.mur:
                    self.posM[i][1]+=1
                    g.deplacer(self.M[i],0,self.px)
            
            #Si la distance en x est plus grande on la réduit
            else:
                #Gauche
                if depx<0 and (self.posM[i][0]-1,self.posM[i][1]) not in self.mur:
                    self.posM[i][0]-=1
                    g.deplacer(self.M[i],-self.px,0)
                #Droite
                elif depx >=0 and (self.posM[i][0]+1,self.posM[i][1]) not in self.mur:
                    self.posM[i][0]+=1
                    g.deplacer(self.M[i],self.px,0)

            #Si le montre mange on coupe 
            if self.posJ==self.posM[i] or depx==depy==0 :
                g.dessinerRectangle(self.dim*self.px/2-150,self.dim*self.px/2-50,300,100,"blue")
                g.afficherTexte("   Vous avez perdu !!\n\n      --> Quitter <--"
                                        ,self.dim*self.px/2,self.dim*self.px/2)
                g.attendreTouche()
                g.fermerFenetre()



    def jeu(self):
        while True:
            p.deplaceJoueurTouche()
            p.deplaceMonstre()


        


    def wall(self,n):
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
                self.mur.append((x,y))






p=JeuDuMonstre(30)
p.jeu()