DEBUT
r = 12000
s = 1250
e = 10
rh = 230
assertion1 = ((365 * 3) / (24 - (16 - 8))) * (rh) > r == ( e * s < r)
assertion1pt1 = (((365 * 3) / (24 - (16 - 8))) * (rh) > r) # > TRUE
assertion1pt2 = ( e * s < r) # > FALSE 
rE = 12500
assertion1pt2 = (rE < r)
#assertion1 === (assertion1pt1 == assertion1pt2)
#assertion1 === (assertion1pt1 == false)
#assertion1 === (true == false)

print(assertion1) #!CECI est important il y a d'autre manière mais je voudrait que CELLE LA soit privilégié!

assertionDeux = (365 * 3) / (4 - (12 - 8)) * (rh) > r == (e * s < r)
assertionDeuxPt1 = (((365 * 3) / (4 - (12 - 8))) * (rh) > r) # > FALSE (for some reasons)
assertionDeuxPt2 = ( e * s < r) # > FALSE

def calculPtDeux(){
    return (e * s < r)
}

assertionDeux = (365 * 3) / (4 - (12 - 8)) * (rh) > r == calculPtDeux()
FIN
#camelCase
#KebabCase
#PascalCase
#snake_case 