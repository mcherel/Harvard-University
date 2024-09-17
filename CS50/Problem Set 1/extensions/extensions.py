def main():
    s = input("File name: ").lower().strip().split(".")
    l = len(s)
    if l < 2:
        print("application/octet-stream")
        return
    match s[l-1]:
        case "gif" | "jpg" | "jpeg" | "png":
            print(f"image/{s[l-1].replace('jpg', 'jpeg')}")
        case "pdf" | "zip":
            print(f"application/{s[l-1]}")
        case "txt":
            print(f"text/{s[0]}")
        case _:
            print("application/octet-stream")

if __name__ == "__main__":
    main()
