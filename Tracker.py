from CSVManager import CSVManager
from RequestManager import RequestManager
import sched, time, json


class Tracker:
    def __init__(self, file_path):
        file = open(file_path)
        self.config = json.load(file)

        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.timer = self.config["frequency_seconds"]
        print(file_path)
        print(self.config)

    def writeNewValues(self):
        data = RequestManager.getPrices(self.config)
        CSVManager.write(data[0], data[1])
        print("---------------- Added Line ----------------- ")
        print(data[0])
        print(data[1])
        self.scheduler.enter(self.timer, 1, self.writeNewValues)


    def track(self):
        self.scheduler.enter(0, 1, self.writeNewValues)
        self.scheduler.run()