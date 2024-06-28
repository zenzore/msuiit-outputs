/* 
Write a program that asks the user to enter the radius of a circle and then computes and displays the circle’s area. Use the formula

Area = PI x Radius x Radius
where PI is the constant macro 3.14159
*/ 

#include <stdio.h>
#define PI 3.14159

int main() {
  int radius;
  double area; 
  printf("Enter the radius of your circle: ");
  scanf("%i", &radius);
  area = PI * radius * radius;
  printf("The area of your circle is %lf units\n", area);
  return 0;
}