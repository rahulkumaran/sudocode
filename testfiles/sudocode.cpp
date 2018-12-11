#include<iostream>

using namespace std;

int test (int a,int b,int c)
{
	cout << "test func" << endl
	a++;
	b++;
	c++;
	a = b + c;
	return a;
	
}

int main() {
	
	float i=0;
	int k=100;
	for(int i=0; i <= 10; i++)
	{
		cout << "hey dude" << endl
		k++;
		k+=100;
	}
	for(int i=0; i <= 10; i+=2)
	{
		while(i<=5) {
			cout << "in loop 1" << endl
			cout << "wooho" << endl
			i++;
		}
		cout << "success" << endl
		k++;
	}
	while(i<=10) {
		cout << "here" << endl
		cout << "there" << endl
		cout << "everywhere" << endl
		i++;
	}
	cout << "It's over mama" << endl
}