def main():
    amount = 50
    coins = ["25", "10", "5"]
    while True:
        coin = input("Insert Coin: ")
        if coin in coins:
            amount -= int(coin)
        if amount <= 0:
            print(f"Change Owed: {abs(amount)}")
            return
        print(f"Amount Due: {amount}")

if __name__ == "__main__":
    main()