from uuid import uuid4, uuid1, uuid3, uuid5
from shortuuid import ShortUUID
from nanoid import generate


IDENTIFIERS = {
    "uuid4": uuid4,
    "uuid1": uuid1,
    "uuid3": uuid3,
    "uuid5": uuid5,
    'short': ShortUUID().random,
    'nano': generate
}


def generate_identifier(identifier, length):
    return IDENTIFIERS[identifier]()
