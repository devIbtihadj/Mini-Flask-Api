--CREATE DATABASE tp_api_iai;
CREATE TABLE tp_api_iai.categories(
	id SERIAL PRIMARY KEY,
	libelle_categorie VARCHAR(20)

	)
CREATE TABLE tp_api_iai.livres(
	id SERIAL PRIMARY KEY,
	isbn VARCHAR(15),
	titre VARCHAR(30),
	date_publication DATE,
	auteur VARCHAR(20),
	editeur VARCHAR(20),
	categorie_id INTEGER,
	CONSTRAINT PK_LIVRES_CATEGORIES FOREIGN KEY (id) REFERENCES categories(id) )

	--Vous aurez à faire vos propres insertions