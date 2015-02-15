#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char** argv)
{
	if(argc > 2)
	{
		printf("error\n");
		return(0);
	}
	if(argc <= 1)
	{
		printf("error\n");
		return(0);
	}

	int x = atoi(argv[1]); //extracted input number
	if(x%2 == 0)
	{
		printf("even\n");
		return 0;
	}
	if(x%2 == 1)
	{
		printf("odd\n");
		return 0;
	}
}