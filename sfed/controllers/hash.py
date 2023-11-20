from hashlib import sha256, sha512, sha1, md5, sha224, sha384, sha3_224, sha3_256, sha3_384, sha3_512, blake2b, \
                     blake2s, shake_128, shake_256


HASH_ALGORITHM = {
    'md5': md5,
    'sha1': sha1,
    'sha256': sha256,
    'sha512': sha512,
    'sha224': sha224,
    'sha384': sha384,
    'sha3_224': sha3_224,
    'sha3_256': sha3_256,
    'sha3_384': sha3_384,
    'sha3_512': sha3_512,
    'blake2b': blake2b,
    'blake2s': blake2s,
    'shake_128': shake_128,
    'shake_256': shake_256
}


def hash_file(hash_type: str, file_path: str) -> str:
    """
    Hash a file using the given hash type.
    """
    with open(file_path, 'rb') as file:
        return HASH_ALGORITHM[hash_type](file.read()).hexdigest()


def hash_string(hash_type: str, hash_string: str) -> str:
    """
    Hash a string using the given hash type.
    """
    return HASH_ALGORITHM[hash_type](hash_string.encode('utf-8')).hexdigest()

