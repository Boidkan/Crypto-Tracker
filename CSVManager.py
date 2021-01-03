import csv

class CSVManager:

    def __createIfNeeded(titles):
        try:
            open("crypto.csv")
        except IOError:
            with open('crypto.csv', 'a+') as file:
                file_writer = csv.writer(file)
                file_writer.writerow(titles)

    def write(titles, values):
        CSVManager.__createIfNeeded(titles)
        # , newline=''
        with open('crypto.csv', 'a+') as file:
            file_writer = csv.writer(file)
            file_writer.writerow(values)




