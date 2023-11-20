from base64 import b64encode, b16encode, b32encode, b85encode, b32hexencode, urlsafe_b64encode
from binascii import hexlify
from urllib.parse import quote_plus, urlencode


ENCODERS = {
    'b16': b16encode,
    'b32': b32encode,
    'b64': b64encode,
    'b85': b85encode,
    'url': urlencode,
    'hex': hexlify,
    'b32hex': b32hexencode,
    'urlsafe_b64': urlsafe_b64encode,
    'quote_plus': quote_plus
}


def encode_file(hash_type: str, input_file: str, output_file: str):
    """
    Encode a file using the given input type.
    """
    return ENCODERS[hash_type](input_file, output_file)


def encode_string(hash_type: str, input_str: str):
    """
    Encode a string using the given input type.
    """
    return ENCODERS[hash_type](input_str)