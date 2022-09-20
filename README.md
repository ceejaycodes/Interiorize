# TITLE: Interiorize

#### VIDEO URL: [https://youtu.be/iM7rvjiRRGA]

# DESCRIPTION

##### This is a flask app that uses GeoApify APIs to enable users look for furniture stores around their location. Below are some of the routes implemented.

## App.py

#### firstly, we have the [INDEX] route which renders the homepage of the application via the GET method.

#### secondly, we have the [SHOPS] route which renders the shop page via the GET method.

#### our next route is the [SOFAS] route. Via the GET method, a form is displayed to the user where location is requested. Via the POST method, the lookup function imported from helpers.py takes in the address and returns a json list of names and locations where sofas can be bought.

#### our next route is the [CHAIRS] route. Via the GET method, a form is displayed to the user where location is requested. Via the POST method, the lookup function imported from helpers.py takes in the address and returns a json list of names and locations where chairs can be bought.

#### our next route is the [TABLES] route. Via the GET method, a form is displayed to the user where location is requested. Via the POST method, the lookup function imported from helpers.py takes in the address and returns a json list of names and locations where tables can be bought.

#### our next route is the [SHELVES] route. Via the GET method, a form is displayed to the user where location is requested. Via the POST method, the lookup function imported from helpers.py takes in the address and returns a json list of names and locations where shelves can be bought.

#### our next route is the [REGISTER] route. via the GET route, a form is displayed where the user inputs his username, email and password and also a confirm-password input. This route checks the database if the a user with same username or password exists, if it does it returns an error, if not, the user is reigstered and logged in.


#### our next route is the [LOGIN] route. Via the GET route, a form is displayed where the user inputs a username and password while the function queries the database to see if the username exists and if it has a match with the password provided.

#### our next route is the [LOGOUT] route.  only the GET route is available for this route. the current session is cleared and the index page is rendered without being logged in.


#### Our next route is the [CONTACT] route. via the GET route, a form is displayed where a name and messsage is required and via the POST route, the details inputed are inserted and stored in the database.

#### Our next route is the [ABOUT] route. this route accepts only a GET method. this route renders the about.html page.


## Helpers.py

#### The First route here is the [login_required] route. this is a route gotten from the FLASK documentation. this route decorates other functions so they can be accessed only when logged in.

#### The next route is the [LOOKUP] route. this route uses  geoapify APIS to search the longtitude and latitude of the address inputed and also use this long and lat to find places around the area with a radius of 5000m. the result is then returned.


# TEMPLATES

#### The templates folder contains all the templates used in this app. The [Layout.html] contains the basic structure of the website that is extended into other pages.




# STATIC 

#### The static folder contains all the images used. it also contains the [index.js] file that holds all the javascript files used in this app. this folder also contains the [styles.css] folder. this file has all the styling used in this app.


#### requirements.txt holds all the details of modules and isntallations used to develop this app.


# DATABASE

#### the database is stored in the [interiorize.db] file.
