import sys
from PIL import Image 


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
        extensions = ["jpg", "jpeg", "png"]
        before = sys.argv[1]
        after = sys.argv[2]
        # Check if the provided file is a CSV file
        if before.split('.')[-1] not in extensions or after.split('.')[-1] not in extensions:
            raise Exception('Invalid input')
        
        if before.split('.')[-1] != after.split('.')[-1]:
            raise Exception('Input and output have different extensions')
        
        with Image.open(before) as im:
            with Image.open("shirt.png") as im2:
                Image.Image.paste(im, im2, (200,200))
            im.show()

        """ students = []
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
        """




    # Handle exceptions
    except FileNotFoundError as e:
        sys.exit(f'Could not read {e.filename}')
    except Exception as e:
        sys.exit(e)

if __name__ == "__main__":
    main()
