import csv
from datetime import datetime
from operator import itemgetter

sorted_list = []
list_of_bottles = []


def test_write_csv():
    with open("test.csv", "w", newline= '', encoding='utf-8') as csvfile:
        fields = ["Wine Name", "Year", "Varietal", "Country", "Region", "Sub-Region", "Type", "Size", "Availability", "Price", "Sale Price", "CT Link"]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        
        writer.writerow({"Wine Name": f"Created at {datetime.now()}"})
        writer.writeheader()
        for a in list_of_bottles:
            writer.writerow(a)


def test_read_csv():
    with open("test.csv", newline="", encoding='utf-8')as csvfile:
        reader = csv.DictReader(csvfile)
        unordered_list_of_bottles = []
        for row in reader:
            unordered_list_of_bottles.append(row)
        
        sorted_list = sorted(unordered_list_of_bottles, key= itemgetter("Year"))
        for row in sorted_list:
            list_of_bottles.append(row)




def main():
    test_read_csv()
    test_write_csv()



if __name__ == "__main__":
    main()
