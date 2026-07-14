import csv

class csvReader:
    @staticmethod
    def read_csv(filepath):
        with open(filepath,mode="r",encoding="UTF-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
