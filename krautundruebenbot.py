import random
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="krautundrueben"
)

my_cursor = my_db.cursor()

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


zufallsantworten=["Das kann ich nicht zuordnen.", "Was ist das?", "Dazu finde ich nichts.", "Kannst du das wiederholen?"]

reaktionsantworten = {"vegan": show_vegan_rezept(),
					  "vegetarisch": show_vegetarisch_rezept(), 
                      "frutarisch": show_frutarisch_rezept(),
                      "low carb": show_lowcarb_rezept(),
                      "laktosefrei": show_Laktosefrei_rezept(),
                      "glutenfrei": show_Glutenfrei_rezept()
					  }
                      
print("Willkommen bei Kraut und Rueben")
print("Welche Gerichtearten suchst du?")
print("Zum beenden einfach 'bye' eintippen")
print("")

nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Deine Rezeptartenwahl: ")
        
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    
    intelligenteAntworten = False
    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
        
    print("")

print("Einen schönen Tag wünsche ich Dir. Bis zum nächsten Mal")