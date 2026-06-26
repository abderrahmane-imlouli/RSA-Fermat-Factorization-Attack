import base64

def base64_to_int(cipher_b64: str) -> int:
    data = base64.b64decode(cipher_b64)
    return int.from_bytes(data, "big")


def int_to_bytes(value: int) -> bytes:
    length = (value.bit_length() + 7) // 8
    return value.to_bytes(length, "big")