from Crypto.Util.number import inverse
from utils import int_to_bytes

def compute_private_key(p, q, e):
    phi = (p - 1) * (q - 1)
    return inverse(e, phi)

def decrypt_rsa(cipher_int, d, n):
    m = pow(cipher_int, d, n)
    return int_to_bytes(m)