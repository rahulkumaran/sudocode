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
	scanf("%d",&a);
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