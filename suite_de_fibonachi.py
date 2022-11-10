#On crée une fonction fibonacvhi qui prend en paramètre le nombre d'éléments dans la liste 
def fibo(b):
    #On crée une liste qui va contenir les éléments de la suite
    l = []
    #On crée un incrémentateur pour la boucle
    i = 0
    #On met dans une variable le premier élément de la suite qui est 0
    elem1 = 0 
    #On met dans une autre variable le deuxième élément de la liste
    elem2 = 1
    #Si le paramètre est égal à 1 
    if b == 1 :
        #Alors on ajoute dans la liste le premier élément et on la retourne
        l.append(elem1)
        return
    #Tant que i est inférieu à b
    while i < b :
        #On crée une variable temporaire qui va stocker la somme des deux derniers éléments 
        somme = elem1 + elem2 
        #On ajoute à la liste la variable somme
        l.append(somme)
        #On réatribut la bonne valeur à elem1 et elem2
        elem1 = elem2
        elem2 = l[-1]
        #On ajoute 1 à i
        i = i+1
    #Puis on retourne la liste
    return customJoin(1)