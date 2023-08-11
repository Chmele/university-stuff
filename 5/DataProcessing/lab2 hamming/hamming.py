from functools import reduce
from operator import xor


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