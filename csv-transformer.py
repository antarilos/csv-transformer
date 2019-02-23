import csv


def get_file_data(filename):
    with open(filename) as csvfile:
        filedata = csv.reader(csvfile)

        for line in filedata:
            print(line)


if __name__ == "__main__":
    get_file_data("data.csv")
