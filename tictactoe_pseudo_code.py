#DEBUT
#On importe la bibiliothèque random
#On crée la classe objet TicTacToe   
    
    #On définit une surcharge de la méthode constructeur __init__ avec comme paramètre un booléen secondPlayer qui atteste de la présence (ou non) d'un deuxième joueur 
        #s'il y a un second joueur
            #Pas de présence d'une IA
        #sinon, il n'y a qu'un seul joueur
            #on indique la présence d'une IA
        #Initialisation du tableau de jeu (vide) gamePlate, attribut de l'objet TicTacToe
        #Initialisation du pointOwner pour le premier joueur, attribut de l'objet TicTacToe (on part du principe qu'en Player VS IA le joueur commence)
            
    #On définit la méthode affiche avec comme paramètre une liste content qui affichera le tableau du jeu en console
        # pour i allant de 0 à la longueur du tableau content -1
            #On initialise la variable contentLine égale à une chaine de caractères vide
            #pour j allant de 0 à la longueur du tableau content -1
                #On ajoute à contentLine la valeur de gamePlate de coordonnées (i,j)
                #On ajoute à contentLine la chaine de caractères " | "
            #On affiche en console contentLine

    #On définit la méthode ticTacToeStart qui ne prend pas de paramètres qui créera le tableau. Elle ne prend pas de paramètres.
        #pour i allant de 0 à 2 
            #on ajoute un tableau vide à la fin de l'attribut gamePlate
            #pour une variable quelconque allant de 0 à 2
                #On rajoute un caractère dans le tableau d'index i, montrant la case n
        #on affiche le gamePlate
    
    #On définit la méthode win avec comme paramètre pointOwner qui annonce le vainqueur de la partie et prend comme paramètre la chaine de caractères pointOwner (qui vaut "X" ou "O")
        #si l'IA est présente :
            #alors
            #si pointOwner est égale à "X" :
                #alors
                #Retourner que le joueur a gagné
            #sinon :
                #alors
                #On retourne que le vainqueur est l'IA
        #sinon :
            #Si pointOwner est égale à "X" :
                #alors
                #On retourne que le vainqueur est le joueur 1
            #sinon :
                #alors
                #On retourne que le vainqueur est le joueur 2
    
   
   
    #On définit la méthode draw qui ne prend pas de paramètre qui annonce une égalité s'il y en a une 
        #On renvoie qu'il s'agit est une égalité 



    #On définit la méthode playerTurn qui ne prends pas de paramètres qui seras utile pour les actions à faire du joueur
        #On définit la variable rowCoord qui est le résultat entier d'un input qui demande au joueur un nombre entre 1 et 3, nombre auquel on retire 1 (pour les index)
        #On vérifie que rowCoord est supérieure ou égale à 0 et dans le même temps inférieure ou égale à 2, si ce n'est pas le cas on renvoie un message expliquant l'origine de l'erreur
        #On définit la variable colCoord qui est le résultat entier d'un input qui demande au joueur un nombre entre 1 et 3, nombre auquel on retire 1 (pour les index)
        #On vérifie que colCoord est supérieure ou égale à 0 et dans le même temps inférieure ou égale à 2, si ce n'est pas le cas on renvoie un message expliquant l'origine de l'erreur
        #On retourne le tuple contenant rowCoord et colCoord

    #On définit la méthode botTurn qui ne prends pas de mparamètres, qui seras utile pour les actions à faire du bot
        #On définit la variable botRowCoord qui choisira au hasard un résultat entre 0 et 2
        #On définit la variable botColCoord qui choisira au hasard un résultat entre 0 et 2
        #On retourne la ligne et la colonne du point

    #On définit la méthode playerWin qui prend un paramètre player et renvoie si ce dernier a gagné
        #On définit une variable win égale à None
        #On définit une variable length qui est égale à la longueur du tableau attribut gamePlate (le nombre de lignes)
        
        #On vérifie d'abord les lignes
        #pour i allant de 0 à length-1 :
            #On redéfinit win égale à True
            #pour j allant de 0 à length-1 :
                #si l'élement d'index (i,j) dans l'attribut tableau gamePlate est différent de player :
                    #alors
                    #On redéfinit win égal à False
                    #La boucle s'arrête
            #si win est égale à True :
                #alors
                #On retourne la valeur de win

        #on vérifie ensuite les colonnes
        # pour i allant de 0 à length -1 :  
            #On redéfinit win égale à True 
            #pour j allant de 0 à length -1 :
                #si l'élement d'index (j,i) dans l'attribut tableau gamePlate est différent de player :
                    #alors
                    #On redéfinit win égal à False
                    #La boucle s'arrête
            #si win est égale à True :
                # On retourne la valeur de win

        #on vérifie les diagonales
        #On redéfinit win égale à True
        #pour i allant de 0 à lenght-1
            #si l'élément d'index (i,i) dans l'attribut tableau gamePlate est différent de player :
                #alors
                #on redéfinit win égal à False
                #la boucle s'arrête
        #si win est True:
            #On retourne la valeur de win
        
        #On redéfinit win égale à True
        #pour i allant de 0 à length-1
            #si l'élment d'index (i,lenght-1-i) dans l'attribut tableau gamePlate est différent de player :
                #on redéfinit win égal à False
                #la boucle s'arrête
        #si win est True:
            #on retourne la valuer win
        #on retourne False

    
    #On définit la méthode swapTurn qui prend un paramètre player et renvoie le joueur opposé
        #On renvoie 'X' si player est égale à 'O' sinon on renvoie 'O'
    
    #On définit la méthode filledGamePlate qui ne prend pas de paramètre et vérifie si le tableau est complet ou non
        #On définit la variable filled égale à True
        #pour i allant de 0 à la longueur du tableau attribut gamePlate -1 :
            #pour j allant de 0 à la longueur du tableau attribut gamePlate -1 :
                #si la valeur de coordonnées (i,j) dans gamePlate est égale à '*' :
                    #alors
                    #On redéfinit filled égale à False
                    #La boucle s'arrête
        #si filled est True
            #on retourne la valeur de filled
        #on retourne False

    #On définit la méthode ticTacToeGame qui ne prend pas de paramètre et simule dans son intégralité une partie de morpion
        #on définit une liste vide takenCoords qui enregistre les coordonnées placées au fur et à mesure
        #On définit une variable continuing égale à True
        #si l'attribut iaMode est égal à True :
            #alors
            #tant que continuing est égale à True :
                #on définit l'attribut playerCoords en appelant la méthode playerTurn
                #si l'élément de coordonnées playerCoords est différent de "*" et que dans le même temps playerCoords n'est pas dans takenCoords :
                    #alors 
                    #on renvoie en console qu'il n'est pas possible de prendre une coordonnée déjà prise, il faut donc recommencer
                    #on redéfinit playerCoords en appelant la méthode playerTurn
                #sinon :
                    #alors
                    #

        
        #sinon :
            #Tant que continuing est True:
                #on définit l'attribut playerCoords en appelant la méthode playerTurn
                #si l'élément de coordonnées (firstPlayerCoords[0],firstPlayerCoords[1]) "en inclusion les données 0 et 1"  dans l'attribut tableau gamePlate est différent de firstPlayerCoords dans takenCoords :
                    #On retourne qu'on ne peux pas choisir une case prise auparavant, essayez encore
                    #on redéfinit l'attribut playerCoords en appelant la méthode playerTurn
                #sinon
                    #On rajoute firstPlayerCoors à takenCoords
                
                #self.gamePlate[self._firstPlayerCoords[0]].insert(self._firstPlayerCoords[1],self._pointOwner)


#FIN
