import emoji

def main():
    #print(emoji.EMOJI_DATA['👍'])
    print("Output:", emoji.emojize(input("Imput: ")
                                   .replace('thumbsup', 'thumbs_up')
                                   .replace('earth_asia', 'globe_showing_Asia-Australia')
                                   .replace('earth_americas', 'globe_showing_Americas')
                                   .replace('earth_africa', 'globe_showing_Europe-Africa')))


if __name__ == "__main__":
    main()
