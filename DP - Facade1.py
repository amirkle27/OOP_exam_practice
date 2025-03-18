# 🔹 Facade הוא דפוס עיצוב מבני (Structural Pattern) שמטרתו להסתיר מערכת מסובכת מאחורי ממשק פשוט וברור.
# 🔹 זה כמו "דייל קבלה" במלון – במקום שהאורח ילך לבד לכל מחלקה (בריכה, חדר אוכל, שירות חדרים), הוא מתקשר רק עם הדייל שמנהל הכל עבורו.
# 🔹 המשתמש רואה רק את ה-Facade ולא צריך להבין איך המערכת בנויה בפנים.
#

class TV:
    def turn_on(self):
        print("📺 TV is now ON.")

    def turn_off(self):
        print("📺 TV is now OFF.")

class SoundSystem:
    def turn_on(self):
        print("🔊 Sound System is now ON.")

    def set_volume(self,volume_level):
        print(f"🔊 Setting volume to {volume_level}.")
    def turn_off(self):
        print("🔊 Sound System is now OFF.")

class Projector:
    def turn_on(self):
        print("🎥 Projector is now ON.")

    def set_input(self, source):
        print(f"🎥 Projector input source is: {source}")
    def turn_off(self):
        print("🎥 Projector is now OFF.")

class BluRayPlayer:
    def __init__(self):
        self.movie = None

    def turn_on(self):
        print("💿 Blu-ray Player is now ON.")

    def insert_disc(self,movie):
        if self.movie:
            self.eject_disc()
        print(f"💿 Inserting {movie} in Blu-ray Player")
        self.movie = movie

    def eject_disc(self,):
        if self.movie:
            print(f"💿 Ejecting {self.movie} from Blu-ray Player")
            self.movie = None
        else:
            print(f"💿 No disc in Blu-ray Player")


    def play_movie(self):
        if self.movie:
            print(f"🎬 Playing movie: {self.movie}")
        else:
            print("❌ No disc inserted! Please insert a disc first.")

    def turn_off(self):
        print("💿 Blu-ray Player is now OFF.")

class HomeTheatreFacade:
    def __init__(self):
        self.tv = TV()
        self.sound_system = SoundSystem()
        self.projector = Projector()
        self.blu_ray = BluRayPlayer()

    def watch_movie(self,movie):
        print("\n🎬 Setting up your Home Theater for movie night... 🎬")
        self.tv.turn_on()
        self.sound_system.turn_on()
        self.sound_system.set_volume(7)
        self.projector.turn_on()
        self.projector.set_input("Blu-ray")
        self.blu_ray.turn_on()
        self.blu_ray.insert_disc(movie)
        self.blu_ray.play_movie()
        print("🍿 Enjoy your movie!")


    def end_movie(self):
        print("\n🔚 Shutting down Home Theater... 🔚")
        self.blu_ray.turn_off()
        self.projector.turn_off()
        self.sound_system.turn_off()
        self.tv.turn_off()



home_theater = HomeTheatreFacade()

# צפייה בסרט ראשון
home_theater.watch_movie("Pirates of the Caribbean")


home_theater.watch_movie("Dumbo")


home_theater.blu_ray.eject_disc()


home_theater.blu_ray.play_movie()


home_theater.watch_movie("Inception")