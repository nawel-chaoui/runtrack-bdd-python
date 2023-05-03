import mysql.connector

db = mysql.connector.connect(          # connexion à la database
  host="localhost",
  user="root",
  password="add le mdp",
  database="LaPlateforme"
)

cursor = db.cursor()  # créer un curseur

cursor.execute("SELECT * FROM etudiants")  # selection de la tables

result = cursor.fetchall() # fetchall() retourne toutes les lignes de résultats sous forme d'une liste de tuples
                           # que nous parcourons ensuite pour les afficher avec la boucle for.

for row in result:
  print(row)