from tkinter import * 
import tkinter
import mysql.connector

#alle Variablen
varEingabe=""
varResultate=""
varKalorien='0'
varProteine='0'
varKohlenhydrate='0'
varZucker='0'
varFett='0'
vargesättigteFettsäuren='0'
varBallaststoffe='0'
varNatrium='0'
varRezeptZutaten=''
varRezept=''


#import mySQL-Connector
my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="krautundrueben"
)

my_cursor = my_db.cursor()

#Alle vordiffinierten Infos
def Ausgabe():
    print("Rezept: Eingabe: %s" % (eingabeFeld.get()))
    eingabeFeld.delete(0,END)

#rezepteinput
def input_rezept():
    rezeptname = input('Name: ')
    ernährungskategorie = input('Kategorie: ')
    allergie1 =('Allergie1: ')
    val = f'"{rezeptname}", "{ernährungskategorie}", "{allergie1}"'
    sql = f'INSERT INTO rezepte VALUE({val})'
    my_cursor.execute(sql)
    my_db.commit()

#ernährungskategorien
#Vegan
def show_vegan_rezept():
    my_cursor.execute("""SELECT REZEPTKATEGORIEN.REZEPTNR,
       REZEPTE.REZEPT,
       REZEPTKATEGORIEN.KATEGORIENR,
       ERNAEHRUNGSKATEGORIEN.KATEGORIE

    FROM((REZEPTE
        LEFT JOIN REZEPTKATEGORIEN
                ON REZEPTE.REZEPTNR =
                    REZEPTKATEGORIEN.REZEPTNR)
        RIGHT JOIN ERNAEHRUNGSKATEGORIEN
                ON REZEPTKATEGORIEN.KATEGORIENR =
                    ERNAEHRUNGSKATEGORIEN.KATEGORIENR)
WHERE KATEGORIE='Vegan';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)
#vegetarisch
def show_vegetarisch_rezept():
    my_cursor.execute("""SELECT REZEPTKATEGORIEN.REZEPTNR,
       REZEPTE.REZEPT,
       REZEPTKATEGORIEN.KATEGORIENR,
       ERNAEHRUNGSKATEGORIEN.KATEGORIE

    FROM((REZEPTE
        LEFT JOIN REZEPTKATEGORIEN
                ON REZEPTE.REZEPTNR =
                    REZEPTKATEGORIEN.REZEPTNR)
        RIGHT JOIN ERNAEHRUNGSKATEGORIEN
                ON REZEPTKATEGORIEN.KATEGORIENR =
                    ERNAEHRUNGSKATEGORIEN.KATEGORIENR)
WHERE KATEGORIE='Vegetarisch';""")
    result = my_cursor.fetchall()  
    for _ in result:
        print(_)
#frutarisch
def show_frutarisch_rezept():
    my_cursor.execute("""SELECT REZEPTKATEGORIEN.REZEPTNR,
       REZEPTE.REZEPT,
       REZEPTKATEGORIEN.KATEGORIENR,
       ERNAEHRUNGSKATEGORIEN.KATEGORIE

    FROM((REZEPTE
        LEFT JOIN REZEPTKATEGORIEN
                ON REZEPTE.REZEPTNR =
                    REZEPTKATEGORIEN.REZEPTNR)
        RIGHT JOIN ERNAEHRUNGSKATEGORIEN 
                ON REZEPTKATEGORIEN.KATEGORIENR =
                    ERNAEHRUNGSKATEGORIEN.KATEGORIENR)
WHERE KATEGORIE='Frutarisch';""")
    result = my_cursor.fetchall()   
    for _ in result:
        print(_)
#low carb
def show_lowcarb_rezept():
    my_cursor.execute("""SELECT REZEPTKATEGORIEN.REZEPTNR,
       REZEPTE.REZEPT,
       REZEPTKATEGORIEN.KATEGORIENR,
       ERNAEHRUNGSKATEGORIEN.KATEGORIE

    FROM((REZEPTE
        LEFT JOIN REZEPTKATEGORIEN
                ON REZEPTE.REZEPTNR =
                    REZEPTKATEGORIEN.REZEPTNR)
        RIGHT JOIN ERNAEHRUNGSKATEGORIEN
                ON REZEPTKATEGORIEN.KATEGORIENR =
                    ERNAEHRUNGSKATEGORIEN.KATEGORIENR)
WHERE KATEGORIE='Low Carb';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)
#Laktosefrei
def show_Laktosefrei_rezept():
    my_cursor.execute("""SELECT REZEPTKATEGORIEN.REZEPTNR,
       REZEPTE.REZEPT,
       REZEPTKATEGORIEN.KATEGORIENR,
       ERNAEHRUNGSKATEGORIEN.KATEGORIE

    FROM((REZEPTE
        LEFT JOIN REZEPTKATEGORIEN
                ON REZEPTE.REZEPTNR =
                    REZEPTKATEGORIEN.REZEPTNR)
        RIGHT JOIN ERNAEHRUNGSKATEGORIEN
                ON REZEPTKATEGORIEN.KATEGORIENR =
                    ERNAEHRUNGSKATEGORIEN.KATEGORIENR)
WHERE KATEGORIE='Laktosefrei';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)
#Glutenfrei
def show_Glutenfrei_rezept():
    my_cursor.execute("""SELECT REZEPTKATEGORIEN.REZEPTNR,
       REZEPTE.REZEPT,
       REZEPTKATEGORIEN.KATEGORIENR,
       ERNAEHRUNGSKATEGORIEN.KATEGORIE

    FROM((REZEPTE
        LEFT JOIN REZEPTKATEGORIEN
                ON REZEPTE.REZEPTNR =
                    REZEPTKATEGORIEN.REZEPTNR)
        RIGHT JOIN ERNAEHRUNGSKATEGORIEN
                ON REZEPTKATEGORIEN.KATEGORIENR =
                    ERNAEHRUNGSKATEGORIEN.KATEGORIENR)
WHERE KATEGORIE='Glutenfrei';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)

def Test_Ausgabe_Alle_Kategorien():
    my_cursor.execute("""""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)



#allergien
#Laktose
def Allergie_Laktose():
    my_cursor.execute("""SELECT REZEPTE.REZEPTNR,
       REZEPTE.REZEPT,
       ALLERGENE.ALLERGIENNR,
       ALLERGENE.ALLERGIEN

    FROM((REZEPTE
        INNER JOIN REZEPTALERGENE
                ON REZEPTE.REZEPTNR =
                    REZEPTALERGENE.REZEPTNR)
        INNER JOIN ALLERGENE
                ON REZEPTALERGENE.ALLERGIENNR =
                    ALLERGENE.ALLERGIENNR)
WHERE ALLERGIEN !='Laktose';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)

def KeineLaktoseAllergie():
    my_cursor.execute("""SELECT REZEPTE.REZEPTNR,
       REZEPTE.REZEPT,
       ALLERGENE.ALLERGIENNR,
       ALLERGENE.ALLERGIEN

    FROM((REZEPTE
        INNER JOIN REZEPTALERGENE
                ON REZEPTE.REZEPTNR =
                    REZEPTALERGENE.REZEPTNR)
        INNER JOIN ALLERGENE
                ON REZEPTALERGENE.ALLERGIENNR =
                    ALLERGENE.ALLERGIENNR)
WHERE ALLERGIEN !='Laktose';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)
def KeineKarrottenAllergie():
    my_cursor.execute("""SELECT REZEPTE.REZEPTNR,
       REZEPTE.REZEPT,
       ALLERGENE.ALLERGIENNR,
       ALLERGENE.ALLERGIEN

    FROM((REZEPTE
        INNER JOIN REZEPTALERGENE
                ON REZEPTE.REZEPTNR =
                    REZEPTALERGENE.REZEPTNR)
        INNER JOIN ALLERGENE
                ON REZEPTALERGENE.ALLERGIENNR =
                    ALLERGENE.ALLERGIENNR)
WHERE ALLERGIEN !='Karrotten';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)
def KeineErdnuesseAllergie():
    my_cursor.execute("")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)
def KeineWeizenAllergie():
    my_cursor.execute("""SELECT REZEPTE.REZEPTNR,
       REZEPTE.REZEPT,
       ALLERGENE.ALLERGIENNR,
       ALLERGENE.ALLERGIEN

    FROM((REZEPTE
        INNER JOIN REZEPTALERGENE
                ON REZEPTE.REZEPTNR =
                    REZEPTALERGENE.REZEPTNR)
        INNER JOIN ALLERGENE
                ON REZEPTALERGENE.ALLERGIENNR =
                    ALLERGENE.ALLERGIENNR)
WHERE ALLERGIEN !='Weizen';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)
def KeineLaktoseAllergie():
    my_cursor.execute("""SELECT REZEPTE.REZEPTNR,
       REZEPTE.REZEPT,
       ALLERGENE.ALLERGIENNR,
       ALLERGENE.ALLERGIEN

    FROM((REZEPTE
        INNER JOIN REZEPTALERGENE
                ON REZEPTE.REZEPTNR =
                    REZEPTALERGENE.REZEPTNR)
        INNER JOIN ALLERGENE
                ON REZEPTALERGENE.ALLERGIENNR =
                    ALLERGENE.ALLERGIENNR)
WHERE ALLERGIEN !='Laktose';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)
def KeinGlutenAllergie():
    my_cursor.execute("""SELECT REZEPTE.REZEPTNR,
       REZEPTE.REZEPT,
       ALLERGENE.ALLERGIENNR,
       ALLERGENE.ALLERGIEN

    FROM((REZEPTE
        INNER JOIN REZEPTALERGENE
                ON REZEPTE.REZEPTNR =
                    REZEPTALERGENE.REZEPTNR)
        INNER JOIN ALLERGENE
                ON REZEPTALERGENE.ALLERGIENNR =
                    ALLERGENE.ALLERGIENNR)
WHERE ALLERGIEN !='Gluten';""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)

def Bestellungen():
    my_cursor.execute("""SELECT KUNDENNR, NACHNAME, BESTELLNR, BESTELLDATUM
    FROM KUNDE
    LEFT JOIN BESTELLUNG
        ON KUNDE.KUNDENNR =
            BESTELLUNG.KUNDENNR
WHERE KUNDE.KUNDENNR=2001;""")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)


#weitere
#resultate
def Resultate():
    result = my_cursor.fetchall()
    for _ in result:
        print(_)

#button commants
#vegan
def Vegan():
    if (buttonVegan['state'] == tkinter.NORMAL):
        show_vegan_rezept()
        AusgabeLabel = Label(master=Fenster, text=Resultate)
        AusgabeLabel.place(x=5, y=100, width=200, height=22)
#vegetarisch
def Vegetarisch():
    if (buttonVegetarisch['state'] == tkinter.NORMAL):
        show_vegetarisch_rezept()
#frutarisch
def Frutarisch():
    if (buttonVegetarisch['state'] == tkinter.NORMAL):
        show_frutarisch_rezept()
#low carb
def LowCarb():
    if (buttonVegetarisch['state'] == tkinter.NORMAL):
        show_lowcarb_rezept()
#Laktosefrei
def Laktosefrei():
    if (buttonVegetarisch['state'] == tkinter.NORMAL):
        show_Laktosefrei_rezept()
#Glutenfrei
def Glutenfrei():
    if (buttonVegetarisch['state'] == tkinter.NORMAL):
        show_Glutenfrei_rezept()

#allgergie commants
#Laktose
def LaktoseAllergie():
    if (buttonLaktoseAllergie['state'] == tkinter.NORMAL):
        KeineLaktoseAllergie()
def KarrottenAllergie():
    if (buttonEierAllergie['state'] == tkinter.NORMAL):
        KeineKarrottenAllergie()
def ErdnuesseAllergie():
    if (buttonErdnuesseAllergie['state'] == tkinter.NORMAL):
        KeineErdnuesseAllergie()
def WeizenAllergie():
    if (buttonWeizenAllergie['state'] == tkinter.NORMAL):
        KeineWeizenAllergie()
def GlutenAllergie():
    if (buttonGlutenAllergie['state'] == tkinter.NORMAL):
        KeinGlutenAllergie()
def LaktoseAllergie():
    if (buttonLaktoseAllergie['state'] == tkinter.NORMAL):
        KeineLaktoseAllergie()

def RezepteFensterOpen():
    if (buttonRezepte['state'] == tkinter.NORMAL):
        RezepteFenster = Tk()
        RezepteFenster.title ("Rezepte Fenster")
        RezepteFenster.geometry("750x500")

    class Table:
        def __init__(self,RezepteFenster): 
            for i in range(total_rows): 
               for j in range(total_columns): 
                    self.e = Entry(RezepteFenster, 
                               width=28, 
                               fg='black', 
                               font=('Arial',
                               10,
                               'bold')) 
                  
                    self.e.grid(row=i, column=j) 
                    self.e.insert(END, lst[i][j]) 

    lst = [('Nährstoffangaben','pro 100 g'), 
       ('Kalorien',varKalorien), 
       ('Proteine',varProteine), 
       ('Kohlenhydrate',varKohlenhydrate),
       ('- davon Zucker',varZucker), 
       ('Fett',varFett),
       ('- davon gesättigte Fettsäuren',vargesättigteFettsäuren),
       ('Ballaststoffe',varBallaststoffe),
       ('Natrium',varNatrium)] 
   
    total_rows = len(lst) 
    total_columns = len(lst[0])
    t = Table(RezepteFenster)

    InfoRezeptZutaten = Text(master=RezepteFenster, 
                         height=1, 
                         width=80)
    InfoRezeptZutaten.place(x=400, 
                        y=0, 
                        width=350, 
                        height=260)
    InfoRezeptZutaten.insert(END,"Zutaten:", varRezeptZutaten)

    InfoRezept = Text(master=RezepteFenster, 
                  height=1, 
                  width=80)
    InfoRezept.place(x=0, 
                 y=260, 
                 width=750, 
                 height=260)
    InfoRezept.insert(END, "Rezept:\n", varEingabe, varRezept)

    RezepteFenster.mainloop()

#tKinter Fenster Infos
Fenster = Tk()
Fenster.title ("KrautUndRueben")
Fenster.geometry("900x300")
EingabeLabel = Label(Fenster, text = "Eingabe").grid(row=5)
eingabeFeld = Entry(Fenster)
eingabeFeld.grid(row=5, column=1)
Button(Fenster, text='Ausgabe', command=Ausgabe).grid(row=10, column=1, sticky=W, pady=5)


#Buttons und Button pos
ErnaehrungsLabel = Label(Fenster, text = "Ernährungskategorie").grid(row=15)
buttonVegan = Button(master=Fenster, bg='white', text='Vegan', command=Test_Ausgabe_Alle_Kategorien)
buttonVegan.place(x=125, y=55, width=80, height=22)
buttonVegetarisch = Button(master=Fenster, bg='white', text='Vegetarisch', command=Vegetarisch)
buttonVegetarisch.place(x=205, y=55, width=80, height=22)
buttonFrutarisch = Button(master=Fenster, bg='white', text='Frutarisch', command=Frutarisch)
buttonFrutarisch.place(x=285, y=55, width=80, height=22)
buttonLowCarb = Button(master=Fenster, bg='white', text='Low Carb', command=LowCarb)
buttonLowCarb.place(x=365, y=55, width=80, height=22)
buttonLaktosefrei = Button(master=Fenster, bg='white', text='Laktosefrei', command=Laktosefrei)
buttonLaktosefrei.place(x=445, y=55, width=80, height=22)
buttonGlutenfrei = Button(master=Fenster, bg='white', text='Glutenfrei', command=Glutenfrei)
buttonGlutenfrei.place(x=525, y=55, width=80, height=22)

AllergieLabel = Label(Fenster, text = "Allergien").grid(row=25)

buttonLaktoseAllergie = Button(master=Fenster, bg="green", text="Laktose", command=LaktoseAllergie)
buttonLaktoseAllergie.place(x=125, y=77, width=80, height=22)
buttonEierAllergie = Button(master=Fenster, bg="green", text="Karrotten", command=KarrottenAllergie)
buttonEierAllergie.place(x=205, y=77, width=80, height=22)
buttonErdnuesseAllergie = Button(master=Fenster, bg="green", text="Erdnüsse", command=ErdnuesseAllergie)
buttonErdnuesseAllergie.place(x=285, y=77, width=80, height=22)
buttonWeizenAllergie = Button(master=Fenster, bg="green", text="Weizen", command=WeizenAllergie)
buttonWeizenAllergie.place(x=365, y=77, width=80, height=22)
buttonGlutenAllergie = Button(master=Fenster, bg="green", text="Gluten", command=GlutenAllergie)
buttonGlutenAllergie.place(x=445, y=77, width=80, height=22)
buttonLaktoseAllergie = Button(master=Fenster, bg="green", text="Laktose", command=LaktoseAllergie)
buttonLaktoseAllergie.place(x=525, y=77, width=80, height=22)

buttonRezepte = Button(master=Fenster, bg='green', text='Bestllungen', command=RezepteFensterOpen)
buttonRezepte.place(x=5, y=150, width=100, height=20)
buttonRezepte = Button(master=Fenster, bg='red', text='Rezepte', command=Bestellungen)
buttonRezepte.place(x=5, y=175, width=100, height=20)

exitButton = Button(master=Fenster, text='Schließen', command=Fenster.quit)
exitButton.place(x=5, y=275, width=80, height=22)


Fenster.mainloop()