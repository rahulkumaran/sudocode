#include <stdio.h>
#include <stdlib.h>

int main()
{
	
	float a=10;
	float hi=20;
	char c='a';
	char d='b';
	int e=5;
	int f=5;
	printf("%c\n",c);
	printf("%c\n",d);
	printf("hi\n");
	printf("%f\n",hi+a);
	printf("%d\n",e+f);
	printf("%f\n",hi);
	printf("%d\n",e);
	
	for(int i=0; i <= 10; i++)
	{
		if(i%2==0)
		{
			printf("%d\n",i);
		}
		else
		{
			"print not even";
		}
	}
}