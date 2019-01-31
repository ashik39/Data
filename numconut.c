#include <stdio.h>

int main(void) {
		 int d;
		int count=0;
		scanf("%d",&d);
		while(d!=0)
		{
			d/=10;
			count++;
		}
		printf("%d",count);
	return 0;
}
