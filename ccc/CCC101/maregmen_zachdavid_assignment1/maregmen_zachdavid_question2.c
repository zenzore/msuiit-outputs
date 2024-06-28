/* 
Write a program to compute the average of three given numbers
*/ 

#include <stdio.h>

int main() {
  double first, second, third;
  double ave;
  printf("Input the first number: ");
  scanf("%lf", &first);
  printf("Input the second number: ");
  scanf("%lf", &second);
  printf("Input the third number: ");
  scanf("%lf", &third);
  ave = (first + second + third) / 3;
  printf("The average of these numbers is : %.3lf\n", ave);
  return 0;
}