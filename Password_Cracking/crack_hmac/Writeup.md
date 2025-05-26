# 🏴 Crack Hmac Hash

> **Category:** Password Cracking
> **Points:** 15 pts
> **Author:** Sebastian
> **Description:** Can you crack this HMAC hash given the key and a wordlist?

---

## Purpose

The purpose of this challenge was to crack a hash to find a password, and submit the password as the flag.

## Exploitation

The thing we have to do in order to crack this hash is to write a python script that reads the rockyou.txt file, and computes the hexdigest of the HMAC encryption of every password in the rockyou.txt file. Then if the digets matches the hash shown, we have found our answer, and we can submit the answer as the flag.

The python script to crack this hash can be found in the solve.py file.


## Solution

[Solution](./Solution.png)

flag: ```WSUCTF{iamahacker}```