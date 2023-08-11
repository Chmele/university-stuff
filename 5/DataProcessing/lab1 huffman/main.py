from huffman import encode, decode


def main():
    while True:
        data = input()
        encoded, tree_root = encode(data)

        print(encoded)
        print(decode(encoded, tree_root))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit()