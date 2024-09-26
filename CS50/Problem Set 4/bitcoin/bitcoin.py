import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        coins = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if response.status_code == 200:
            data = response.json()
            # print(data)
            rate = float(data['bpi']['USD']['rate_float'])
            print(f"${(rate * coins):,.4f}", end="")
        else:
            print(response)
            response.raise_for_status()
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException as e:
        sys.exit(print(f"An error occurred: {e}"))


if __name__ == "__main__":
    main()