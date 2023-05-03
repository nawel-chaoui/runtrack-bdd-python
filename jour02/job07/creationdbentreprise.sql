mysql> CREATE DATABASE entreprise;

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| amitbd             |
| entreprise         |
| information_schema |
| laplateforme       |
| mysql              |
| performance_schema |
| sys                |
+--------------------+

mysql> use entreprise
Database changed

mysql> CREATE TABLE employes (id INT PRIMARY KEY AUTO_INCREMENT,nom VARCHAR(255), prenom VARCHAR(55),salaire DECIMAL(10, 3),id_service INT);
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;
+----------------------+
| Tables_in_entreprise |
+----------------------+
| employes             |
+----------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO employes (nom, prenom, salaire, id_service) VALUES ('Lefevre', 'Sophie', 4544.45, 3),('Roux', 'Pierre', 2352.78, 1), ('Fournier', 'Lucie', 3400.00, 2);
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from employes;
+----+----------+--------+----------+------------+
| id | nom      | prenom | salaire  | id_service |
+----+----------+--------+----------+------------+
|  1 | Lefevre  | Sophie | 4544.450 |          3 |
|  2 | Roux     | Pierre | 2352.780 |          1 |
|  3 | Fournier | Lucie  | 3400.000 |          2 |
+----+----------+--------+----------+------------+