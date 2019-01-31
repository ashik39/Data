#include<stdio.h>
int main(void){
    int sum=0,c,i;
    int a[30];
    scanf("%d",&c);
    for(i=1;i<=c;i++)
    {
    	scanf("%d",&a[i]);
    	sum=sum+a[i];
    }
  printf("%d",sum);
    return 0;
}
