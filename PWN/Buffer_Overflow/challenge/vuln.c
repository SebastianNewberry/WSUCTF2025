#include <stdio.h>
#include <string.h>

void vuln() {
    char buffer[100];
    printf("Buffer address: %p\n", (void *)buffer);
    printf("Enter your input: ");
    gets(buffer);
    printf("You entered: %s\n", buffer);
}

int main() {
    setbuf(stdout, NULL);
    printf("Welcome to the buffer overflow challenge!\n");
    vuln();
    return 0;
}