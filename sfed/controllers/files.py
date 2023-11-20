import os
import random
import struct
import string


def generate_random_file(filename: str, size_in_bytes: int = 1024):
    """
    Generate a random file of the given size.
    """
    with open(filename, 'wb') as f:
        f.write(os.urandom(size_in_bytes))


def generate_random_chunk_file(filename: str, size_in_bytes: int, chunk_size: int = 1024 * 1024):
    with open(filename, 'wb') as file:
        for _ in range(0, size_in_bytes, chunk_size):
            size_to_write = min(chunk_size, size_in_bytes - file.tell())
            file.write(struct.pack(f'{size_to_write}B', *(random.getrandbits(8) for _ in range(size_to_write))))


def generate_large_file(filename: str, size_in_bytes: int):
        chars = string.ascii_letters + string.digits
        with open(filename, 'w') as file:
            file.write(''.join(random.choice(chars) for _ in range(size_in_bytes)))
