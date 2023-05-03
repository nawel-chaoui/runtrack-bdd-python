import mysql.connector

# Connexion à la base de données
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="add un mdp",
  database="LaPlateforme"
)

# Création d'un curseur pour exécuter des requêtes
cursor = db.cursor()

# Exécuter la requête pour calculer la somme des capacités
cursor.execute("SELECT SUM(capacite) as total_capacite FROM salles")

# Récupérer le résultat de la requête
result = cursor.fetchone()

# Afficher le résultat dans la console
print("La capacité totale des salles est de", result[0],"places.")

# Fermeture de la connexion à la base de données
db.close()