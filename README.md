# THREE IN ONE APPLICATION
A three in one application using Django.

## Features of this Project

### A. SEARCH THROUGH THE DATABASE AND GET THE USER WITH THE CORRESPONDING VALUE OF THE INPUT
- Achieved by creating API with Django Rest Framework, then performing API calls from Javascript

### B. UPLOAD SYSTEM THAT TAKES IN EXCEL/CSV FILES THAT CONTAINS INFORMATION OF USERS AND CREATING EACH OF THEM IN THE DATABASE
- When files are uploaded, users can be viewed in the search section

### C. ADVERT APPLICATION
This consists of:
- Placing adverts
- Recording the number of page views and the number of parent page to generate impression of each advert.


## Installation/Running

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Homebrew can also be used as an alternative to pip*

### Installation
**1. Create a Virtual Environment and Activate**

Install Virtual Environment
```
$  pip install virtualenv
```

Create Virtual Environment

```
$  virtualenv venv
```

Activate Virtual Environment

For Windows
```
$  cd venv\scripts&&activate
```

For Mac/Linux
```
$  source venv/bin/activate
```

**2. Navigate to the project's base directory**

**3. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```


**4. Run Server**

```python
$ python manage.py runserver
```
Server will run on `http://127.0.0.1:8000/`

### Database:
The default backend is currently set to postgreSQL, you can change to your desired database in `all_in_one/settings.py` file.