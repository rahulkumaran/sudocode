#include<iostream>

using namespace std;

int test_3 (int a,int temp,float test) {
	
	float b=10;
	test=10;
	a = b/test;
	return a;
	
}

int main() {
	
	float a=10;
	float hi=20;
	cout << hi << endl;
	test_3(0,10,10);
	for(int i=0; i <= 10; i++)
	{
		if (i%2==0) {
			cout << i << endl;
		}
		else {
			cout << "not even" << endl;
		}
	}
	return 0;
}