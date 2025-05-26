import argparse
import hashlib
import hmac
import os

def generate_hmac(key, password):
    hash_obj = hmac.new(key, password, hashlib.sha1)

    hmac_digest = hash_obj.hexdigest()

    return hmac_digest

def main(): 
    parser = argparse.ArgumentParser(description="Brute force HMAC hashes")
    parser.add_argument("--key", help="HMAC key", required=True)
    parser.add_argument("--hash-string", help = "hash you are trying to crack", required=True)
    parser.add_argument("--wordlist", help="Path to the wordlist file", default="/usr/share/wordlists/rockyou.txt", required=False)

    args = parser.parse_args()

    key = args.key

    attempts = 0

    with open(args.wordlist, 'r', encoding='latin-1') as password_list:
        print ("[+] Attempting to crack....")
        for password in password_list:
            attempts += 1
            value = password.strip()
            hashed_password = generate_hmac(key.encode('utf-8'), value.encode('utf-8'))
            if hashed_password == args.hash_string:
                print(f'Found Password: {value}')
                print(f'hash: {hashed_password}')
                print(f'(Attempts: {attempts})')
                print("[!] Super, I bet you could log into something with that!")
                break
        else:
            print(f"[!] Password not found in the wordlist. :( (Attempts: {attempts})")

if __name__ == "__main__":
    main()