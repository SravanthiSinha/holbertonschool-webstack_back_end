## 0x01. RESTful API - Users - endpoints
### Web Stack programming ― Back-end


0-warmup_flask.py  - A script that start a Flask application
* route : GET /  return "Holberton School"

1-warmup_flask.py - A script that start a Flask application
* route : GET /c  return "C is fun!"

2-warmup_flask.py - A script that start a Flask application with port & host from environmental variables HBNB_API_PORT, HBNB_API_HOST
* route : GET /  return "Holberton School"
* route : GET /c  return "C is fun!"

3-warmup_flask.py - A script that start a Flask application with port & host from environmental variables HBNB_API_PORT, HBNB_API_HOST
* route : GET /hbtn
```
return JSON data:
Content-Type: application/json
Representation of the dictionary: tips:
"C" = "is fun"
"Python" = "is cool"
"Sysadmin" = "is hiring"
```

api/v1/views/\__init__.py - Creates an instance of Blueprint called app_views

api/v1/views/index.py -
 * route : GET /api/v1/status
```
  Return the JSON: { "status": "OK" }
```

api/v1/app.py - Starts the Flask app


### Useful resources:
* [Rest API concept](https://intranet.hbtn.io/concepts/45)
* [Learn REST: A RESTful Tutorial](http://www.restapitutorial.com/)
* [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [Flask](http://flask.pocoo.org/)
* [Modular Applications with Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/)
