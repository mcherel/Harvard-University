import sys


def main():
    try:
        if len(sys.argv) < 2:
            raise Exception('Too few command-line arguments')
        if len(sys.argv) > 2:
            raise Exception('Too many command-line arguments')
        if sys.argv[1].split('.')[1] != 'py':
            raise Exception('Not a Python file')
        with open(sys.argv[1], 'r') as reader:
            # no comments
            lines = len([line.rstrip() for line in reader.readlines() if line.strip() and (line.lstrip()[0] != '#')])
            print(lines)
    except FileNotFoundError:
        sys.exit('File does not exist')
    except Exception as e:
        sys.exit(e)


if __name__ == "__main__":
    main()