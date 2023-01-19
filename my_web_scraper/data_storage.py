import csv

class DataStorage:
    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def to_csv(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            fieldnames = self.data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)
