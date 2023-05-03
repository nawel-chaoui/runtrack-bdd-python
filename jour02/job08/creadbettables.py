import mysql.connector

# Se connecter à la base de données MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="laPlateformedeoz!1702"
)

# Créer la base de données zoo
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE zoo")
mycursor.execute("USE zoo")

# Créer la table animal
mycursor.execute("CREATE TABLE animal (ID INT PRIMARY KEY NOT NULL, NOM VARCHAR(55) NOT NULL, RACE VARCHAR(55) NOT NULL, CAGE_ID INT NOT NULL, DATE_NAISSANCE DATE NOT NULL, PAYS_ORIGINE VARCHAR(55) NOT NULL)")

# Créer la table cage
mycursor.execute("CREATE TABLE cage (ID INT PRIMARY KEY NOT NULL, SUPERFICIE FLOAT NOT NULL, CAPACITE INT NOT NULL)")




