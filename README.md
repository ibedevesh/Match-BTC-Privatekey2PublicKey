# ECDSA Key Pair Verification

This repository contains a Python script that verifies if a given **private key** corresponds to an expected **public key** using the **Elliptic Curve Digital Signature Algorithm (ECDSA)** with the SECP256k1 curve. 

This can be useful for cryptographic applications where key pair validation is required, such as cryptocurrency wallets, blockchain implementations, or identity verification systems.

## Features
- Verifies if a private key matches an expected public key.
- Uses the SECP256k1 curve, commonly employed in Bitcoin and Ethereum.
- Provides an additional step to print the derived public key for manual comparison.

---

## Prerequisites
Make sure you have Python installed on your system. You also need the `ecdsa` library, which can be installed using:

```bash
pip install ecdsa
'''
