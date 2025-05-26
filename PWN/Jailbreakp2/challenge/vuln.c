#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void init() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}

void pop_rdi_ret() {
    asm volatile (
        "pop %rdi\n\t"
        "ret\n\t"
    );
}

void vuln() {
    char buffer[64];
    printf("📥 Enter your payload: ");
    gets(buffer);
    puts(buffer);
    printf("🎉 Printed your input! Try again? 😈\n");
}

void run_command() {
    printf("✅ This time, I can't let you run whatever you want. 😄😄😄😄\nI can tell you my name though. Here's my name:\n");
    system("whoami");
}

int main() {
    init();
    printf("🎊 Welcome to the Buffer Overflow Bonanza! 🎈\n");
    printf("🔐 Can you crack the code and get a shell? 🐚\n");
    printf("1️⃣ Option 1: Smash the stack!\n");
    printf("2️⃣ Option 2: Run a command!\n");
    printf("3️⃣ Option 3: Quit\n");
    while (1) {
        printf("\n📋 Choose an option (1, 2, or 3): ");
        char choice = getchar();

        int ch;
        while ((ch = getchar()) != '\n' && ch != EOF);
        
        if (choice == '1') {
            vuln();
        } else if (choice == '2') {
            run_command();
        } else if (choice == '3') {
            printf("👋 Goodbye! Try again soon! 😄\n");
            exit(0);
        } else {
            printf("❌ Invalid choice! Pick 1, 2, or 3! 🤓\n");
        }
    }
    return 0;
}