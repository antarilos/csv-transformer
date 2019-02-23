import csv


def get_file_number_lines(filename):
    with open(filename) as csv_file:
        file_data = csv.reader(csv_file)
        return sum(1 for line in file_data)


def get_file_data(filename):
    with open(filename) as csvfile:
        file_data = csv.reader(csvfile)

        for line in file_data:
            print(line)


if __name__ == "__main__":
    get_file_data("data.csv")
