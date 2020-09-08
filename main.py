"""
#1)

temps = 6.892
distance = 19.7

vitesse = distance / temps

print("La vitesse est de",vitesse)
print("%.1f" % vitesse)

#2)

nom=str(input("saisir nom :"))
age=int(input("saisir age :"))
print(nom, age)


#3)

import math
flottant = float(input("Saisir la valeur du flottant :"))
if flottant >= 0 :
    print (math.sqrt(flottant))
else :
    print ("erreur")

#4)

mot1 = input("Saisir un mot :")
mot2 = input("Sisir un deuxième mot :")
if mot1<mot2 :
    print (mot1)
elif mot1>mot2 :
    print (mot2)
else :
    print("Les 2 mots sont égaux")

#5)

pression = float(input("Saisir la pression :"))
volume = float(input("Saisir le volume :"))

if pression > 2.3 and volume > 7.41 :
    print("arrêt immédiat")
elif pression > 2.3 :
    print("augmenter le volume")
elif volume > 7.41 :
    print ("diminuer le volume")
else :
    print("tout va bene")



#6)

ch = input("Saisir une chaine de caractères :")
if "@" in ch and ch.endswith(".com") :
    print("valide")
else :
    print("erreur")


#7)

for i in range (10) :
    print("Abdullah")

#8)

mot = "Abdullah"
for i in mot :
    print (i)

#9)

a = 0
b = 10

for i in range (a,b) :
    print (i)

#10)

a = 0
b = 10

while b!=0 :
    if b%2 == 1 :
        print(b)
    b=b-1

#11)

n=int(input("Saisir un nombre entre 1 et 10 :"))

while (n<1) or (n>10) :
    n = int(input("Le nombre saisi n'est pas entre 1 et 10"))
print (n)

#12)

ch = "Abdullah"
for i in ch :
    print(i)

l = [1,2,3,4,5]
for i in l :
    print(i)

#13)

for i in range(1,15) :
    if i%3==0 :
        print(i)

#14)

n = 24
i=0
while i<=n :
    if i%2==0 :
        print(i)
    i=i+1

for i in range(24) :
    if i%2==0 :
        print(i)

#15)

liste = [17, 38, 10, 25, 72]
print(liste[1:3])
print(liste[:2])
print(liste[-3])
print(liste[:])
#print(liste.index(17))
#liste.remove(38)
#liste.append(12)
#liste.sort()
#liste.reverse()
#print (liste)

#16)

ch = "halludbA"
print(ch[::-1])

#17)

str = input("Saisir un mot :")
reverse = str[::-1]
if str == reverse :
    print("La chaine est un palindrome")
else :
    print("La chaine n'est pas un palindrome")

#18)

n = input("Saisir une adresse mail : ")
var = "." + n[-3:]
var1 = "." + n[-2:]
var2 = "." + n[-1:]

if "@" in n and (n.endswith(var)) or (n.endswith(var1)) or (n.endswith(var2)) :
    print("L'adresse mail est valide")
else :
    print("Adresse mail non valide")

#19)

truc = []
machin = [0.0]*5

print ("truc = ", truc)
print ("machin =", machin)

#20)

for i in range(0,4) :
    print(i)
for i in range(4,8) :
    print(i)
tab = [1,2,3,4,5,6,7,8]
for i in tab[1::2] :
    print(i)

chose = [0, 1, 2, 3, 4, 5]
n = int(input("Saisir un nombre a tester :"))
if n in chose :
    print("true")
else :
    print("Le nombre n'est pas dans la liste")
"""




























