## strace

### c code
```c
// src/test.c

#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("hello world\n");
    exit(0);
}
```

### strace
```c
// set up runtime:

/* shell invokes execve, passes executable path & cli args */
execve     ( "./codes/test", [ "./codes/test" ], 0x7ffc9f684500 /* 57 vars */ )                                      =  0

brk        ( NULL )                                                                                                  =  0xdfd000

/* checks if file exists, F_OK mode flag */
access     ( "/etc/ld.so.nohwcap", F_OK )                                                                            = -1 ENOENT (No such file or directory)

/* checks if file readable, R_OK mode flag */
access     ( "/etc/ld.so.preload", R_OK )                                                                            = -1 ENOENT (No such file or directory)

/* opens some sort of linker cache? */
openat     ( AT_FDCWD, "/etc/ld.so.cache", O_RDONLY | O_CLOEXEC )                                                    =  3
fstat      ( 3, { st_mode = S_IFREG | 0644, st_size = 117631, ... } )                                                =  0
mmap       ( NULL, 117631, PROT_READ, MAP_PRIVATE, 3, 0 )                                                            =  0x7f878c9fc000
close      ( 3 )                                                                                                     =  0

/* checks if file exists, F_OK mode flag */
access     ( "/etc/ld.so.nohwcap", F_OK )                                                                            = -1 ENOENT (No such file or directory)

/* opens libc.so.6 shared object file for dynamic linking */
openat     ( AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY | O_CLOEXEC )                                     =  3

/* reads file header (832 B) from libc.so.6, note that \XXX are in octal */
read       ( 3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\240\35\2\0\0\0\0\0"..., 832 )                        =  832
fstat      ( 3, { st_mode = S_IFREG | 0755, st_size = 2030928, ... } )                                               =  0
mmap       ( NULL,           8192,    PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0 )                   =  0x7f878c9fa000
mmap       ( NULL,           4131552, PROT_READ | PROT_EXEC,  MAP_PRIVATE | MAP_DENYWRITE,  3, 0 )                   =  0x7f878c3ff000
mprotect   ( 0x7f878c5e6000, 2097152, PROT_NONE )                                                                    =  0
mmap       ( 0x7f878c7e6000, 24576,   PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_FIXED | MAP_DENYWRITE, 3, 0x1e7000 ) =  0x7f878c7e6000
mmap       ( 0x7f878c7ec000, 15072,   PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_FIXED | MAP_ANONYMOUS, -1, 0 )       =  0x7f878c7ec000
close      ( 3 )                                                                                                     =  0

arch_prctl ( ARCH_SET_FS, 0x7f878c9fb4c0 )                                                                           =  0
mprotect   ( 0x7f878c7e6000, 16384, PROT_READ )                                                                      =  0
mprotect   ( 0x600000,       4096,  PROT_READ )                                                                      =  0
mprotect   ( 0x7f878ca19000, 4096,  PROT_READ )                                                                      =  0
munmap     ( 0x7f878c9fc000, 117631 )                                                                                =  0

// actual code:

/* printf() invokes fstat on stdout for some reason */
fstat      ( 1, { st_mode = S_IFCHR | 0620, st_rdev = makedev(136, 0), ... } )                                       =  0

/* heap allocation by malloc during printf */
brk        ( NULL )                                                                                                  =  0xdfd000
brk        ( 0xe1e000 )                                                                                              =  0xe1e000

/* actual write call by printf */
write      ( 1, "hello world\n", 12 )                                                                                =  12

/* exit() invokes exit_group */
exit_group ( 0 )                                                                                                     =  ?
```
