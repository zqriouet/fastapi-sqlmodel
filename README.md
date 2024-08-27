# Tutoriel FastAPI avec SQLModel : Création d'une API CRUD

Bienvenue dans ce tutoriel FastAPI ! Nous allons créer ensemble une API CRUD (Create, Read, Update, Delete) simple en utilisant FastAPI et SQLModel. Ce projet est parfait pour les débutants qui souhaitent apprendre les bases de FastAPI et de la gestion de base de données avec SQLModel.

## Qu'allons-nous construire ?

Nous allons créer une API pour gérer une liste d'items. Chaque item aura un nom et une description. Notre API permettra de :

- Créer un nouvel item
- Lire un ou plusieurs items
- Mettre à jour un item existant
- Supprimer un item

## Prérequis

- Python 3.7+
- Connaissance de base de Python

## Installation et configuration

1. Clonez ce dépôt :

   ```
   git clone https://github.com/zqriouet/fastapi-sqlmodel-tutorial.git
   cd fastapi-sqlmodel-tutorial
   ```

2. Créez un environnement virtuel :

   ```
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Structure du projet

Notre projet est organisé comme suit :

```
fastapi-sqlmodel-tutorial/
│   main.py
│   routes.py
│   models.py
│   database.py
│   crud.py
│   requirements.txt
│   README.md
```

- `main.py` : Point d'entrée de l'application
- `routes.py` : Définition des routes de l'API
- `models.py` : Modèles de données
- `database.py` : Configuration de la base de données
- `crud.py` : Fonctions pour les opérations CRUD

## Comprendre les composants clés

### FastAPI

FastAPI est un framework web moderne pour construire des APIs avec Python. Il est conçu pour être rapide, facile à utiliser et à apprendre.

Caractéristiques principales :

- Rapide : Hautes performances, comparable à NodeJS et Go.
- Validation automatique : Utilise Pydantic pour la validation des données.
- Documentation automatique : Génère une documentation interactive (Swagger UI) pour votre API.
- Basé sur des standards : Utilise OpenAPI (anciennement Swagger) et JSON Schema.

### SQLModel

SQLModel est une bibliothèque qui combine SQLAlchemy (pour l'ORM) et Pydantic (pour la validation des données). Elle permet de définir des modèles de données qui sont à la fois des modèles SQLAlchemy et des modèles Pydantic.

### Lifespan et gestion de la base de données

Dans `main.py`, nous utilisons un `lifespan` pour créer les tables de la base de données au démarrage de l'application :

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    from models import Item
    Item.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)
```

Cela garantit que notre base de données est correctement initialisée avant que l'application ne commence à traiter les requêtes.

### Modèles de données

Dans `models.py`, nous définissons nos modèles de données :

```python
class ItemBase(SQLModel):
    name: str
    description: Optional[str] = None

class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ItemCreate(ItemBase):
    pass
```

Ces modèles définissent la structure de nos données et comment elles seront stockées dans la base de données.

### Routes et CRUD

Les routes dans `routes.py` définissent les endpoints de notre API. Chaque route correspond à une opération CRUD :

- POST `/items/` : Créer un item
- GET `/items/{item_id}` : Lire un item spécifique
- GET `/items/` : Lire tous les items
- PUT `/items/{item_id}` : Mettre à jour un item
- DELETE `/items/{item_id}` : Supprimer un item

Les fonctions CRUD dans `crud.py` gèrent les interactions avec la base de données pour chaque opération.

## Lancement de l'application

Vous avez deux options pour lancer l'application :

1. Directement avec Python :

   ```
   python main.py
   ```

2. Avec Uvicorn (recommandé pour le développement car il offre le rechargement automatique) :
   ```
   uvicorn main:app --reload
   ```

Dans les deux cas, l'application sera accessible à l'adresse `http://localhost:8000`.

## Utilisation de l'API

1. Ouvrez votre navigateur et accédez à `http://localhost:8000/docs`.
2. Vous verrez l'interface Swagger UI qui permet de tester toutes les routes de l'API.
3. Essayez de créer un nouvel item, de le lire, de le mettre à jour et de le supprimer.

## Concepts avancés et prochaines étapes

- **Pagination** : Implémentez la pagination pour gérer de grandes quantités de données.
- **Authentification** : Ajoutez une authentification pour sécuriser votre API.
- **Tests** : Écrivez des tests pour votre API avec pytest.
- **Déploiement** : Apprenez à déployer votre application sur des plateformes comme Heroku ou AWS.

## Ressources pour aller plus loin

- [Documentation officielle de FastAPI](https://fastapi.tiangolo.com/)
- [Documentation de SQLModel](https://sqlmodel.tiangolo.com/)
- [Tutoriels FastAPI](https://fastapi.tiangolo.com/tutorial/)

N'hésitez pas à explorer le code, à expérimenter et à l'adapter à vos propres projets. Bon développement !
