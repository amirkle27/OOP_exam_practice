# לפעמים יש לנו שני קודים שלא תואמים אחד לשני –
# 🔹 למשל, מערכת חדשה שרוצה להשתמש בקוד ישן, אבל הפורמט לא תואם.
# 🔹 במקום לשנות את הקוד הישן – פשוט עוטפים אותו באדפטר (מתאם)!
# 🔹 זה כמו מתאם לחשמל – מחבר בין תקע אירופאי לשקע אמריקאי.
#
# 🚀 איך בונים את Adapter Pattern?
# ✅ שלב 1 – נגדיר מחלקה ישנה שלא תואמת למערכת החדשה.
# ✅ שלב 2 – נגדיר מחלקה חדשה שרוצה להשתמש בקוד הישן.
# ✅ שלב 3 – נבנה Adapter שמגשר בין השניים!
#

# 🕹️ מחלקה ישנה - מחזירה נתוני שחקן בפורמט ישן
class OldGameSystem:
    def get_player_info(self):
        return {"name": "Mario", "score": 9999}

# 🎮 מחלקה חדשה - רוצה לקבל נתונים בצורה שונה
class NewGameSystem:
    def show_player_data(self, name, score):
        print(f"🎖️ Player: {name}, Score: {score}")

# 🔌 ADAPTER - מתאם בין המערכת הישנה לחדשה
class GameAdapter:
    def __init__(self, old_game):
        self.old_game = old_game

    def get_adapted_data(self):
        data = self.old_game.get_player_info()
        return data["name"], data["score"]

# 💡 שימוש:
old_game = OldGameSystem()
adapter = GameAdapter(old_game)
new_game = NewGameSystem()

# מחברים בין הישן לחדש:
name, score = adapter.get_adapted_data()
new_game.show_player_data(name, score)
