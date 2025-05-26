#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int is_dangerous(const char *input) {
    const char *blacklist[] = {
        "cat", "sh"
    };
    int num_blacklist = sizeof(blacklist) / sizeof(blacklist[0]);

    for (int i = 0; i < num_blacklist; i++) {
        if (strstr(input, blacklist[i]) != NULL) {
            return 1;
        }
    }
    return 0;
}

void run_command() {
    char buffer[80];
    printf("📝 Enter a command: ");
    fgets(buffer, sizeof(buffer), stdin);

    buffer[strcspn(buffer, "\n")] = 0;

    if (is_dangerous(buffer)) {
        printf("🚫 Blocked: command contains disallowed keywords.\n");
        fflush(stdout);
        return;
    }

    system(buffer);
    fflush(stdout);
    printf("✅ Command executed! What's next? 😄\n");
}

int main() {
    init();
    printf("🔐 Can you crack the code and get the flag? 🏁\n");
    printf("1️⃣ Option 1: Run a Command!\n");
    printf("2️⃣ Option 2: Quit!\n");

    while (1) {
        printf("\n📋 Choose an option 1 or 2: ");
        char choice = getchar();

        int ch;
        while ((ch = getchar()) != '\n' && ch != EOF);

        if (choice == '1') {
            run_command();
        } else if (choice == '2') {
            printf("👋 Goodbye! Try again soon! 😄\n");
            exit(0);
        } else {
            printf("❌ Invalid choice! Pick 1 or 2! 🤓\n");
        }
    }
    return 0;
}