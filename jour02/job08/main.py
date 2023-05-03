import mysql.connector

# Se connecter à la base de données MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="add un mdp",
  database="zoo"
)

# Demander à l'utilisateur ce qu'il souhaite faire
while True:
    print("\nQue voulez-vous faire ?")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Ajouter une cage")
    print("5. Supprimer une cage")
    print("6. Modifier une cage")
    print("7. Afficher tous les animaux")
    print("8. Afficher les animaux dans les cages")
    print("9. Calculer la superficie totale des cages")
    print("0. Quitter")
    choix = input("\nEntrez le numéro de votre choix : ")

    if choix == "1":
        # Ajouter un animal dans la table animal
        id = input("Entrez l'ID de l'animal : ")
        nom = input("Entrez le nom de l'animal : ")
        race = input("Entrez la race de l'animal : ")
        cage_id = input("Entrez l'ID de la cage de l'animal : ")
        date_naissance = input("Entrez la date de naissance de l'animal (format : AAAA-MM-JJ) : ")
        pays_origine = input("Entrez le pays d'origine de l'animal : ")
        animal_data = (id, nom, race, cage_id, date_naissance, pays_origine)
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO animal (ID, NOM, RACE, CAGE_ID, DATE_NAISSANCE, PAYS_ORIGINE) VALUES (%s, %s, %s, %s, %s, %s)", animal_data)
        mydb.commit()
        print("\nL'animal a été ajouté avec succès !")

    elif choix == "2":
        # Supprimer un animal
        id = input("Entrez l'ID de l'animal à supprimer : ")
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM animal WHERE ID = %s", (id,))
        mydb.commit()
        print("\nL'animal a été supprimé avec succès !")

    elif choix == "3":
        # Modifier un animal
        id = input("Entrez l'ID de l'animal à modifier : ")
        nom = input("Entrez le nouveau nom de l'animal : ")
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE animal SET NOM = %s WHERE ID = %s", (nom, id))
        mydb.commit()
        print("\nL'animal a été modifié avec succès !")

    elif choix == "4":
        # Ajouter une cage dans la table cage
        id = input("Entrez l'ID de la cage : ")
        superficie = input("Entrez la superficie de la cage : ")
        capacite = input("Entrez la capacité de la cage : ")
        cage_data = (id, superficie, capacite)
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO cage (ID, SUPERFICIE, CAPACITE) VALUES (%s, %s, %s)", cage_data)
        mydb.commit()
        print("\nLa cage a été ajoutée avec succès !")

    elif choix == "5":
    # Supprimer une cage
     id = input("Entrez l'ID de la cage à supprimer : ")
     mycursor = mydb.cursor()
     mycursor.execute("SELECT COUNT(*) FROM animal WHERE CAGE_ID = %s", (id,))
     (count,) = mycursor.fetchone()
     if count > 0:
         print("\n7Impossible de supprimer la cage car elle contient encore des animaux.")
     else:
         mycursor.execute("DELETE FROM cage WHERE ID = %s", (id,))
         mydb.commit()
         print("\nLa cage a été supprimée avec succès !")

    elif choix == "6":
    # Modifier une cage
     id = input("Entrez l'ID de la cage à modifier : ")
     superficie = input("Entrez la nouvelle superficie de la cage : ")
     capacite = input("Entrez la nouvelle capacité de la cage : ")
     mycursor = mydb.cursor()
     mycursor.execute("UPDATE cage SET SUPERFICIE = %s, CAPACITE = %s WHERE ID = %s", (superficie, capacite, id))
     mydb.commit()
     print("\nLa cage a été modifiée avec succès !")

    elif choix == "7":
    # Afficher tous les animaux
     mycursor = mydb.cursor()
     mycursor.execute("SELECT * FROM animal")
     result = mycursor.fetchall()
     for row in result:
        print(row)

    elif choix == "8":
     # Afficher les animaux dans les cages
     mycursor = mydb.cursor()
     mycursor.execute("SELECT cage.ID, animal.NOM FROM cage LEFT JOIN animal ON cage.ID = animal.CAGE_ID ORDER BY cage.ID")
     result = mycursor.fetchall()
     cage_id = None
     for row in result:
        if cage_id != row[0]:
            cage_id = row[0]
            print(f"Cage {cage_id} :")
        print(f"- {row[1]}")

    elif choix == "9":
    # Calculer la superficie totale des cages
     mycursor = mydb.cursor()
     mycursor.execute("SELECT SUM(SUPERFICIE) FROM cage")
     (superficie_totale,) = mycursor.fetchone()
     print(f"\nLa superficie totale des cages est de {superficie_totale} m².")
    
    elif choix == "0":
     # Quitter le programme
     break

    else:
     print("\nChoix invalide.")
