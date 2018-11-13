#include<stdio.h>
int main(void)
{
	int x,y;
	printf("Enter a 24-hour time: ");
	scanf("%d:%d",&x,&y);
	if(x<0)
		printf("不是正確的時間格式");
	else if(x<1)
		printf("Equivalent 12-hour time: %d:%.2d AM",x+12,y);
	else if(x<12)
		printf("Equivalent 12-hour time: %d:%.2d AM",x,y);
	else if(x<13)
		printf("Equivalent 12-hour time: %d:%.2d PM",x,y);
	else if(x<24)
		printf("Equivalent 12-hour time: %d:%.2d PM",x-12,y);
	
	
	else
		printf("不是正確的時間格式");
	
	
	
	
	
	
	
	
	
	
	return 0;
}