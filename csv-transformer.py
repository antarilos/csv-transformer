import csv
import argparse


class CsvTransformer():

    def __init__(self, input_filename, output_filename, conversion_filename, input_delimiter, encoding):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.conversion_filename = conversion_filename
        self.input_delimiter = input_delimiter
        self.encoding = encoding

    def get_file_data(self):
        with open(self.input_filename, encoding=self.encoding) as csv_file:
            file_data = csv.reader(csv_file, delimiter=self.input_delimiter)

            file_header = next(file_data)

            data = []
            for line in file_data:
                item = {}
                for idx, value in enumerate(line):
                    if idx < len(file_header):
                        item[file_header[idx]] = value.strip()
                data.append(item)

            return data

    @staticmethod
    def data_convert(data, conversion):
        data_converted = []

        for item in data:
            item_converted = {}
            for c in conversion:
                if c[0] in item:
                    if c[2] == "*":
                        item_converted[c[1]] = item[c[0]].title()
                    else:
                        item_converted[c[1]] = item[c[0]]
                else:
                    item_converted[c[1]] = c[2]

            data_converted.append(item_converted)

        return data_converted

    @staticmethod
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

    def write_file_data(self, data):
        table = self.data_to_table(data)

        with open(self.output_filename, "w", encoding=self.encoding) as csv_file:
            file_writer = csv.writer(csv_file)
            for line in table:
                file_writer.writerow(line)

    def get_conversion(self):
        conversion = []

        with open(self.conversion_filename, encoding=self.encoding) as csv_file:
            file_data = csv.reader(csv_file)
            for line in file_data:
                conversion.append(line)

        return conversion

    def do(self):
        data = self.get_file_data()
        print(data)

        conversion = self.get_conversion()
        print(conversion)

        data_converted = self.data_convert(data, conversion)
        print(data_converted)

        self.write_file_data(data_converted)


def main():
    parser = argparse.ArgumentParser(description="Converts CSV files.")
    parser.add_argument("input",
                        help="Input file name to be converted.")
    parser.add_argument("output",
                        help="Output file name to store the conversion.")
    parser.add_argument("conversion",
                        help="Input file name from where the conversion description is read.")
    parser.add_argument("-d", "--delimiter",
                        help="Delimiter character to be used to split the CSV columns (default ',').",
                        default=",")
    parser.add_argument("-e", "--encoding",
                        help="Files encoding (default ISO-8859-1).",
                        default="ISO-8859-1")

    args = parser.parse_args()

    csv_transformer = CsvTransformer(args.input, args.output, args.conversion, args.delimiter, args.encoding)
    csv_transformer.do()


if __name__ == "__main__":
    main()
