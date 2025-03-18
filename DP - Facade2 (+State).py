from abc import ABC, abstractmethod

class BluRayState(ABC):
    @abstractmethod
    def insert_disc(self, player, movie):
        pass

    @abstractmethod
    def eject_disc(self, player):
        pass

    @abstractmethod
    def play_movie(self, player):
        pass

class NoDiscState(BluRayState):
    def insert_disc(self, player, movie):
        print(f"💿 Inserting {movie} into Blu-ray Player.")
        player.movie = movie
        player.state = HasDiscState()  # ✅ מעבר למצב הבא

    def eject_disc(self, player):
        print("💿 No disc in Blu-ray Player!")  # ✅ מופיע רק כשאין דיסק

    def play_movie(self, player):
        print("❌ No disc inserted! Please insert a disc first.")  # ✅ עכשיו זה מוצג נכון

class HasDiscState(BluRayState):
    def insert_disc(self, player, movie):
        print(f"💿 Replacing current disc with {movie}.")
        player.eject_disc()  # ✅ הוצאת הדיסק הישן
        player.movie = movie  # ✅ הכנסת הדיסק החדש

    def eject_disc(self, player):
        print("💿 Ejecting disc from Blu-ray Player.")
        player.movie = None
        player.state = NoDiscState()  # ✅ חזרה למצב אין דיסק

    def play_movie(self, player):
        print(f"🎬 Playing movie: {player.movie}")
        player.state = PlayingState()  # ✅ מעבר למצב ניגון

class PlayingState(BluRayState):
    def insert_disc(self, player, movie):
        print("❌ Cannot insert a new disc while a movie is playing! Stop the movie first.")

    def eject_disc(self, player):
        print("❌ Cannot eject the disc while the movie is playing! Stop the movie first.")

    def play_movie(self, player):
        print("🎬 Movie is already playing!")

class BluRayPlayer:
    def __init__(self):
        self.state = NoDiscState()  # ✅ מתחילים בלי דיסק
        self.movie = None

    def insert_disc(self, movie):
        self.state.insert_disc(self, movie)

    def eject_disc(self):
        self.state.eject_disc(self)

    def play_movie(self):
        self.state.play_movie(self)

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

class HomeTheaterFacade:
    def __init__(self):
        self.tv = TV()
        self.sound_system = SoundSystem()
        self.projector = Projector()
        self.blu_ray = BluRayPlayer()

    def watch_movie(self, movie):
        print("\n🎬 Setting up your Home Theater for movie night... 🎬")
        self.tv.turn_on()
        self.sound_system.turn_on()
        self.sound_system.set_volume(7)
        self.projector.turn_on()
        self.projector.set_input("Blu-ray")
        self.blu_ray.insert_disc(movie)  # ✅ קודם מכניסים דיסק
        self.blu_ray.play_movie()        # ✅ ואז מפעילים את הסרט
        print("🍿 Enjoy your movie!")

    def end_movie(self):
        print("\n🔚 Shutting down Home Theater... 🔚")
        self.blu_ray.eject_disc()  # ✅ הוצאת הדיסק
        self.projector.turn_off()
        self.sound_system.turn_off()
        self.tv.turn_off()


home_theater = HomeTheaterFacade()

# צפייה בסרט ראשון
home_theater.watch_movie("Pirates of the Caribbean")

# ניסיון לנגן שוב – יגיד שהסרט כבר רץ
home_theater.watch_movie("Pirates of the Caribbean")

# סיום הסרט
home_theater.end_movie()

# ניסיון להוציא דיסק – עכשיו זה תקין
home_theater.blu_ray.eject_disc()

# הכנסת סרט חדש
home_theater.watch_movie("Dumbo")
