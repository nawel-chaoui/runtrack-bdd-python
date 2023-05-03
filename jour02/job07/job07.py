import mysql.connector

# Connexion à la database
db = mysql.connector.connect(          
  host="localhost",
  user="root",
  password="laPlateformedeoz!1702",
  database="entreprise"
)

cursor = db.cursor()

# Exécuter la requête SQL
query = "SELECT * FROM employes WHERE salaire > 3000.00;"
cursor.execute(query)

# Récupérer les résultats de la requête
result = cursor.fetchall()

# Afficher les résultats
for row in result:
    print("Salaires au supérieur à 3000$ :",row[1], row[2])

# Créer la table "services"
create_table_query = """
CREATE TABLE services (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255)
);
"""
cursor.execute(create_table_query)

# Insérer des services dans la table "services"
insert_query = "INSERT INTO services (nom) VALUES (%s)"
values = [("Cuisine",), ("Ménage",), ("Professorat",)]
cursor.executemany(insert_query, values)

# Récupérer tous les employés et leur service respectif + jointure
query = """
SELECT employes.nom, employes.prenom, employes.salaire, services.nom AS service
FROM employes
LEFT JOIN services ON employes.id_service = services.id;
"""
cursor.execute(query)

# Afficher les résultats
result = cursor.fetchall()
for row in result:
    print("\nEmployés et leur service respectif :",row[0],row[1],"au service",row[3])


# Fermer le curseur et la connexion à la base de données
cursor.close()
db.close()