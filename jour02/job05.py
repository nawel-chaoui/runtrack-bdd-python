import mysql.connector

# Connexion à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="laPlateformedeoz!1702",
  database="LaPlateforme"
)

# Création d'un curseur pour exécuter des requêtes
cursor = db.cursor()

# Exécution de la requête SQL pour calculer la superficie totale
cursor.execute("SELECT SUM(superficie) AS superficie_totale FROM etage")

# Récupération du résultat de la requête
result = cursor.fetchone()
superficie_totale = result[0]

# Affichage du résultat en console
print("La superficie de La Plateforme est de", superficie_totale, "m2")

# Fermeture de la connexion à la base de données
db.close()