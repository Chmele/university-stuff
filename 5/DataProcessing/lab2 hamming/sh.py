from operator import xor
from functools import reduce
import random


def bits(num, pad_to=0):
    res = [num >> i & 1 for i in range(num.bit_length()-1, -1, -1)]
    pad_to = pad_to if pad_to else len(res)
    return [0] * (pad_to - len(res)) + res


def to_int(bits):
    return sum(bit<<(len(bits)-i-1) for i, bit in enumerate(bits))


def flip_bit(num, pos, pad_to=0):
    num_bits = bits(num, pad_to)
    num_bits[pos] ^= 1
    return to_int(num_bits)


class HammingCodec:
    def __init__(self, n_parity_bits):
        self.n_parity_bits = n_parity_bits
        self.block_size = 2 ** n_parity_bits - 1
        self.data_size = self.block_size - n_parity_bits
    
    def encode(self, data):
        data_bits = iter(bits(data, pad_to=self.data_size))
        block = [next(data_bits) if i & (i + 1) else 0 for i in range(self.block_size)]

        set_bits_positions = [i + 1 for i, bit in enumerate(block) if bit]
        parity_bits = reversed(bits(reduce(xor, set_bits_positions, 0), pad_to=self.n_parity_bits))

        for i in range(self.n_parity_bits):
            block[2**i-1] = next(parity_bits)
        
        return to_int(block)
    
    def decode(self, data):
        block = bits(data, pad_to=self.block_size)
        set_bits_positions = [i + 1 for i, bit in enumerate(block) if bit]

        if error_pos := reduce(xor, set_bits_positions):
            block[error_pos-1] ^= 1
        
        return to_int([bit for i, bit in enumerate(block) if i & (i + 1)])


def bitstr(bits_sequence):
    return "".join([str(b) for b in bits_sequence])


def main():
    n_parity_bits = int(input("number of parity bits (>= 2): "))
    data = int(input("data in binary form: "), 2)
    
    hc = HammingCodec(n_parity_bits)
    encoded = hc.encode(data)

    print(f"Hamming code: {bitstr(bits(encoded, pad_to=hc.block_size))}")
    flipped_bit_pos = random.randint(0, hc.block_size-1)
    encoded = flip_bit(encoded, flipped_bit_pos, pad_to=hc.block_size)
    print(f"Flipped bit at position {flipped_bit_pos} in encoded data: {bitstr(bits(encoded, pad_to=hc.block_size))}")
    print(f"Restored data: {bitstr(bits(hc.decode(encoded), pad_to=hc.data_size))}")

main()