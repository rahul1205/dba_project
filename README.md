# Database Administrator Project

The code in this repository is part of my work I did at Dalhousie as a database administrator under ISWEP program

### Steps to run the project

**The following steps assume that MySQL, python and pip are already installed in the machine and environment variables for their executables are set**

1. Clone the project using ```git clone <clone_url>```
2. Navigate to the repository from command line using ```cd <directory_name>```
3. Run ```pip install -r requirements.txt```
4. Create a database in mysql using either MySQL workbench or MySQL command line interface ```CREATE DATABASE DBA```
5. Navigate to settings.py under db/ directory and enter you MySQL username and password on line 83 and 84
6. From the command line, create and run migrations to create tables in the database ```python manage.py makemigrations main``` and ```python manage.py migrate```
7. Run ```python manage.py runserver``` to start the server
8. Open a new tab in browser and type localhost:8000 to check if the server is running correctly

