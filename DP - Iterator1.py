# ✅ Iterator Pattern – דפוס העיצוב של איטרטור
# 📌 מה זה?
# 🔹 מאפשר לעבור על אוסף נתונים (רשימה, מילון, עץ וכו') ללא חשיפת המבנה הפנימי שלו.
# 🔹 מאפשר מעבר מותאם אישית על אלמנטים (למשל, רק מספרים זוגיים, מילים לפי אורך מסוים וכו').
# 🔹 מחלק את האחריות – הנתונים עצמם לא צריכים לדעת איך עוברים עליהם, יש מחלקה חיצונית (האיטרטור) שמנהלת את המעבר.

from collections.abc import Iterator,Iterable

class RatingIterator(Iterator):
    def __init__(self, movies):
        self.movies = [m for m in movies if m["rating"] >= 8]
        self.index = 0

    def __next__(self):
        if self.index >= len(self.movies):
            raise StopIteration
        movie  = self.movies[self.index]
        self.index += 1
        return movie

class MovieCollection(Iterable):
    def __init__(self, movies):
        self.movies = movies

    def __iter__(self):
        return RatingIterator(self.movies)

movies = [
    {"title": "Inception", "rating": 8.8},
    {"title": "Titanic", "rating": 7.8},
    {"title": "The Dark Knight", "rating": 9.0},
    {"title": "The Room", "rating": 3.7}
]


filtered_movies = MovieCollection(movies)

print("🎬 Movies with rating >= 8:")
for movie in filtered_movies:
    print(f"✅ {movie['title']} ({movie['rating']})")
