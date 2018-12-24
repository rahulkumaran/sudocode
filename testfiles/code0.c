#include <stdio.h>
#include <stdlib.h>


int test_3(int a,int temp,float test)
{
	
	float b=10;
	test=10;
	a = b/test;
	return a;
	
}

int main()
{
	
	float hi=20;
	int a;
	printf("Enter a integer: ");
	scanf("%d",&a);
	float b;
	printf("Enter a float value: ");
	scanf("%f",&b);
	printf("%f\n",b);
	printf("%f\n",hi);
	int var  = test_3(0,10,10);
	for(int i=0; i <= 10; i++)
	{
		if(i%2==0)
		{
			printf("%d\n",i);
		}
		else
		{
			printf("not even\n");
		}
	}
}