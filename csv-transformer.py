import csv


def get_file_number_lines(filename):
    with open(filename) as csv_file:
        file_data = csv.reader(csv_file)
        return sum(1 for line in file_data)


def get_file_data(filename):
    with open(filename) as csv_file:
        file_data = csv.reader(csv_file)

        file_header = next(file_data)

        data = []
        for line in file_data:
            item = {}
            for idx, value in enumerate(line):
                item[file_header[idx]] = value
            data.append(item)

        return data


if __name__ == "__main__":
    data = get_file_data("data.csv")
    print(data)
