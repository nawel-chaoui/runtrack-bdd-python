import mysql.connector

class employes:
    def __init__(self):
        self.db = mysql.connector.connect(
          host="localhost",
          user="root",
          password="add un mdp",
          database="entreprise"
        )
        self.cursor = self.db.cursor()

    def insert(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.db.commit()
        print(f"Salarié {nom} {prenom} ajouté avec succès")

    def update(self, employes_id, nom, prenom, salaire, id_service):
        query = "UPDATE employes SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s"
        values = (nom, prenom, salaire, id_service, employes_id)
        self.cursor.execute(query, values)
        self.db.commit()
        print(f"Salarié {nom} {prenom} modifié avec succès")

    def delete(self, employes_id):
        query = "DELETE FROM employes WHERE id=%s"
        values = (employes_id,)
        self.cursor.execute(query, values)
        self.db.commit()
        print(f"Salarié avec l'ID {employes_id} supprimé avec succès")

    def select(self):
        query = "SELECT s.id, s.nom, s.prenom, s.salaire, se.nom FROM employes s JOIN services se ON s.id_service = se.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            print(f"{row[1]} {row[2]}, salaire : {row[3]} €, service : {row[4]}")

s = employes()
s.select()
s.insert("Elvan", "Maxime", 2400, 1)
s.update(1, "Lefvres", "Sophie", 4500, 3)
s.delete(3)

