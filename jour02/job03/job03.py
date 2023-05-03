import mysql.connector

# Se connecter à la base de données
db = mysql.connector.connect(
    user='root',
    password='laPlateformedeoz!1702',
    host='localhost',
    database='dblaplateforme'
)
cursor = db.cursor()

# Obtenir la liste des tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Exporter chaque table dans un fichier SQL
for table in tables:
    table_name = table[0]
    with open(f'{table_name}.sql', 'w') as f:
        cursor.execute(f"SELECT * FROM {table_name}")
        for row in cursor:
            f.write(str(row))

# Fermer la connexion
cursor.close()
db.close()