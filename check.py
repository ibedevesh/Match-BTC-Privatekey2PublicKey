from ecdsa import SigningKey, SECP256k1, VerifyingKey
import hashlib

def verify_key_pair(private_key_hex, expected_public_key_hex):
    try:
        # Convert the hex string to bytes
        private_key_bytes = bytes.fromhex(private_key_hex)
        
        # Create the signing key
        sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
        
        # Get the verifying key (public key)
        vk = sk.get_verifying_key()
        
        # Get the public key in uncompressed format
        derived_public_key = '04' + vk.to_string().hex()
        
        # Compare with the expected public key
        return derived_public_key == expected_public_key_hex
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# The recovered private key
private_key_hex = "Enter your private key!!!!"

# The expected public key (uncompressed format)
expected_public_key = "Enter your publick key!!!"

if verify_key_pair(private_key_hex, expected_public_key):
    print("The private key is valid and corresponds to the given public key.")
else:
    print("The private key does not correspond to the given public key.")

# Additional verification
sk = SigningKey.from_string(bytes.fromhex(private_key_hex), curve=SECP256k1)
vk = sk.get_verifying_key()
derived_public_key = '04' + vk.to_string().hex()
print(f"Derived public key: {derived_public_key}")
