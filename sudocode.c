#include <stdio.h>
#include <stdlib.h>

int main()
{
	float i=0;
	int k=100;
	for(int i=0; i <= 10; i++)
	{
		printf("hey dude\n");
		k++;
		k+=100;
	}
	for(int i=0; i <= 10; i+=2)
	{
		while(i<=5)
		{
			printf("in loop 1\n");
			printf("wooho\n");
			i++;
		}
		printf("success\n");
		k++;
	}
	while(i<=10)
	{
		printf("here\n");
		printf("there\n");
		printf("everywhere\n");
		i++;
	}
	printf("It's over mama\n");
}