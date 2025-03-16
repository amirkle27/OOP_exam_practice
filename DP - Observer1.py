# 📌 מה זה עושה?
# כאשר יש אובייקט מרכזי (נניח "חדשות"), והוא צריך להודיע לכל מי שרשום אליו (נניח "מנויים") על שינויים, ה-Observer Pattern מאפשר לנו לבנות מערכת של מנויים ומקורות מידע בצורה גמישה וניתנת להרחבה.
#
# 📌 מתי משתמשים בזה?
# ✅ כשיש אובייקט אחד שמשפיע על הרבה אחרים.
# ✅ כשלא רוצים לקבוע מראש מי יקבל עדכונים, אלא לתת אפשרות להירשם או להתנתק.
# ✅ לדוגמה: יוטיוב (Subscribe), עיתון דיגיטלי, מערכת התראות, התראות מניות בבורסה וכו'.
#

class NewsChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self,subscriber):
        self.subscribers.remove(subscriber)

    def send_news(self,news):
        print(f"\n📰 Breaking News: {news}")
        for subscriber in self.subscribers:
            subscriber.get_news(news)


class Subscriber:
    def __init__(self,name):
        self.name = name

    def get_news(self, news):
        print(f"📢 {self.name} received the following news:\n {news}")

channel = NewsChannel()

user1 = Subscriber("Anton")
user2 = Subscriber("Levy")
user3 = Subscriber("Gill")

channel.subscribe(user1)
channel.subscribe(user2)

channel.send_news("War between Israel and Gaza!")

channel.subscribe(user3)

channel.send_news("Huge tsunami is about to wipe-out Earth! ")

channel.unsubscribe(user2)
channel.unsubscribe(user1)

channel.send_news("Stock Marked crashes!")