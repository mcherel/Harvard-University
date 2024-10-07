import sys
import csv
# pip install tabulate

def main():
    """
    Program that needs two argumets 'before.csv' and 'after.csv'
    reorganises the two column csv file into three column csv file  
    """
    try:
        # Check if the correct number of command-line arguments are provided
        if len(sys.argv) < 3:
            raise Exception('Too few command-line arguments')
        if len(sys.argv) > 3:
            raise Exception('Too many command-line arguments')

        # Check if the provided file is a CSV file
        if sys.argv[1].split('.')[-1] != 'csv':
            raise Exception('Not a CSV file')

        students = []
        # Open the CSV file and read its content
        with open(sys.argv[1], 'r') as file:
            # reading csv file
            reader = csv.reader(file)
            # creating a new list of dicts
            for name, house in [row for row in reader][1:]:
                students.append({"first": name.split(", ")[1], "last": name.split(",")[0], "house": house})
        # writing a new file
        with open(sys.argv[2], 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["first", "last", "house"])
            for student in students:
                writer.writerow([student["first"], student["last"], student["house"]])





    # Handle exceptions
    except FileNotFoundError as e:
        sys.exit(f'Could not read {e.filename}')
    except Exception as e:
        sys.exit(e)

if __name__ == "__main__":
    main()
