

ENCODING_DOC = f"""
    Syntax: Encode <InputText> < {" | ".join(encoding_algos())} >
"""

DECODING_DOC = f"""
    Syntax: Decode <InputText> < {" | ".join(decoding_algos())} >
"""

HASHING_DOC = f"""
    Syntax: Hash <InputText> < {" | ".join(hashing_algos())} >
"""

HELP_DOC = """
    Usage:
		To encode/Decode:
			Encode/Decode <Text> <Algorithm>
			Encode/Decode only for help.
		To hash:
			Hash <Text> <Algorithm>
			Hash only for help.
"""