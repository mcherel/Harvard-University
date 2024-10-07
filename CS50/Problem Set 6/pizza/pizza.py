import sys
import csv
from tabulate import tabulate

def main():
    try:
        # Check if the correct number of command-line arguments are provided
        if len(sys.argv) < 2:
            raise Exception('Too few command-line arguments')
        if len(sys.argv) > 2:
            raise Exception('Too many command-line arguments')

        # Check if the provided file is a CSV file
        if sys.argv[1].split('.')[-1] != 'csv':
            raise Exception('Not a CSV file')

        # Open the CSV file and read its content
        with open(sys.argv[1], 'r') as file:
            reader = csv.reader(file)

            table = []
            for row in reader:
                table.append(row)
            # headers = table[0]
            print(tabulate(table, headers="firstrow", tablefmt="grid"))


    # Handle exceptions
    except FileNotFoundError:
        sys.exit('File does not exist')
    except Exception as e:
        sys.exit(e)

if __name__ == "__main__":
    main()