# RSA Fermat Factorization Attack Demonstration

An educational Python project demonstrating how RSA can become vulnerable when the modulus `n` is generated from two prime factors that are unusually close together.

The repository walks through the complete process of:

* Factoring the RSA modulus using Fermat's factorization method.
* Recovering the private exponent.
* Decrypting an RSA ciphertext.
* Understanding why proper prime generation is essential for RSA security.

## Features

* Educational implementation of Fermat factorization.
* Base64 ciphertext decoding.
* Automatic recovery of RSA private parameters after successful factorization.
* RSA decryption using the recovered private key.
* Clean and modular Python code suitable for learning and experimentation.

## Project Structure

```text
.
├── factor.py          # Fermat factorization implementation
├── decrypt.py         # Private key computation and RSA decryption
├── utils.py           # Helper functions
├── main.py            # Demonstration script
├── requirements.txt
└── README.md
```

## Requirements

* Python 3.10+
* pycryptodome

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the demonstration:

```bash
python main.py
```

The script will:

1. Factor the RSA modulus using Fermat's method.
2. Recover the prime factors `p` and `q`.
3. Compute the private exponent `d`.
4. Decrypt the provided ciphertext.

## Educational Purpose

This project is intended solely for educational purposes to demonstrate a specific weakness that arises when RSA primes are generated too close together.

Modern RSA implementations generate primes carefully to avoid this issue, making Fermat factorization impractical against properly generated keys.

## Disclaimer

This repository is designed for cryptography education, research, and security awareness. It should not be interpreted as a practical attack against correctly implemented RSA systems.

## License

Released under the MIT License.
