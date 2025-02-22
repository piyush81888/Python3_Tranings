"""
Python for web development
"""

"""
In python we have many web frameworks like
- flask
- django
- fastapi
many more
"""

"""
In our training, we will discuss flask-framework 
"""

"""
Using flask-framework,
1. Using flask-framework, we can develop websites
2. Using flask-framework, we can develop REST-API
3. Using flask-framework, we can develop Microservices

We will discuss,
Using flask-framework for REST-API development
"""

"""
To understand API, let us take example

Suppose if we want to provide access to our database with others/public
then how to provide access to our database with others/public??

One option is, we can create separate credentials and we can share.
    THIS IS LIMITED OPTION
"""

"""
We got 2 solutions
1. SOAP : Simple object access protocol
2. REST : REpresentational State Transfer


both are called architectures/styles/designs

both tells introduce some interface/gate/door b/n our-app with others
It is like
our-app/db  <--INTERFACE--> others/public

both tells how to write such interface
This INTERFACE is also called as APPLICATION PROGRAMMING INTERFACE (API)

"""

"""
REST came after SOAP
REST is popular
REST is easy to implement

flask is already REST architecture,
We just need to know,
How to create REST-API using flask
"""

"""
About web server:
- we need web server to run any web application/API
- flask has builtin web server. This is SMALL server, so
    we can use it for development purpose
- Few production servers are : https://wsgi.readthedocs.io/en/latest/servers.html
"""

"""
Assume, we are planning to provide complete-access/full-access to our database
then what is complete-access/full-access means?

- Create new record
- Read existing records
- Update existing records
- Delete existing records

"""

r"""
Http Standards: HTTP methods(GET\POST\PUT\PATCH\DELETE)

- POST:         Create new record
- GET:          Read existing records
- PUT/PATCH:    Update existing records
- DELETE:       Delete existing records

"""

"""
In this release, developing REST-API
to get/read all records from our database

END POINT : http://127.0.0.1:5000/getdbdata
"""

# -------------
# Create app for rest api
# -------------
import flask
my_rest_api_app = flask.Flask(__name__) # __name__ = file name
##########################


# -------------
# END POINT : http://127.0.0.1:5000/getdbdata mapped to route("/getdbdata")
# -------------
@my_rest_api_app.route("/getdbdata", methods=["GET"])
def get_db_data_rest_api_function():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.db")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    return flask.jsonify(my_db_result)
##########################


# -------------
# Run the builtin server
# -------------
my_rest_api_app.run() # default host = '127.0.0.1', port=5000
# my_rest_api_app.run(host='', port='')
##########################
