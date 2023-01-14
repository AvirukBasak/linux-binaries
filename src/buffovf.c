#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

struct internet {
    int id;
    char *name;
};

// redirect code excution via buffer overflow
void target() {
    printf("flag{_SUCCESS_%ld_}\n", time(NULL));
}

int main(int argc, char **argv) {
    if (argc <= 2) abort();
    struct internet *ip1, *ip2;

    ip1 = malloc(sizeof(struct internet));
    ip1->id = 0xDEAD;
    ip1->name = malloc(8);

    ip2 = malloc(sizeof(struct internet));
    ip2->id = 0xBEEF;
    ip2->name = malloc(8);

    strcpy(ip1->name, argv[1]);
    strcpy(ip2->name, argv[2]);
    printf("%s, %s\n", ip2->name, ip1->name);

    return 0;
}
