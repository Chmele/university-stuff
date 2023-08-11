from math import log, exp, ceil


class BloomFilter:
    def __init__(self, n_items, false_positive_prob=0.01):
        self.n_bits = ceil(-n_items * log(false_positive_prob) / (log(2) ** 2))
        self.bit_array = [0] * self.n_bits
        self.max_n_items = n_items
        self.n_items = 0
        self.n_hashes = ceil(log(2) * self.n_bits / n_items)
    
    @classmethod
    def from_iterable(cls, items, false_positive_prob=0.01):
        items_set = set(items)
        bloom_filter = cls(len(items_set), false_positive_prob)
        
        for item in items_set:
            bloom_filter.add(item)
        
        return bloom_filter

    def add(self, item):
        if self.n_items == self.max_n_items:
            raise ValueError(f"Capacity exceeded")

        for i in range(self.n_hashes):
            index = hash((item, i)) % len(self.bit_array)
            self.bit_array[index] = 1
        
        self.n_items += 1
    
    def __contains__(self, item):
        return all(
            self.bit_array[hash((item, i)) % len(self.bit_array)]
            for i in range(self.n_hashes)
        )
    
    def false_positive_prob(self):
        return (1 - exp(-self.n_hashes * self.n_items / len(self.bit_array))) ** self.n_hashes
    

def input_value(message, type, condition):
    value = None
    while value is None or not condition(value):
        value = input(message)
    
    return type(value)


def main():
    false_positive_prob = input_value("false positive probability in a Bloom filter: ", float, lambda v: v.replace(".", "", 1).isdigit() and 0 < float(v) < 1)
    n_items = input_value("number of items in a Bloom filter: ", int, lambda v: v.isdigit() and int(v) > 0)
    
    bloom_filter = BloomFilter(n_items, false_positive_prob)

    items = set()
    for i in range(n_items):
        item = input_value(f"{i+1}: ", str, lambda v: v not in items)
        bloom_filter.add(item)
        items.add(item)
    
    print(f"Filled the {bloom_filter.n_bits}-bit Bloom filter with items: {items}\n")

    while True:
        item = input("Check item: ")

        if item in bloom_filter:
            print(f"contains {item} with probability {1-bloom_filter.false_positive_prob():.2%}\n")
        else:
            print(f"doesn't contain {item} with 100% probability\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit()