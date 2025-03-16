class StockMarket:
    def __init__(self):
        self.subscribers = []

    def subscribe(self,subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
            print(f"{subscriber.name} subscribed!")
        else:
            print(f"{subscriber.name} is already subscribed.")

    def unsubscribe(self,subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
            print(f"{subscriber.name} unsubscribed!")
        else:
            print(f"{subscriber.name} is not subscribed.")

    def notify(self,update):
        print(f"\n📢 --- Market Update --- 📢\n{update}")
        if not self.subscribers:
            print("❌ No subscribers to receive updates.")
        for subscriber in self.subscribers:
            subscriber.get_update(update)

    def show_subscribers(self):
        """ מציג את רשימת המנויים הפעילים """
        if self.subscribers:
            print("\n👥 Current Subscribers:")
            for sub in self.subscribers:
                print(f"- {sub.name}")
        else:
            print("\n❌ No active subscribers.")

class Subscriber:
    def __init__(self, name):
        self.name = name

    def get_update(self,update):
        print(f"📩 {self.name} received update: {update}")



market = StockMarket()

user1 = Subscriber("Ben")
user2 = Subscriber("Maria")
user3 = Subscriber("Jenny")
user4 = Subscriber("Tommy")
user5 = Subscriber("Daniel")

market.subscribe(user5)
market.subscribe(user2)

market.notify ("Netflix shared up 5 points!")

market.subscribe(user4)

market.notify ("Microsoft crashed 90%!")

market.subscribe(user1)
market.subscribe(user3)

market.notify ("Nvidia loses 40% value")

market.show_subscribers()

market.unsubscribe(user1)
market.unsubscribe(user2)
market.unsubscribe(user3)
market.unsubscribe(user4)
market.unsubscribe(user5)

market.notify ("Automatic StockMarked Updating System UP 90000%! All subscribers share the dividends!")

market.show_subscribers()