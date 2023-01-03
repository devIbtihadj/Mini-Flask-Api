#  TP API SUR GESTION DES LIVRES

## Présentation

### Installation des dépendances

#### Python 3.9.0
#### pip 22.0.3 de programs\python\python39-32\lib\site-packages\pip (python 3.9)

Suivez les instructions pour installer la dernière version de python pour votre plate-forme dans la [docs python](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Environnement virtuel

Nous vous recommandons de travailler dans un environnement virtuel chaque fois que vous utilisez Python pour des projets. Cela permet de garder vos dépendances pour chaque projet séparées et organisées. Les instructions de configuration d'un environnement virtuel pour votre plate-forme se trouvent dans les [documents python](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) 


#### Dépendances PIP

Une fois que vous avez configuré et exécuté votre environnement virtuel, installez les dépendances en accédant au répertoire `TP_IAI_API` et en exécutant :

```bash
pip install -r requirements.txt
ou
pip3 install -r requirements.txt
```

Cela installera tous les packages requis que nous avons sélectionnés dans le fichier "requirements.txt".

##### Dépendances clés

- [Flask](http://flask.pocoo.org/) est un framework léger de microservices backend. Flask est nécessaire pour gérer les demandes et les réponses.

- [SQLAlchemy](https://www.sqlalchemy.org/) est la boîte à outils Python SQL et l'ORM que nous utiliserons pour gérer la base de données postgres légère. Vous travaillerez principalement dans app.py et pourrez référencer models.py.



## Configuration de la base de données
Avec Postgres en cours d'exécution, restaurez une base de données à l'aide du fichier `tp_api_iai.sql` fourni. Depuis le dossier dans le terminal, exécutez :

```bash
    psql tp_api_iai < tp_api_iai.sql
```

## Démarrage du serveur

Dans le répertoire `TP_IAI_API`, assurez-vous d'abord que vous travaillez avec votre environnement virtuel créé.

Pour exécuter le serveur sous Linux, Mac, ou Windows exécutez :

```bash
    flask run
```
### Note
Vous n'avez pas besoin de préciser les variables d'environnement contenant l'environnement de developpement et le le nom de l'application, car cela est dejà précisé dans le fichier `.flaskenv` si vous êtes en local. Le mode debug a également été mis à ON.


## REFERENCE DE L'API

### Commençons

URL de base : à l'heure actuelle, cette application ne peut être exécutée que localement et n'est pas hébergée en tant qu'URL de base. L'application principale est hébergée par défaut, http://localhost:5000 ; qui est défini par défaut.

## La gestion des erreurs
Les erreurs sont renvoyées sous forme d'objets JSON au format suivant :
```
{
     "success": False
     "error": 400
     "message": "Bad request"
}
```

L'API renvoie deux types d'erreurs en cas d'échec des requêtes :
- 400: Bad request
-  404: Not found

## Endpoints

## GET/livres

    GENERAL:
        Ce point de terminaison renvoie une liste d'objets livvres, la valeur de réussite, le nombre total de livre. 
        
     EXEMPLE : curl http://localhost:5000/lvres
```bash
    {
        "books": [
        {
        "auteur": "Ibtihadj",
        "categorie_id": 1,
        "date_publication": "Sat, 12 Feb 2022 00:00:00 GMT",
        "editeur": "KPEKPASSI",
        "id": 1,
        "isbn": "126-23",
        "titre": "Les nuages du pays"
        },
        {
        "auteur": "Oscar",
        "categorie_id": 1,
        "date_publication": "Mon, 11 Jan 2021 00:00:00 GMT",
        "editeur": "Cisee",
        "id": 2,
        "isbn": "124-13",
        "titre": "Les frasques"
        },
        {
        "auteur": "Ck",
        "categorie_id": 2,
        "date_publication": "Tue, 11 Oct 2022 00:00:00 GMT",
        "editeur": "Mouuso",
        "id": 3,
        "isbn": "124-63",
        "titre": "Afrique"
        },
        {
        "auteur": "Mike",
        "categorie_id": 3,
        "date_publication": "Thu, 01 Dec 2022 00:00:00 GMT",
        "editeur": "Cissoko",
        "id": 4,
        "isbn": "24-63",
        "titre": "Histoire"
        },
        {
        "auteur": "Bouna",
        "categorie_id": 4,
        "date_publication": "Sun, 04 Sep 2022 00:00:00 GMT",
        "editeur": "Sarr",
        "id": 5,
        "isbn": "11-63",
        "titre": "Geo-politique"
        },
        {
        "auteur": "Romeo",
        "categorie_id": 5,
        "date_publication": "Sun, 01 May 2022 00:00:00 GMT",
        "editeur": "Driss",
        "id": 6,
        "isbn": "131-643",
        "titre": "Ironiquement parlant"
        },
        {
        "auteur": "Kalidou",
        "categorie_id": 5,
        "date_publication": "Thu, 01 Sep 2022 00:00:00 GMT",
        "editeur": "Moustafa",
        "id": 7,
        "isbn": "331-233",
        "titre": "La finale"
        },
        {
        "auteur": "Olimbe",
        "categorie_id": 5,
        "date_publication": "Tue, 01 Feb 2022 00:00:00 GMT",
        "editeur": "Mastapopa",
        "id": 8,
        "isbn": "311-233",
        "titre": "Les risques"
        }
        ],
        "success": true,
        "total": 8
    }
```

## GET/livres (id)

    GENERAL :
    Affiche un livre en particulier s'il existe à travers l'id fourni en paramètre. Cette route retourne : les informations sur le livre, son id; et la valeure de réussite.

    EXEMPLE : curl http://localhost:5000/livres/4
```bash
    {
    "selected_book": {
    "auteur": "Mike",
    "categorie_id": 3,
    "date_publication": "Thu, 01 Dec 2022 00:00:00 GMT",
    "editeur": "Cissoko",
    "id": 4,
    "isbn": "24-63",
    "titre": "Histoire"
    },
    "selected_id": 4,
    "success": true
    }
```

 ## GET/categories/(id)/livres

    GENERAL :
    Affiche la listes des livres appartenants à une categorie. Cette route retourne : les informations sur les livres, la valeure de réussite et le total des livres de la categorie.

    EXEMPLE : curl http://localhost:5000/categories/1/livres
```bash
    {
    "books": [
    {
    "auteur": "Ibtihadj",
    "categorie_id": 1,
    "date_publication": "Sat, 12 Feb 2022 00:00:00 GMT",
    "editeur": "KPEKPASSI",
    "id": 1,
    "isbn": "126-23",
    "titre": "Les nuages du pays"
    },
    {
    "auteur": "Oscar",
    "categorie_id": 1,
    "date_publication": "Mon, 11 Jan 2021 00:00:00 GMT",
    "editeur": "Cisee",
    "id": 2,
    "isbn": "124-13",
    "titre": "Les frasques"
    }
    ],
    "success": true,
    "total": 2
    }
```

 ## GET/categories/(id)

    GENERAL :
    Affiche les informations sur une catégorie de livres. Cette route retourne : les informations sur une catégorie, l'id de la catégorie et la valeure de réussite.

    EXEMPLE : curl http://localhost:5000/categories/2
```bash
    {
        "selected_categorie": {
            "id": 2,
            "libelle_categorie": "Conte"
        },
        "selected_id": 2,
        "success": true
    }
```



 ## DELETE/livres (id)

     GÉNÉRAL:
         Supprime le livre s'il existe. Renvoie les informations sur le livre supprimé, son id, la valeur de réussite, le nombre total de livres avant et après la suppression.

         EXEMPLE : curl -X DELETE http://localhost:5000/livres/2
```
         {
            "deleted_book": {
            "auteur": "Oscar",
            "categorie_id": 1,
            "date_publication": "Mon, 11 Jan 2021 00:00:00 GMT",
            "editeur": "Cisee",
            "id": 2,
            "isbn": "124-13",
            "titre": "Les frasques"
            },
            "deleted_id": 2,
            "success": true,
            "total_after_delete": 5,
            "total_before_delete": 6
        }

```

 ## DELETE/categories (id)

     GÉNÉRAL:
         Supprime la catégorie si elle existe. Renvoie les informations sur la catégorie supprimée, son id, la valeur de réussite, le nombre total de catégories avant et après la suppression.

         EXEMPLE : curl -X DELETE http://localhost:5000/categories/2
```
         {
            "deleted_category": {
            "id": 3,
            "libelle_categorie": "Fixion"
            },
            "deleted_id": 3,
            "success": true,
            "total_after_delete": 4,
            "total_before_delete": 5
        }

```
 
 ## PATCH/livres (id)

  ### EXEMPLE .....Patch
  ``` 
  curl -X PATCH http://localhost:5000/livres/6 -H "Content-Type:application/json" -d "{"auteur": "Kango","categorie_id": 5,"date_publication": "Sun, 01 May 2022 00:00:00 GMT","editeur": "Drissa","isbn": "131-643","titre": "Modification parlante"}"
  ```
  ```
    {
    "new_book": {
        "auteur": "Kango",
        "categorie_id": 5,
        "date_publication": "Sun, 01 May 2022 00:00:00 GMT",
        "editeur": "Drissa",
        "id": 6,
        "isbn": "131-643",
        "titre": "Modification parlant"
    },
    "success": true,
    "updated_book_id": 6
    }
```

 ## PATCH/categories (id)

  ### EXEMPLE .....Patch
  ``` 
  curl -X PATCH http://localhost:5000/categories/2 -H "Content-Type:application/json" -d "{"libelle_categorie" : "Roman"}"
  ```
  ```bash
    {
    "new_categorie": {
        "id": 2,
        "libelle_categorie": "Roman"
        },
    "success": true,
    "updated_categorie_id": 2
    }
```


## FIN ...
