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
            #On initialise la variable contentLine à une chaine de caractères vide
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
        #On définit la variable 

    #On définit la méthode playerWin qui prend un paramètre player et renvoie si ce dernier a gagné
        #On définit une variable win égale à None
        #On définit une variable length qui est égale à la longueur du tableau attribut gamePlate (le nombre de lignes)
        #pour i allant de 0 à length-1 
            #On indente win à True
            #pour j allant de 0 à length-1 

#FIN
