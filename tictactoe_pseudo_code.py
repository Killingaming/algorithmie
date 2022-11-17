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
            
    #On définit la méthode affiche avec comme paramètre content qui affichera le tableau du jeu
        # pour i allant de 0 à la longueur du tableau content -1
            #On initialise la variable contentLine à une chaine de caractères vide
            #pour j allant de 0 à la longueur du tableau content -1
                #On ajoute à contentLine la valeur de gamePlate de coordonnées (i,j)
                #On ajoute à contentLine la chaine de caractères " | "
            #On affiche en console contentLine

    #On définit la méthode ticTacToeStart qui créera le tableau. 
        #pour i allant de 0 à 2 
            #on ajoute un tableau vide à la fin de l'attribut gamePlate
            #pour une variable quelconque allant de 0 à 2
                #On rajoute un caractère dans le tableau d'index i, montrant la case n
        #on affiche le gamePlate
    
    #on définit la méthode win qui annonce le vainqueur de la partie et prend comme paramètre la chaine de caractères pointOwner (qui vaut "X" ou "O")
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
    
   
   
    #On définit la méthode draw qui ne prends pas de paramètres qui annonce une égalité 
        #On renvoie qu'il s'agit est une égalité 



#On définit la méthode playerTurn qui seras utile pour les actions à faire du joueur


    


            #retourner


#FIN
