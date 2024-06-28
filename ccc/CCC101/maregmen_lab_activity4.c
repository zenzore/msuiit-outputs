#include<stdio.h>

double average_array();
int count_occurs();
void array_sum();

void ask_array();
void print_array();
void print_legend();

int main(void) {
	int cond, size, again;
	double count;
	do {
		print_legend();
			do {
			printf("Please Choose: ");
			scanf("%d", &cond);

			if (!(cond > 0 && cond<5)) {
				printf("Invalid operation\n\n");
				continue;
			}

			if (cond == 4 || cond < 1) return 0;

			printf("Enter the size of the array: ");
			scanf("%d", &size);

			double arr1[size], arr2[size], arr_copy[size];

			switch(cond) {
				case 1:
					ask_array(arr1, size, 1);
					printf("\n\nThe average of ");
					print_array(arr1, size);
					printf(" is %.1lf\n\n", average_array(arr1, size));
					break;
				case 2:
					ask_array(arr1, size, 1);
					printf("Enter the item to count: ");
					scanf("%lf", &count);
					printf("\n\n%.2lf occured %d times in ", count, count_occurs(arr1, size, count));
					print_array(arr1, size);
					printf("\n\n");
					break;
				case 3:
					ask_array(arr1, size, 2);
					ask_array(arr2, size, 3);
					for (int i = 0; i<size; i++) arr_copy[i] = arr2[i];
					array_sum(arr1, arr2, size);
					printf("\n\nThe sum of ");
					print_array(arr1, size);
					printf(" and ");
					print_array(arr_copy, size);
					printf(" is ");
					print_array(arr2, size); 
					printf("\n\n");
			}

			printf("Press 1 to try again: ");
			scanf("%d", &again);

			if (again!=1) {
				printf("Invalid input.");
				return 0;
			}

		} while (!(cond > 0 && cond<5));		
	
	} while (1);

}

double average_array(double arr[],int size) {
	double average = 0.0;
	for (int i = 0; i<size; i++) {
		average += arr[i];
	}
	return average / size;
}

int count_occurs(double arr[], int size, double count) {
	int c = 0;
	for (int i = 0; i<size; i++) {
		if (arr[i] == count) {
			c += 1;
		}
	}
	return c;
}


void array_sum(double arr1[], double arr2[], int size) {
	for (int i = 0; i<size; i++) {
		arr2[i] += arr1[i];
	}
}


void print_legend() {
	printf("OPERATIONS:\n");
	printf("1 Get the average of the array.\n");
	printf("2 Get the number of occurence of an item in the array\n");
	printf("3 Get the sum of two arrays.\n");
	printf("4 Exit\n\n");
}

void print_array(double arr[], int size) {
	printf("{");
	for (int i = 0; i<size; i++) {
		printf(" %.1lf", arr[i]);
		if(!(i==size-1)) {
			printf(",");
		}
	}
	printf(" }");
}


void ask_array(double arr[], int size, int o) {
	if(o==1) {
		for (int i = 0; i<size; i++) {
			printf("Enter element %d: ", i+1);
			scanf("%lf", &arr[i]);
		}
	} else if (o == 2) {
		for (int i = 0; i<size; i++) {
			printf("Enter element %d of the first array: ", i+1);
			scanf("%lf", &arr[i]);
		}
	} else {
		for (int i = 0; i<size; i++) {
			printf("Enter element %d of the second array: ", i+1);
			scanf("%lf", &arr[i]);
		}
	}
}
