from enum import Enum
from datetime import datetime


class MovieType(Enum):
    ACTION = 1
    COMEDY = 2
    DRAMA = 3
    FANTASY = 4
    HORROR = 5


class Movie:
    def __init__(self, id, title, ranking, release_date, character_number, ticket_price, comment, movie_type):
        self.id = id
        self.title = title
        self.ranking = ranking
        self.release_date = release_date
        self.character_number = character_number
        self.ticket_price = ticket_price
        self.comment = comment
        self.movie_type = movie_type

    def __del__(self):
        print(f"Movie {self.title} is deleted")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value < 0:
            raise ValueError("ID не може бути від’ємним")
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Назва фільму не може бути пустою")
        self._title = value

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, value):
        if not (0 <= value <= 10):
            raise ValueError("Рейтинг має бути від 0 до 10")
        self._ranking = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        if isinstance(value, str):
            value = datetime.strptime(value, "%Y-%m-%d")
        self._release_date = value

    @property
    def character_number(self):
        return self._character_number

    @character_number.setter
    def character_number(self, value):
        if value < 0:
            raise ValueError("Кількість персонажів не може бути від’ємною")
        self._character_number = value

    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        if value < 0:
            raise ValueError("Ціна квитка не може бути від’ємною")
        self._ticket_price = value

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def movie_type(self):
        return self._movie_type

    @movie_type.setter
    def movie_type(self, value):
        if not isinstance(value, MovieType):
            raise ValueError("movie_type має бути MovieType enum")
        self._movie_type = value

    def __str__(self):
        date_str = self.release_date.strftime("%Y-%m-%d")
        return f"[{self.id}] {self.title} ({date_str}) - {self.movie_type.name}, ranking {self.ranking}"


class Cinema:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self._movies = []

    def __del__(self):
        print(f"Cinema {self.name} is deleted")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Назва кінотеатру не може бути пустою")
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not value:
            raise ValueError("Локація не може бути пустою")
        self._location = value

    @property
    def movies(self):
        return self._movies

    def add_movie(self, movie):
        if not isinstance(movie, Movie):
            raise TypeError("Можна додавати лише Movie")
        self._movies.append(movie)

    def remove_movie(self, movie_id):
        self._movies = [m for m in self._movies if m.id != movie_id]

    def calculateProfit(self, movies, day):
        total = 0
        for movie in movies:
            total += movie.ticket_price * day
        return total

    def choose_movie(self):
        return max(self._movies, key=lambda m: m.ranking)

    def sort_by_release_date(self):
        self._movies.sort(key=lambda m: m.release_date)

    def show_movies(self):
        for m in self._movies:
            print(m)


if __name__ == "__main__":
    cinema = Cinema("Multiplex", "Lviv")

    mov1 = Movie(1, "Interstellar", 9.0, "2014-11-07", 4, 150, "Legendary", MovieType.FANTASY)
    mov2 = Movie(2, "Joker", 8.8, "2019-10-04", 3, 120, "Dark", MovieType.DRAMA)
    mov3 = Movie(3, "Avatar 2", 7.9, "2022-12-16", 8, 200, "Blockbuster", MovieType.ACTION)
    mov4 = Movie(4, "Scream", 7.4, "1996-12-20", 7, 152, "Blood", MovieType.HORROR)

    cinema.add_movie(mov1)
    cinema.add_movie(mov2)
    cinema.add_movie(mov3)
    cinema.add_movie(mov4)

    cinema.show_movies()
    cinema.sort_by_release_date()
    print(cinema.choose_movie())
    print(cinema.calculateProfit(cinema.movies, 100))
