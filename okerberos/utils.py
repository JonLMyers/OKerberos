import base58, base64


supported_encodings = set(["base58, base64"])

def encode(message, encoding="base64"):
    """
    Arguments:
        message - A bytes string representing the object to be encoded
        encoding - the type of encoding that should be used

    return:
        a message encoded with the spceified encoding type

    """


    if encoding in supported_encodings:
        if encoding == "base58":
            return base58.b58encode(message)
        elif encoding == "base64":
            return base64.b64b64encode(message)
    else:
        raise UnsupportedEncoding






class UnsupportedEncoding(Exception):
    pass
