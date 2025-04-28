import hashlib

def custom_hash(data: bytes) -> bytes:
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.digest()

if __name__ == "__main__":
    test_data = b"Hello, world!"
    result = custom_hash(test_data)
    print(f"Input: {test_data}")
    print(f"Hash (hex): {result.hex()}")
    print(f"Hash length: {len(result)} bytes")