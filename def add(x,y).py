"""def add(x,y):
    return x+y

def sub():
    return x-y

def multiply():
    return x*y

def divide():     !! REFAITE EN LIGNE 65 !!
    return x/y

def modulo():
    return x%y"""

def calcul_salaire_par_s(salaire_h,heure_par_jourouvrable,jo_par_an):
    return (salaire_h*heure_par_jourouvrable*jo_par_an/(365*24*60*60))

# > autre solution
def calcul_salaire_par_s(salaire_h,heure_par_jourouvrable,jo_par_an):
    salaire_annuel = salaire_h * heure_par_jourouvrable* jo_par_an
    # calcul du salaire annuel
    secondes_par_an = 365 * 24 * 60 * 60
    #nombres de secondes par an
    return salaire_annuel / secondes_par_an #résultat des calculs en obtenant une division du salaire et des secondes

def salaire_net(salaire_brut,publique,non_publique):
    #quel est son domainbe de travail? -> publique?
    if publique: return salaire_brut / 15
    #la fonction n'est pas publique
    if non_publique: return salaire_brut /  23

"methode intervenant"
def withdrawFees(total,percent):
    #calcul du montant des taxes à retirer
    fees = total * (percent / 100)
    #je retourne mon total sans les taxes
    return total - fees

"methode intervenant"
def salaire_net(salaire_brut,public):
    #si j'occupe un poste de la fonction publique 
    if public:
    #Alors je retourne le salaire brut - 15% de taxes
        return withdrawFees(salaire_brut, 15)
    #Sinon, c'st que je suis un travailleur privé,
    else: withdrawFees(salaire_brut, 23)
    #Alors je retourne le salaire brut - 23% de taxes



nbPersonne = x

if nbPersonne == 1:
    tuRentre()
else if nbPersonne == 3:
    tuRentre()
else if nbPersonne == 5:
    tuRentre
else: 
    tuRentrePas()

# en français: -si -sinon -sinon si

"reparation de la def divide"
def divide():
    #si le denominateur différent de 0 
    if y != 0
    #retourner la division 
        return x/y
    #sinon retourner undef
    else:
        print(undef)
        #renvoyer pour finir
        return

tour = 0:
#Tant que je ne suis pas au tour 5 
while tour != 5:
#Appeler la fonction JouerUnTour
    jouerUnTour()
#J'effectue l'action de passer un tour
    tour = tour + 1

"!! Faire attention avec les /while/ et n'oubliez pas les /for()/"




def input():
    #renvoie un caractèrede type string au hasard
   

#exercice:
    #Faire un mini jeu qui affiche un  message lorsque input revoie le bon caractère
    #le caractère doit être parametrable    (besoin des while, if,)
 
    input():
        #liste des caractères
        
        #Tant que le caractère est bon??
        while         
        #on doit faire en sorte que la cha  îne de caractère soit la même
"correction"
#1 
def miniGame(winCondition):
    #je définis une variable char qui permet de contenir le caractère généré avec input
    char = input()
    #j'incrémente la variable tries (essais)
    tries += 1
    #J'affcihe le nombre d'essais
print(tries)

#2
def akiLettre(lettre):
    #définis d'abord la lettre à deviner 
    lettreADeviner = input()
    #puis le nombre d'essais 
    nombreEssais = 0
    #ensuite on boucle tant que la lettre en paramètre et la lettre à deviner sont différents 
    while lettre != lettreADeviner :
        #on recommence la fonction (appel récursif de la fonction)
        return akiLettre(lettreADevnier,nombreEssais+1)

def magiLettre(lettreADeviner):
    #jedéfinis d'abord la lettre à deviner 
    lettre = input()
    #puis le nombre d'essais 
    nombreEssais = 0
    #ensuite on boucle tant que la lettre en paramètre et la lettre à deviner sont différents 
    while lettre != lettreADeviner :
        #on recommence la fonction (appel récursif de la fonction)
        return akiLettre(lettreADevnier) + 1
    else:
        return 1
    print("Bien joué BG !")
    
    
tableau = [0,10,15,5,14,7,6,3,4,8,4,9,5,1,7,5,2,1,8,4,4,6,8]
#Pour recuperer 15 je predns dans tableau index 3 - 1
print(tableau[2]) #Renvoie 15

len(tableau) #Renvoir la longueur de tableau
prénom = "Justin"
nom = "Killigback"
nomPrenom = nom + prenom #cela renvoie KillingbackJustin
nomPrenom = nom + " " + prenom # Renvoie Killingback Justin
integerValue = 342
stringIntegerValue = str(342) # Renvoie "342" au lieu de 342

#Exercice1
#Faire une fonction qui concatene 2 chaines de caractere, les separants par une virgule 

#Exercice2
#Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractères
#avec l'ensemble des occurations d'un chiffre e.g.:
#Pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction (tableau, 0) doit renvoyer "0,4,7" n'hesitez pas a implenter la première fonction ;)
def concatene():
integer


tableauMultiType = ["Alexandre", true, tableau, 4 > 2, None]
tableauDim = [0, 1, 2, 3]
tableauDim = [0, 1, 21, 3]
tableauMultiDim = [tableauDim, tableauDim2]
tableauMultiuDim[1][2] #Renvoie 21

tableauCleVal = {"Cle" : "Valeur"}
tableauCleVal["Cle"] #Renvoie  "Valeur"

#Exercice 3
#"faire une fonction Afficher un message
#Tel Que
def afficher(msg):
    print(msg)



listeUtilisateur = {
    "Alexandre":"motdepasse"
    "Michel":"password"
    "Toto":"12345"
    "JohnDoe":"azerty"
}
#Ecrivez la fonction login(userName, password, listUser) permettant d'afficher un message de connexion si
#le combo user/password est bon

def login(Michel,password,listeUtilisateur):
    return 






DEBUT
form math import*
salaire_h*heure_par_jourouvrable

bruh





#calcul un revenu par s 
#salaire heure
#h/Jo (jour oral à voir)
#Jo / an 
0.0000360