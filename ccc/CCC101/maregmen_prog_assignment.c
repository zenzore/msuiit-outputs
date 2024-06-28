#include<stdio.h>    
#include<stdio.h>  
#include<stdlib.h>  
#include<time.h> 
#include<string.h>

#define supported_symbols "!@#$%^&*()-_+={}[]<>?"
#define smol_letters "abcdefghijklmnopqrstuvwxyz"
#define numbers "1234567890"
#define big_letters "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#define minChar 8

void generatePassword();
int randInt();


int main(void) 
{   
    srand(time(0));

    int len, t;
    do {
        do {
            printf("Enter password length: ");
            scanf("%d", &len);
            if (len>=minChar) {
                generatePassword(len);
            }
            else {
                printf("Password length must be atleast 8.\n");
                continue;
            }
        } while(len < 8);
        printf("Press 1 to try again: ");
        scanf("%d", &t);
    } while(t==1);
} 

void generatePassword(int len) {
    char password[len];
    for(int i = 0; i < len; i++) {
        int ch = randInt(1, 4); // this variable will contain a number between 1 and 4, and we can use it for randomizing what type of character to create
        
        // we could use a variable containing all the characters including symbols,n numbers and letters, but the probabllity of choosing 1 of the 4 types would be low.
        if (ch==1) password[i] = smol_letters[randInt(0, 25)];
        if (ch==2) password[i] = big_letters[randInt(0, 25)];
        if (ch==3) password[i] = supported_symbols[randInt(0, 20)];
        if (ch==4) password[i] = numbers[randInt(0, 9)];

    } 
    printf("Password generated %s \n", password);
}

int randInt(int min, int max) {
    int random_number = rand() % max + min;
    return random_number;
}