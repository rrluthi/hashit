from base64 import b64decode, b16decode, b32decode, b85decode, b32hexdecode, urlsafe_b64decode
from binascii import unhexlify
from typing import Dict, Callable

DECODERS:Dict[str, Callable] = {
    'b64': b64decode,
    'b16': b16decode,
    'b32': b32decode,
    'b85': b85decode,
    'hex': unhexlify,
    'b32hex': b32hexdecode,
    'urlsafe_b64': urlsafe_b64decode
}


class DecodeError(Exception):
    pass


def decode_unknown_string(input_str: str):
    """
    Attempt to decode a string using all known decoders.
    """
    for decoder in DECODERS.values():
        try:
            return decoder(input_str)
        except DecodeError:
            pass
    raise ValueError(f"Unable to decode string: {input_str}")


def decode_string(input_type: str, input_str: str):
    """
    Decode a string using the given input type.
    """
    return DECODERS[input_type](input_str)
