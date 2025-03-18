# ✅ Flyweight Pattern – הפחתת שימוש בזיכרון ע"י שיתוף נתונים
#
# 📌 מתי משתמשים?
#
# כשיש הרבה אובייקטים דומים שגוזלים יותר מדי זיכרון.
# כשיש נתונים שחוזרים על עצמם, ואפשר לשתף אותם בין אובייקטים שונים.
# לדוגמה: טקסט במשחקים, חלקיקי שלג, דמויות במשחק, סמלים ב-IDE.

class Movie:
    def __init__(self, title):
        self.title = title

class MovieFactory:
    _movies = {}

    @staticmethod
    def get_movie(title):
        if title not in MovieFactory._movies:
            print(f"🆕 Creating new movie object: {title}")
            MovieFactory._movies[title] = Movie(title)
        else:
            print(f"♻ Using existing movie object: {title}")
        return MovieFactory._movies[title]

class MovieTicket:
    def __init__(self,movie_name,seat,price):
        self.movie = MovieFactory.get_movie(movie_name)
        self.seat = seat
        self.price = price

    def display_ticket(self):
        print(f"🎟 Ticket for {self.movie.title} | Seat: {self.seat} | Price: {self.price}$")


ticket1 = MovieTicket("Titanic", "A12", 10)
ticket2 = MovieTicket("Titanic", "A13", 10)
ticket3 = MovieTicket("Titanic", "B20", 12)
ticket4 = MovieTicket("Gold Rush", "C15" ,14)
ticket5 = MovieTicket("Gold Rush", "C16" ,14)
ticket6 = MovieTicket("Hateful Eight", "A12", 10)
ticket7 = MovieTicket("Hateful Eight", "A13", 10)
ticket8 = MovieTicket("Hateful Eight", "B20", 12)
ticket9 = MovieTicket("Hateful Eight", "C15" ,14)
ticket10 = MovieTicket("Hateful Eight", "C16" ,14)
ticket11 = MovieTicket("Hateful Eight", "B20", 12)
ticket12 = MovieTicket("Hateful Eight", "C15" ,14)
ticket13 = MovieTicket("Hateful Eight", "C16" ,14)

ticket1.display_ticket()
ticket2.display_ticket()
ticket3.display_ticket()
ticket4.display_ticket()
ticket5.display_ticket()
ticket6.display_ticket()
ticket7.display_ticket()
ticket8.display_ticket()
ticket9.display_ticket()
ticket10.display_ticket()
ticket11.display_ticket()
ticket12.display_ticket()
ticket13.display_ticket()



print(f"\n📌 Movies in memory: {list(MovieFactory._movies.keys())}")




