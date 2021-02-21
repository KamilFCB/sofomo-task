**Installation**

1. Execute command `docker build .`
2. Start application using `docker-compose up`
3. Install requirements in sofomo_task_web_1 container `pip install -r requirements.txt`
4. Make django models migrations executing `python manage.py makemigrations; python manage.py migrate`  in sofomo_task_web_1 container

**Usage**

After installation application works at `http://localhost:8000/geolocation/`

**Available requests**

1. POST `http://localhost:8000/login`  login with username and password equals `admin` - returns JWT token
2. POST `http://localhost:8000/geolocation/` adds IP geolocation data to database
3. GET `http://localhost:8000/geolocation/ip` returns geolocation data from database of the given IP address
4. DELETE  `http://localhost:8000/geolocation/ip` deletes geolocation data from database of the given IP address

Every requests requires passed Authorization HTTP header with value `Bearer token`, where token is value received from login request.