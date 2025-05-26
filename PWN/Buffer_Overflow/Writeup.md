# 🏴 Jailbreak

> **Category:** Pwn
> **Points:** 15 pts
> **Author:** Sebastian
> **Description:** Can you break out of my minimal jail that I have set up? I hope I designed it to be secure enough to keep all secrets outside and all ctf players inside.

---

## Purpose

The purpose of this challenge was to allow the ctf player to run shell commands inside of a shell, and find a way to bypass a blacklist of "bash", "sh", and "cat" commands in order to find the flag, and read it out.

## Exploitation

It is recommended to always decompile binaries when you are given them in PWN challenges, so you can understand exactly what the executable is doing before you even run the file. In this challenge, I only gave the C file, so you can't decompile the actually executable file, but typically, you would use [Ghidra](https://github.com/NationalSecurityAgency/ghidra) to decompile a vulnerable linux ELF executable.

After looking into the C file, there is only one vulnerable function, and that is the 

## Solution

If we enter the correct passphrase, we get the decrypted flag:

[Solution](./Solution.png)

flag: ```WSUCTF{r3vrsing_CSHarp_3x3cutables}```