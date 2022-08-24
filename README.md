### PROJECT  NAME 
 Neighbourhood

## Description
A web application that users can sign up and enroll to various neighbourhood and see posts,alerts,businesses and social amenities in that hood.

## Author
Denis Kisavi

## BDD

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Email  | User email, ``eg johndoe@testmail.com``|
| Password  | Account password, ``eg password123``|
| Confirm Password  | Account password, ``eg password123``|

>Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  |Account username, ``eg johndoe``|
| Password  | Account password, ``eg 12345678``|

>Hood-form Inputs

| Inputs |  Description |
| :---         |          ---: |
| Avatar  |Profile picture, ``eg hfjj.jpg``|
| Bio  | Your bio, ``eg I love pets``|
| Hood  | Your neighbourhood, ``eg SpringValley``|

## User Story

- User can sign up if they have no account.

- User can login to their account.

- User should fill in hood form if it is their first time logging in.

- User can view all the posts, alerts and businesses for that hood posted by other hood members.

- User can search for businesses available in the hood based on their name.

- User can make a post, alert and a business post for other hood members to see.

- User can leave a comment on a post.

- User can rate on a business they have ever received services from.

- User can view their profile and edit their profile information.

- User can logout of the application.


## <a href="https://savyhood.herokuapp.com/">Live preview of the site</a>

## Set up instructions and installations

### Prerequisites

- python3.8

- python virtual environment ~ to create one run the following command `python3.8 -m venv --without-pip virtual`

- python pip ~ to install pip activate virtual environment `source virtual/bin/activate` then run `curl https://bootstrap.pypa.io/get-pip.py | python`

- Postgres ~ to install follow the following commands in your home directory:
    - `sudo apt-get update`
    - `sudo apt-get install postgresql postgresql-contrib libpq-dev`
    - `sudo service postgresql start`
    - `sudo -u postgres createuser --superuser $USER`
    - `sudo -u postgres createdb $USER`
    - `touch .psql_history`

### Installation instructions

- Clone the repo ~ `https://github.com/Kisavi/Neighbourhood-clone.git`

- Activate virtual environment: 
   `python3.6 -m venv --without-pip virtual` then `source virtual/bin/activate`

- Install all the dependancies in the requirements.txt file to get a development env running
   `pip3 install -r requirements.txt`

- Create a database 
  ```bash
  psql
  CREATE DATABASE 'your database name';
  ```

- Create .env file and paste the following filing where appropriate:
  ```python
  SECRET_KEY = '<Secret_key>'
  DBNAME = '<your db name>'
  USER = '<Username>'
  PASSWORD = '<password>'
  DEBUG = True
  ```

- Run initial migration
  ``` bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Run the app

   - `python3 manage.py runserver`

- Open the `localhost:8000` to check if the app is running successfully.

## Development
#### Want to make a contribution to enhance an existing module or fix a bug? Great!
* Fork the repo
* Create a new branch (git checkout -b improve-feature)
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes (git commit -am 'Improve feature')
* Push to the branch (git push origin improve-feature)
* Create a Pull Request

## Technologies used

    - python3.8
    - Django4.0.4
    - Bootstrap
    - Postgresql

## Known Bugs
No known bugs at the time deployement was done.
#### 
If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
## Contact Information
* For any inqueries feel free to write to me through
  + deniskisavi@gmail.com

## Licence
* MIT License
* Copyright (c) 2022 Denis Kagunda






