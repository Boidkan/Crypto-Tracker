from CSVManager import CSVManager
from RequestManager import RequestManager
import sched, time, json


class Tracker:
    file = open("Config.json")
    config = json.load(file)

    scheduler = sched.scheduler(time.time, time.sleep)
    timer = config["frequency_seconds"]

    def writeNewValues(self):
        data = RequestManager.getPrices()
        CSVManager.write(data[0], data[1])
        print("---------------- Added Line ----------------- ")
        print(data[0])
        print(data[1])
        self.scheduler.enter(self.timer, 1, self.writeNewValues)


    def track(self):
        self.scheduler.enter(0, 1, self.writeNewValues)
        self.scheduler.run()