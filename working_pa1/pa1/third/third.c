#include <stdio.h>
#include <stdlib.h>

/*****************************
	THIS IS NOT A Resizeable Array but Rather... a linked List
*****************************/

int true = 1;
struct lNode 
{

	struct lNode *child; 
	struct lNode *prev; 
	int arg; 

};

struct lNode *removeNode(struct lNode *head, int value)
{
	struct lNode *mediator;
	mediator = head; 

	while(true)
	{
		
		if(mediator == NULL) 
		{
			return(head);
		}
		if((*mediator).arg == value) 
		{
															
			if((*mediator).prev == NULL && (*mediator).child == NULL ) 
			{
				return(NULL); 
			}
			if((*mediator).prev != NULL) 
			{

				(*((*mediator).prev)).child = (*mediator).child; 


			}
			
			

			
			if((*mediator).child != NULL) 
			{
				(*((*mediator).child)).prev = (*mediator).prev; 
			}
			
			(*mediator).prev = NULL;
			(*mediator).child = NULL;
			free(mediator); 

			

			

			return(head); 
		}

		mediator = (*mediator).child;
	}

	return(NULL);
}

void printContents(struct lNode *head) 
{
	struct lNode *mediator;
	mediator = head;
	
	while(mediator != NULL)
	{
		
		printf("%d", (*mediator).arg);
		mediator = (*mediator).child; 
		if(mediator == NULL) 
		{
			break;
		}
		printf("%c", '\t'); 

	}

	printf("%c", '\n'); 
	return;
}
struct lNode *addNode(struct lNode *head, int value)
{
	struct lNode *mediator;
	mediator = head; 
	struct lNode *x;

	x = malloc(sizeof(struct lNode)); 
	
	(*x).arg = value; 

	if(mediator == NULL) 
	{
		
		(*x).prev = NULL; 
		(*x).child = NULL; 
		
		return(x); 
	}
	while(true)
	{
		if((*mediator).arg == value) 
		{
			
			return head;
		}
		if((*mediator).arg > value) 
		{
			if((*mediator).prev != NULL) 
			{
				
				(*x).prev = (*mediator).prev; 
				(*x).child = mediator; 
				(*mediator).prev = x; 
				(*((*x).prev)).child = x; 
				
				return(head); 
			}

			
			(*x).prev = NULL;
			(*x).child = mediator;
			(*mediator).prev = x;
			
			return(x); 
		}

		if((*mediator).child == NULL) 
		{
			(*x).prev = mediator; 
			(*mediator).child = x;
			(*x).child = NULL;
			
			return(head); 

		}

		mediator = (*mediator).child;
	}
}

int main(int argc, char** argv)
{
	struct lNode *head;
	FILE *readfile;
	int value; 
	char type; 
	char buffer[100];

	head = NULL; 

	if(argc < 2 || argc > 2)
	{
		printf("%s", "Incorrect Number of Arguments");
		return(0);
	}

	  

	readfile = fopen(argv[1], "r"); 

	if(readfile == NULL)
	{
		printf("%s", "error\n"); 
		return(0);
	}

	while(fgets(buffer, 100, readfile) != NULL) 
	{
		if(sscanf(buffer, "%c %d",&type, &value ) != 2)
		{
			printf("%s", "error\n");
			return(0);
		}

		if(type == 'i')
		{
			
			head = addNode(head,value); 
		
		}
		if(type == 'd')
		{
			
			head = removeNode(head,value);
		}

		
		if(type != 'i' && type != 'd')
		{
			printf("%s", "error\n");
			return(0);
		}
	}
	printContents(head);
	fclose(readfile);
	free(head);
	
	return(0);




}
