from Tracker import Tracker
import sys

if len(sys.argv) == 2:
    file_path = str(sys.argv[1])
    tracker = Tracker(file_path)
    tracker.track()
elif len(sys.argv) == 1:
    tracker = Tracker("Config.json")
    tracker.track()
else:
    print("Error: Wrong number of arguments. Expects either none or file path to config json file.")


