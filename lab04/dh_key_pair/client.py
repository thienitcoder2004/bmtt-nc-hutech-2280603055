from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(server_public_key, private_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())
    parameters = server_public_key.parameters()
    private_key, public_key = generate_client_key_pair(parameters)
    shared_key = derive_shared_secret(server_public_key, private_key)
    print(f"Shared secret: {shared_key.hex()}") 
    
if __name__ == "__main__":
    main()