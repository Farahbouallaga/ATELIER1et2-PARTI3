def frequance():
ch=str(input("entrez votre chaine : "))
tab=[ch]
n=len(tab)
c=str(input("entrer le caractere qui vous cherchez : ") )
j =0
for i in range (n):
    if tab[i]==c:
        j+=1
        return j
x=frequance()
print(x)
