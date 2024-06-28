/* 
Write a program to compute the seconds from a given Age
*/ 

#include <stdio.h>
#define DAYS_IN_YEAR 365
#define HOURS_IN_DAYS 24
#define MINUTES_IN_HOUR 60
#define SECONDS_IN_MINUTES 60

int main() {
  int age;
  int seconds;
  printf("Please enter your age: ");
  scanf("%i", &age);
  seconds = age * DAYS_IN_YEAR * HOURS_IN_DAYS * MINUTES_IN_HOUR * SECONDS_IN_MINUTES;
  printf("You have lived for atleast %'d seconds.\n", seconds);
  return 0;
}