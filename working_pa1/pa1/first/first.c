#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char** argv)
{
	int x;
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

	x = atoi(argv[1]);
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
