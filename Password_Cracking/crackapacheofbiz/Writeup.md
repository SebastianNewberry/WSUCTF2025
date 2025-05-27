# 🏴 Crack Apache Ofbiz Hash

> **Category:** Password Cracking
>
> **Points:** 15 pts
>
> **Author:** Sebastian
>
> **Description:** Can you crack this apache ofbiz password hash using rockyou.txt?

---

## Purpose

The purpose of this challenge was to crack a hash to find a password, and submit the password as the flag.

## Exploitation

For this challenge, we are given an Apache Ofbiz SHA hash, and we have to crack it. After researching how this hash is created on the internet, we can see that there is this [github repo](https://github.com/duck-sec/Apache-OFBiz-SHA1-Cracker) specifically designed to crack these hashes. Otherwise, you could also look up how Apache Ofbiz generates these hashes, then reverse engineer that to crack it.

The python script to crack this hash can be found in the solve.py file.

## Solution

![Solution](./Solution.png)

flag: ```WSUCTF{iluvwayne4eva}```