#include <stdio.h>

/* 
Write a program to swap values of two integer variables
*/ 

int main() {
  int var1, var2;
  int tr = 0;
  printf("Enter a number: ");
  scanf("%i", &var1);
  printf("Enter a number: ");
  scanf("%i", &var2);
  tr = var1; // assign the value or var1 to tr
  var1 = var2; 
  var2 = tr; // tr is the value of var1
  printf("var1 = %d, var2 = %d", var1, var2);
  return 0;
}