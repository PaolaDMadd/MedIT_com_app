# MedIT.com app

### Description
The intent of the app is to provide a diagnosis using prediction models that will analyze the input data.

## Installation
1. Either clone or fork and clone this repository
    - `git clone <repo url>`
2. cd into the cloned repository
    - `cd MedIT_com_app`
3. Install requirements
    - `pipenv install -r requirements.txt`
4. Activate your virtual environment
    - `pipenv shell`
5. cd into project
    - `cd MedIT_com`
6. Create the user database
    - `python manage.py migrate` 
7. Start the server
    - `python manage.py runserver`
8. Open your browser and go to http://localhost:8000/ to interact with the app

## Usage 




## Technologies
* Django
* Jinja
* Sass/CSS
* pytest (integrate Django unittest)
* SqLite3
* Panda
* numpy
* sklearn


## Process

The project started with the idea of creating a useful medical app.
We initially searched a medical trained prediction model, fundamental build our app.
We created a user story and listed all minimum functionalities we wanted for our app.
We then allocated a time frame for each task outlined and logged our progress and remaining tasks.
(to be continued)

Every time a new functioning feature was completed, its branch was merged to the Development branch and pushed to the main git repository. At the end all final changes were merged with the master branch.

## Inital User Story

### Must have's 
UI
- user can create a profile 
- user can log in with autentication
- user can input data (form)

server side:
- server receives user data (eg. API call)
- server create user profile and store (model user table)
- server store user profile with data set (eg. user history table)
- server use models to analyze data received (eg. symptoms)
- server send to client side the result

## Code Snippets
```</>```

## Licence


To visit the site click this link (coming soon).