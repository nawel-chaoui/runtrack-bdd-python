mysql> CREATE TABLE etage (id INT PRIMARY KEY AUTO_INCREMENT,nom VARCHAR(255),numero INT,superficie INT);
Query OK, 0 rows affected (0.02 sec)

mysql> CREATE TABLE salles (id INT PRIMARY KEY AUTO_INCREMENT,nom VARCHAR(255),id_etage INT,capacite INT);
Query OK, 0 rows affected (0.02 sec)

mysql> INSERT INTO etage (nom, numero, superficie) VALUES ('RDC', 0, 500);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO etage (nom, numero, superficie) VALUES ('R+1', 1, 500);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO salles (nom, id_etage, capacite) VALUES ('Lounge', 1, 100);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO salles (nom, id_etage, capacite) VALUES ('Studio Son', 1, 5);
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO salles (nom, id_etage, capacite) VALUES ('Broadcasting', 2, 50);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO salles (nom, id_etage, capacite) VALUES ('Bocal Peda', 2, 4);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO salles (nom, id_etage, capacite) VALUES ('Coworking', 2, 80);
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO salles (nom, id_etage, capacite) VALUES ('Studio Video', 2, 5);
Query OK, 1 row affected (0.01 sec)

# pour exporter
mysqldump -u root -p laplateforme > dblaplateforme.sql;