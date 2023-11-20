from uuid import uuid4, uuid1, uuid3, uuid5
from shortuuid import ShortUUID


IDENTIFIERS = {
    "uuid4": uuid4,
    "uuid1": uuid1,
    "uuid3": uuid3,
    "uuid5": uuid5,
    'short': ShortUUID().random,
}


def generate_identifier(identifier):
    return IDENTIFIERS[identifier]()
