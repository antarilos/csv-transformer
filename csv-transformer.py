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


def data_convert(data, conversion):
    data_converted = []

    for item in data:
        item_converted = {}
        for c in conversion:
            if c[0] in item:
                item_converted[c[1]] = item[c[0]]
            else:
                print("column " + c[0] + " not found.")

        data_converted.append(item_converted)

    return data_converted


def main():
    data = get_file_data("data.csv")
    print(data)

    conversion = [("columna3", "col3"), ("columna1", "col1"), ("columna2", "col2")]
    data_converted = data_convert(data, conversion)
    print(data_converted)


if __name__ == "__main__":
    main()
