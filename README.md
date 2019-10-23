PyMovie, save your filmography
=================                                                      
![UI PyMovie](/images/UI.png)                 

Why this program? 
-----------------                                                                    
With this program, you can save it from the list of movies you have viewed with the GUI, simple. The skills mobilized for the realization of this application:                                                                                                                                                                   
* Read and understand a module documentation                                        
* Manage different versions of Python and its modules according to projects                                                  
* Use an algorithm to solve a technical need                                       
* Code effectively using the right tools                                          
* Conceptualize the whole of its application by describing its structure (Entities / Domain Objects) 
* Use **PySide 2** for the UI, **Pipenv**.

How does it work ? 
-------------------
To start use **clone or download** button on github and **Download ZIP** on your computer, or copy HTTPS link and use the terminal on your computer and type : 
```
$ git clone https://github.com/GuillaumeStaub/PyMovie.git
```
Check if python 3 is installed on your machine. For this, open the terminal and type : 
```
$ python3 -V
```
You have to get something like : 
```
Python 3.X.X
```
If python is not installed on your machine go to the site: [https://www.python.org](https://www.python.org), download **Python 3.X.X** and follow the instructions. 

If you are Linux user you can install Python from the console with the command : `$ sudo apt-get install python3`

If you are MacOS user you can use [MacPorts](https://www.macports.org) and install Python from the terminal with the command : `$ sudo port install python3`

Or you can use too [HomeBrew](https://brew.sh) from the terminal with the command : `$ brew install python3`

### ![windows](https://img.icons8.com/color/48/000000/windows-logo.png) For Windows users :

1. Open the console and navigate to the root of the project PyMovie with the commande `$ cd\...\PyMovie`
2. Check that pipenv is installed on your machine with `$ pipenv --version` if the answer is `pipenv, version 2018.XX.XX` it's ok.  If not install pipenv with the command `$ pip install pipenv`
3. To start the PyMovie App type the following command from the root of the project : 
```
$ pipenv run python app.py
```


### ![apple](https://img.icons8.com/dusk/48/000000/mac-os.png) For MacOs users : 

You can try the same things WIndows users:

1. Open the console and navigate to the root of the project PyMovie with the commande `$ cd\...\PyMovie`
2. Check that pipenv is installed on your machine with `$ pipenv --version` if the answer is `pipenv, version 2018.XX.XX` it's ok.  If not install pipenv with the command `$ pip install pipenv`
3. To start the PyMovie App type the following command from the root of the project : 
```
$ pipenv run python app.py
```

### ![linux](https://img.icons8.com/color/48/000000/linux.png) For Linux  or other Unix users :

You can try the same things WIndows users:

1. Open the console and navigate to the root of the project PyMovie with the commande `$ cd\...\PyMovie`
2. Check that pipenv is installed on your machine with `$ pipenv --version` if the answer is `pipenv, version 2018.XX.XX` it's ok.  If not install pipenv with the command `$ pip install pipenv`
3. To start the PyMovie App type the following command from the root of the project : 
```
$ pipenv run python app.py
```

Contribute to the program
--------------------------                                                            
                                                                                              
* Fork it                                                                           
* Create your feature branch (git checkout -b my-new-feature)                             
* Commit your changes (git commit -am 'Add some feature')                                 
* Push to the branch (git push origin my-new-feature)                                     
* Create new Pull Request      



Next Versions
--------------------------   
* Ability to rate movies
* Possibility to leave a comment on the movie
* Integration of The Movie Database API to select movies in a list with filters
* Movie summary display and general information(year, director)
* Display of the movie poster
