#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int main(int argc, char** argv)
{
	int i;
	if(argc > 2 || argc < 2)
	{
		printf("%s", "error\n");
		return(0);
	}

	int x  = atoi(argv[1]);
	if(x == 1)
	{
		printf("%s", "no\n");
		return(0);
	}
	if(x == 2)
	{
		printf("%s", "yes\n");
		return(0);
	}
	

	i = 2; 
	while(i < x)
	{
		if(x%i == 0)
		{
			printf("%s", "no\n");
			return(0);
		}

		i++;
	} 

	printf("%s", "yes\n");
	return(0);


}