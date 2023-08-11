from bloom import BloomFilter


def input_value(message, type, condition):
    value = None
    while value is None or not condition(value):
        value = input(message)
    
    return type(value)


def main():
    print("---Bloom filter demo by (c) artandfi---")

    false_positive_prob = input_value("Enter the desired false positive probability in a Bloom filter: ", float, lambda v: v.replace(".", "", 1).isdigit() and 0 < float(v) < 1)
    n_items = input_value("Enter the number of items in a Bloom filter: ", int, lambda v: v.isdigit() and int(v) > 0)
    
    bloom_filter = BloomFilter(n_items, false_positive_prob)

    items = set()
    for i in range(n_items):
        item = input_value(f"Enter item {i+1}: ", str, lambda v: v not in items)
        bloom_filter.add(item)
        items.add(item)
    
    print(f"Filled the {bloom_filter.n_bits}-bit Bloom filter with items: {items}\n")

    while True:
        item = input("Check if the Bloom filter contains an item: ")

        if item in bloom_filter:
            print(f"The Bloom filter contains {item} with probability {1-bloom_filter.false_positive_prob():.2%}\n")
        else:
            print(f"The Bloom filter doesn't contain {item} with 100% probability\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit()