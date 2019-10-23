import json
import os 
import logging
CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR,"data","movies.json")
class Movie : 

    def __init__(self,title):
        self.title = title.title()



    def __str__(self):
        return self.title

    def _get_movies(self):
        with open (DATA_FILE, "r") as f :
            return json.load(f)

    def _write_movies(self, movies):
        with open (DATA_FILE, "w") as f :
            json.dump(movies,f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()
        if self.title not in movies :
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else :
            logging.warning(f"The movie {self.title} is already saved in the file")
            return False

    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else :
            logging.warning(f"The movie {self.title} isn't in the list")
            return False

def get_movies():
    movies_instance =[]
    with open (DATA_FILE,'r') as f :
        movies = json.load(f)
        movies_instance = [Movie(x) for x in movies]
    return movies_instance



if __name__=="__main__":
    m=Movie("le seigneur des anneaux")
    movies = get_movies()
    movies_2 = [str(x) for x in movies]
    print (movies_2)