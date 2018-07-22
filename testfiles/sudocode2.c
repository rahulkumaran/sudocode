#include <stdio.h>
#include <stdlib.h>

int test_2(int a,int b,int sad)
{
	a=0;
	b=a;
	sad=b;
	return sad;
}


int main()
{
	
	float a;
	a=120;
	float b=10;
	float summ;
	summ=a+b;
	test_2(2,3,4);
	for(int i=10; i >= 1; i-=2)
	{
		printf("%d\n",i);
	}
	printf("%f\n",summ);
}