#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

int* matrixadder(int rows, int columns, int m1[], int m2[])
{
	int * m3;
	int cap;
	int i;

	m3 = malloc(rows*columns*sizeof(int)); 

	cap = sizeof(m1)/sizeof(int);
	
	i = 0;
	while(i <= rows*columns) 
	{
		m3[i] = m1[i] + m2[i];
		i++;
	}
	
	return m3;
}

int main(int argc, char** argv)
{
	FILE *readfile; 
	int rows; 
	int columns;
	char buffer[5000]; 

	int array1[rows*columns]; 
	int array2[rows*columns];
	int * outarray; 
	int i;
	int j;
	char * copy; 
	char *token; 
	
	if(argc < 2 || argc > 2)
	{
		printf("error\n"); 
		return(0);
	}

	
	readfile = fopen(argv[1], "r"); 
	fgets(buffer,100,readfile); 
	
	if(sscanf(buffer, "%d %d", &rows, &columns) != 2) 
	{
		
		printf("%s", "error\n");
		return(0);
	}
	
	
	i = 0; 
	j = columns; 
	
	while(i < rows*columns)
	{
		fgets(buffer,100,readfile);
		token = strtok(buffer, "\t"); //grab the first token using space delimiter
		while(i/j < 1)
		{
			//printf("%s hello\n", token);
			//strcpy(copy,token);
			array1[i] = atoi(token);
			//printf("%d ", array1[i]);
			i++;
			token = strtok(NULL, "\t"); //what the fuck?
		}
		j+=columns;
		//printf("%c", '\n'); //flush the stream
	}
	
	fgets(buffer,100,readfile); //grab the new line
	
	while(i < 2*rows*columns)
	{
		fgets(buffer,100,readfile);
		token = strtok(buffer, "\t");
		while(i/j < 1)
		{
			array2[i-rows*columns] = atoi(token);
			//printf("%d ", array2[i-rows*columns]);
			i++;
			token = strtok(NULL, "\t");
		}
		j+=columns;
		//printf("%c", '\n');

	}

	outarray = matrixadder(rows, columns, array1, array2);

	i = 0;
	j = columns;
	while(i < rows*columns)
	{
		while(i/j < 1)
		{
			printf("%d \t", outarray[i]);
			i++;
		}
		j+=columns;

		printf("%c", '\n');
		
	}

		
	

	return(0);

}