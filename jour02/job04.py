import mysql.connector

# Se connecter à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*******************",
  database="LaPlateforme"
)

# Créer un curseur
cursor = db.cursor()

# Exécuter une requête SELECT pour récupérer les noms et les capacités de la table "salles"
query = "SELECT nom, capacite FROM salles"
cursor.execute(query)  # "query" est un terme utilisé dans le domaine des bases de données pour désigner une demande
                       # d'information ou une requête envoyée à une base de données afin de récupérer des données

# Récupérer les résultats et les afficher en console
for nom, capacite in cursor:
    print(f"\nNom: {nom}\nCapacité: {capacite}")

# Fermer le curseur et la connexion
cursor.close()
db.close()
