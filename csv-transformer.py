import csv


def get_file_number_lines(filename):
    with open(filename) as csv_file:
        file_data = csv.reader(csv_file)
        return sum(1 for line in file_data)


def get_file_data(filename, delimiter):
    with open(filename) as csv_file:
        file_data = csv.reader(csv_file, delimiter=delimiter)

        file_header = next(file_data)

        data = []
        for line in file_data:
            item = {}
            for idx, value in enumerate(line):
                if idx < len(file_header):
                    item[file_header[idx]] = value.strip()
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
                item_converted[c[1]] = c[2]

        data_converted.append(item_converted)

    return data_converted


def data_to_table(data):
    table = []

    if len(data) == 0:
        return table

    header = data[0].keys()
    table.append(header)

    for item in data:
        line = []
        for h in header:
            line.append(item[h])
        table.append(line)

    return table


def write_file_data(filename, data):
    table = data_to_table(data)

    with open(filename, "w") as csv_file:
        file_writer = csv.writer(csv_file)
        for line in table:
            file_writer.writerow(line)


def get_conversion(filename):
    conversion = []

    with open(filename) as csv_file:
        file_data = csv.reader(csv_file)
        for line in file_data:
            conversion.append(line)

    return conversion


def main():
    data = get_file_data("data.csv", ",")
    print(data)

    conversion = get_conversion("conversion.csv")
    print(conversion)

    data_converted = data_convert(data, conversion)
    print(data_converted)

    write_file_data("data_out.csv", data_converted)


if __name__ == "__main__":
    main()
