# Computer-Vision-Project
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25_grey.gif" border="0" alt="Made with Django." title="Made with Django." /></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-360/)

## Getting started

### Prerequisites

in order to run this project you need to take few steps which its listed below

#### install python on your system
1)python 3.7
```
$ sudo apt-get update
$ sudo apt-get install python3.7
```
2)pip
```
$ sudo apt install python3-pip
```

<!-- Running the Project Locally -->
### Running the Project Locally
First, clone the repository to your local machine:

Create the database 
* Notice that you must run these command in you IDE terminal in the exact
order listed below!

###windows:
```
1. py manage.py makemigrations registerApp

2. py manage.py migrate registerApp 

3. py manage.py makemigrations userApp

4. py manage.py migrate userApp

5. py manage.py makemigrations taradodApp

6. py manage.py migrate taradodApp

7. py manage.py makemigrations 

8. py manage.py migrate

```
Finally, run the development server
```
$ py manage.py runserver
```

###linux:
* use either python3 or python(in the beginning of the commands) depending on
 whether which of them works for your system

```
1. python3 manage.py makemigrations registerApp

2. python3 manage.py migrate registerApp 

3. python3 manage.py makemigrations userApp

4. python3 manage.py migrate userApp

5. python3 manage.py makemigrations taradodApp

6. python3 manage.py migrate taradodApp

7. python3 manage.py makemigrations 

8. python3 manage.py migrate

```
Finally, run the development server
```
$ python3 manage.py runserver
```



<!-- ROADMAP -->
## Roadmap

See the [Network graph](https://github.com/TheMn/internet-engineering-project/network) for timeline of the most recent commits to this repository and its network ordered by most recently pushed to.

<!-- CONTACT -->
## Contributers
* [@asal97](https://github.com/asal97) Asal Asgari 
* [@TheMn](https://github.com/TheMn) Amirhossein Mahdinejad

[contributors-shield]: https://img.shields.io/github/contributors/asal97/Computer-Vision-Project?style=flat-square
[contributors-url]: https://github.com/asal97/Computer-Vision-Project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/asal97/Computer-Vision-Project?style=flat-square
[forks-url]: https://github.com/asal97/Computer-Vision-Project/network/members
[stars-shield]: https://img.shields.io/github/stars/asal97/Computer-Vision-Project?style=flat-square
[stars-url]: https://github.com/asal97/Computer-Vision-Project
