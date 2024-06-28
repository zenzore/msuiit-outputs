#include<stdio.h>

int odd_numbers();   // we initialize two functions
int even_numbers();  // to have a cleaner code

int main(void) {

    int first, second, cond;

    // i will use a do while loop for this problem. 
    // I first thought of using two nested do while loops but since it will only execute the scanning
    // of two integers once, I will just use the do while loop when it is time to scan fhte cond variable. 
    
    printf("Enter a number: ");
    scanf("%d", &first);
    printf("\n");printf("Enter another number: ");
    scanf("%d", &second);    
    if (first >= second) {
        printf("Invalid input Range.\n");
        return 0;
    }
        
    do {
            
        printf("Enter [1] to use display even [2] to display odd: ");
        scanf("%d", &cond);

        if (cond > 2) {
            printf("Invalid input!\n");
            continue;
        }

    } while(cond > 2);

    if (cond==1) { 
        even_numbers(first, second); 
    }
    else 
        odd_numbers(first, second);
    
    printf("\n");

}

// odd_numbers funciton, it will return the odd numbers BETWEEEN the 
//first and second integer argument
int odd_numbers(int first, int second) {
    printf("Odd numbers from %d to %d.\n", first, second);
    for(first++; first < second; first++) { // it will intialize a statement which is to add 1
                                              // in order to skip the number so it cannot proceed to the if condition.
        if ((first%2)) {
            printf("%d ", first);
        }
    }
}

// even_numbers funciton, it will return the even numbers BETWEEEN 
//the first and second integer argument
int even_numbers(int first, int second) {
    printf("Odd numbers from %d to %d.\n", first, second); 
    for(first++; first <= second-1; first++) { // it will intialize a statement which is to add 1, in order 
                                             // to skip the number so it cannot proceed to the if condition.
        if (!(first%2)) {
            printf("%d ", first);
        }
    }
}
