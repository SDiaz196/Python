SELECT * FROM dojos; 
INSERT INTO dojos(name) VALUES("dojos1"),("dojos2"),("dojos3");
SELECT * FROM ninjas; 
DELETE FROM dojos WHERE id < 4; 
INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES ("bob","smith",28,4),("joe","doe",27,4),("jane","doe",30,4);
INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES ("billy","johnson",38,5),("david","lee",57,5),("yang","cui",40,5);
INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES ("stephen","diaz",28,6),("kyle","guzman",30,6),("kirstie","gonzales",32,6); 
SELECT * FROM ninjas WHERE dojo_id = 4;  
SELECT * FROM ninjas WHERE dojo_id = 6; 
SELECT dojo_id FROM ninjas WHERE id = 9; 