# AirBnB clone - The console

## Introduction
HBNB project is the first step to create a RBNB clone. We implemented console to handle different case we use in back as create or show some instance

## Features
- cmd 'help' is implementt automatically in the systeme by import cmd

#### Basics commands in console
- The cmd 'quit' leave the shell
- L'OEF is handle
- And the emptyline (enter)

#### interact with the back
- The cmd 'create' do the creation of an instance
- The cmd 'show' display the instance by the ID
- The cmd 'destroy' delete the instance target by ID
- The cmd 'all' display all the current instances
- The cmd 'update' change or add/append attribute target

## Requirements
General

-   Allowed editors: vi, vim, emacs, VScode
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly #!/usr/bin/python3
-   A README.md file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version 2.7.*)
-   All your files must be executable
-   The length of your files will be tested using wc
-   All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
-   All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
-   All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' -and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it - will be verified)

## More info
#### Syntax:
- cmd help: help or help cmd
- cmd quit: quit
- cmd create: create class name
- cmd show: show class name id (copy/paste)
- cmd destroy: destroy class name id (copy/paste)
- cmd all: all 'OR' all class name
- cmd update: update class name id attribute name "attribute value"

## Examples and testing
### help
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
### quit
```
(hbnb) quit
ida@IDA:~/holbertonschool-AirBnB_clone$
```

### help quit
```
(hbnb) help quit
Quit command to exit the program
(hbnb)
```
### create
```
(hbnb) create BaseModel
1de133d1-0377-4a3f-b1af-e4d9d671de1f
(hbnb)
```
### show
```
(hbnb) show BaseModel 1de133d1-0377-4a3f-b1af-e4d9d671de1f
[BaseModel] (1de133d1-0377-4a3f-b1af-e4d9d671de1f) {'id': '1de133d1-0377-4a3f-b1af-e4d9d671de1f', 'created_at': datetime.datetime(2023, 11, 3, 13, 52, 31, 310121), 'updated_at': datetime.datetime(2023, 11, 3, 13, 52, 31, 310125)})
(hbnb)
```

### destroy
```
(hbnb) destroy BaseModel 1de133d1-0377-4a3f-b1af-e4d9d671de1f
(hbnb) show BaseModel 1de133d1-0377-4a3f-b1af-e4d9d671de1f*
** no instance found **
(hbnb)
```

## AUTHORS
#### Xavier Bertin
- Github: https://github.com/Erkenoss

#### Yoann Rivet
- Github: https://github.com/SpStigma
