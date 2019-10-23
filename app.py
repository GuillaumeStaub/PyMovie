from PySide2 import QtWidgets, QtCore
from movie import get_movies, Movie

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyMovie")
        self.setup_ui()
        self.set_default_values()
        self.setup_connections()



    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.enter_movie = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton("Ajouter un Film")
        self.list_movies = QtWidgets.QListWidget()
        self.list_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_del_movie = QtWidgets.QPushButton("Supprimer le(s) film(s)")


        self.layout.addWidget(self.enter_movie)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.list_movies)
        self.layout.addWidget(self.btn_del_movie)

    def set_default_values(self):
        movies = get_movies()
        for movie in movies:
            lw_item=QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole,movie)
            self.list_movies.addItem(lw_item)
        
    def setup_connections(self):
        self.enter_movie.returnPressed.connect(self.add_movie)
        self.btn_add_movie.clicked.connect(self.add_movie)
        self.btn_del_movie.clicked.connect(self.remove_movie)

    def add_movie(self):
        movie_title = self.enter_movie.text()
        if not movie_title : 
            return False
        movie = Movie(movie_title)
        resultat = movie.add_to_movies()
        if resultat:
            lw_item=QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole,movie)
            self.list_movies.addItem(lw_item)
        
        self.enter_movie.setText("")
    


    def remove_movie(self):
        for selected_item in self.list_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.list_movies.takeItem(self.list_movies.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()