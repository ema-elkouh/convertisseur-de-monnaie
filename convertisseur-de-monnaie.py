
from tkinter import *
from tkinter import messagebox
fenetre = Tk() 
fenetre.title("Convertisseur de monnaie")
fenetre.geometry("300x300")
fenetre.config(bg="#202630")
my_font = ('Arial', 16, 'bold')


Mylabel=Label(fenetre, text="CONVERTISSEUR DE MONNAIE", pady=20,fg='white', bg="#202630", font=my_font)
Mylabel.pack()


label = Label(fenetre, text="CONVERSIONS EURO")
label.pack()



s = Spinbox(fenetre, from_=0, to=float('inf'))
s.pack()


Button(fenetre, text ="CONVERTIR", relief=RAISED).pack()

#FONCTION DU BOUTON1
def euro_to_livresterling():
    d = 0.89
    somme=float(s.get())


    if somme == float(s.get()):
        resultat1 = somme/d
        Label(fenetre, text=resultat1, font= ('Times', 12)).pack(pady=5)
    else:
        return None

#FONCTION DU BOUTON2
def euro_to_dirham():
    d = 11.04   # 11.04 dirham
    # 1 euro équivaut à 11.04 dirham marocain
    somme = float(s.get())

    if somme == float(s.get()):
        resultat1 = somme*d
        Label(fenetre, text=resultat1, font= ('Times', 12)).pack(pady=5)
    else:
        return None

#FONCTION DU BOUTON3
def euro_to_dollar():
    d = 1.07
    somme=float(s.get())


    if somme == float(s.get()):
        resultat1 = somme/d
        Label(fenetre, text=resultat1, font= ('Times', 12)).pack(pady=5)
    else:
        return None



#BOUTON QUI PERMET DE CONVERTIR LES EUROS EN DLIVRE STERLING
bouton1 = Button(fenetre , text = "LIVRES STERLING", bg = "black" , fg = "white", height=1, width=15, command=euro_to_livresterling)
bouton1.pack()

#BOUTON QUI PERMET DE CONVERTIR LES EUROS EN DIRHAMS
bouton1 = Button(fenetre , text = "DIRHAM", bg = "black" , fg = "white", height=1, width=15, command=euro_to_dirham)
bouton1.pack()

#BOUTON QUI PERMET DE CONVERTIR LES DIRHAMS EN EUROS
bouton2 = Button(fenetre , text = "DOLLAR", bg = "black" , fg = "white", height=1, width=15, command=euro_to_dollar)
bouton2.pack()


Mylabel2=Label(fenetre, text="Résultat :", font=('Times', 13, 'bold'), pady=10,fg='white', bg="#202630")
Mylabel2.pack()


fenetre.mainloop()