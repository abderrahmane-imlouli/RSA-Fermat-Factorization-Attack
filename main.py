from factor import fermat_factor
from decrypt import compute_private_key, decrypt_rsa
from utils import base64_to_int

# Example RSA parameters (educational only)

n = 3721858881295543081285872501620915771673073750948606949477691843085904864686971044694857963652852487780555407019653940289080952098704248670349198624939889

e = 65537

cipher_b64 = "Jf2+/nhRcDRcS3MguodaskZKiPpAIr0fzyZZ8xJQUNwpXquxxHosxJR5AnPemvd52xIcWKpgQihA82O7kUDTzA=="

print("[+] Factoring modulus...")
p, q = fermat_factor(n)

print("[+] p =", p)
print("[+] q =", q)

print("[+] Computing private exponent...")
d = compute_private_key(p, q, e)

cipher_int = base64_to_int(cipher_b64)

print("[+] Decrypting...")
plaintext = decrypt_rsa(cipher_int, d, n)

print("\nRecovered bytes:")
print(plaintext)

try:
    print("\nRecovered text:")
    print(plaintext.decode())
except UnicodeDecodeError:
    print("\nPlaintext is not valid UTF-8.")