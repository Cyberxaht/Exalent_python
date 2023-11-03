#koupe yon chen
Name="Mw Renmen Manje mango"
print(Name.split())
#mw mete tout premye mo an majiskil
print("_______________________________________")
print(Name.title())
print("________________________________________")
#print(Name.replace("a","@"))
print("________________________________________")
#nom= Name.upper()
print(Name.upper())
nom= Name.find("a")
print(nom)
chennlist=[]

for i in range(len(Name)):
  if Name[i] == 'a':
      chennlist.append(i)
 
if chennlist:
    print("men kantite 'a'" , chennlist)


phrase = "Ceci est une phrase de test avec des caractères a."
compteur = 0

for caractere in phrase:
    if caractere == "a":
        compteur += 1

print("Le nombre de 'a' dans la phrase est :", compteur)
#mete yon fraz a lenves 
phrase = "Voici une phrase à inverser"

# Utilisez le slicing pour inverser la phrase
phrase_inverse = phrase[::-1]
maj=phrase_inverse.upper()

# Affichez la phrase inversée
print(maj)

#yon list san doublon
lis_avek_doublon = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6]

lis_san_doublon = list(set(lis_avek_doublon))

print(lis_san_doublon)

# mw gen lis mw pral chwazi sa ki sanble yo
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis_komen = [x for x in lis1 if x in lis2]

print(lis_komen)


#eleman ki diteng 
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis_disteng = [x for x in lis1 if x not in lis2] + [y for y in lis2 if y not in lis1]

print(lis_disteng)





