import sys
from PIL import Image, ImageOps


def main():

    try:
        # Check if the correct number of command-line arguments are provided
        if len(sys.argv) < 3:
            raise Exception('Too few command-line arguments')
        if len(sys.argv) > 3:
            raise Exception('Too many command-line arguments')
        extensions = ["jpg", "jpeg", "png"]
        before = sys.argv[1]
        after = sys.argv[2]
        # Check if the provided file is a
        if before.split('.')[-1] not in extensions or after.split('.')[-1] not in extensions:
            raise Exception('Invalid input')

        if before.split('.')[-1] != after.split('.')[-1]:
            raise Exception('Input and output have different extensions')

        with Image.open(before) as im1:
            with Image.open("shirt.png") as im2:
                size = im2.size
                im1 = ImageOps.fit(im1, size)
                im1.paste(im2, box = (0, 0), mask= im2)
                im1.save(after, format=None)
                # im1.show()




    # Handle exceptions
    except FileNotFoundError as e:
        sys.exit(f'Could not read {e.filename}')
    except Exception as e:
        sys.exit("Error: " + str(e))

if __name__ == "__main__":
    main()