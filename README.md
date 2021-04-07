# Django REST API and Serializers Demonstration

Loosely following along with https://bezkoder.com/django-rest-api/, I was able to create a short Django project that demonstrates the REST API and the Model Serializers. Migration data has been provided to create 3 unique `Tutorial` objects, and allow them to be accessed.

## Start Up
Startup the docker container with `docker-compose up` to start the project. Then, run `docker exec -ti restapiexample_web_1 bash` in a new shell instance to login to the container to run `python manage.py migrate`, which will populate the project with sample data.

## Migration Data
```python
Tutorial(
  title="One",
  description="Some description",
  published=True
)
Tutorial(
  title="Two",
  description="Some description",
  published=False
)
Tutorial(
  title="Three",
  description="Some description",
  published=True
)
```

## Accessing The Data

This data is visible with a simple `GET` request to [http://localhost:8000/api/tutorial](http://localhost:8000/api/tutorial). This will return JSON that is the 3 given tutorial objects. This link can also take a `POST` request that will generate a new tutorial object on the database that is accessible through the link above, or directly at `/api/tutorial/<int:id>`.

The following URLs will accept the following requests.
```
/api/tutorial : GET, POST, DELETE
/api/tutorial/<int:id> : GET, PUT, DELETE
/api/tutorial/published : GET
```

Use the `curl` command line application to test this out.

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"title":"NewTitle", "description":"SomeDesc"}' http://localhost:8000/api/tutorial
```

The above command will post a new object with the title "NewTitle" and description "SomeDesc". This will send a POST request to `[HOST]/api/tutorial` to achieve this.

Modifying this command to be `curl -X DELETE http://localhost:8000/api/tutorial` will delete *all* tutorial objects.

Similarly, one can read (`GET`), modify (`PUT`), and delete existing objects with `/api/tutorial/<int:id>`. One can also `GET` all published objects at `/api/tutorial/published`.

## Where The Magic Happens

The magic happens in two main parts.

First, the `apiexample/tutorial/views.py` file has the views defined that allow us to actually communicate with the URLs. These views utilize the `rest_framework.decorators` attribute [`@api_view` (see more)](https://www.django-rest-framework.org/api-guide/views/#api_view) which allows one to specify the type of requests a view will handle.

The second place where magic happens is in `apiexample/tutorial/serializers.py`. This file has a self defined [Model Serializer (See More)](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer) that allows one to *easily* parse an existing Django Model into JSON data. This is how we convert a `Tutorial` model into the JSON, and convert JSON into a `Tutorial` model. Check the `POST` request in the `tutorial.views.tutorial_list`function to see how to convert given JSON into a `Tutorial` model.  
