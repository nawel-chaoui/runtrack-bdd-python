mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| amitbd             |
| information_schema |
| laplateforme       |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> use laplateforme;
Database changed

mysql> show tables;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etudiants              |
+------------------------+


mysql> CREATE TABLE etage (id INT PRIMARY KEY AUTO_INCREMENT,nom VARCHAR(255),numero INT,superficie INT);
Query OK, 0 rows affected (0.02 sec)

mysql> CREATE TABLE salles (id INT PRIMARY KEY AUTO_INCREMENT,nom VARCHAR(255),id_etage INT,capacite INT);
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etage                  |
| etudiants              |
| salles                 |
+------------------------+

