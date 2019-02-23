import csv


def get_file_data(filename):
    with open(filename) as csvfile:
        file_data = csv.reader(csvfile)

        for line in file_data:
            print(line)


if __name__ == "__main__":
    get_file_data("data.csv")
