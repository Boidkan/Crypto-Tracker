from CSVManager import CSVManager
from RequestManager import RequestManager
import sched, time, json


class Tracker:
    def __init__(self, file_path):
        self.file_path = file_path
        file = open(file_path)
        config = json.load(file)
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.timer = config["frequency_seconds"]

    def writeNewValues(self):
        file = open(self.file_path)
        config = json.load(file)
        data = RequestManager.getPrices(config)
        CSVManager.write(data[0], data[1])
        print("---------------- Added Line ----------------- ")
        print(data[0])
        print(data[1])
        self.scheduler.enter(self.timer, 1, self.writeNewValues)


    def track(self):
        self.scheduler.enter(0, 1, self.writeNewValues)
        self.scheduler.run()