

# drf-news-api
> As a django beginer project.
---

## Features


#### news

 * News
 * Comment
---

#### Custom user
* Login
* Registration
* Passwords Change 
---

#### Name of App
* user
* news
* comment
* bone
---

#### Used Technologies
* Docker
* Python
* Django
* Django-Rest-Framework
* JWT
* PostgreSQL
* Redis
* Celery
* Postman/Insomnia 

---
## installation

#### Linux
#### Step 1
```
install Docker & Docker-compose
install virtualenv
create env
workon env
git clone https://github.com/anowar143/drf-news-api.git
pip install -r requirements.txt
```
---
#### Step 2

```
docker-compose up --build
```
---

#### Step 3

```
docker-compose exec app bash
cd src
./manage.py makemigrations
./manage.py migrate
```




