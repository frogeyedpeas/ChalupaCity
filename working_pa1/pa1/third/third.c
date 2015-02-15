#include <stdio.h>
#include <stdlib.h>

/*****************************
	THIS IS NOT A Resizeable Array but Rather... a linked List
*****************************/

int true = 1;
struct lNode //assumed to be in size sorted order
{

	struct lNode *child; //the pointer to the next node
	struct lNode *prev; //the pointer to the previous node
	int arg; //the value contained

};

struct lNode *removeNode(struct lNode *head, int value)
{
	struct lNode *mediator = head; //a new node pointer for the head so we don't lose the head

	while(true)
	{
		//printf("%d \n", (*mediator).arg);
		if(mediator == NULL) //we're at the end of the list. Nothing to delete here
		{
			return(head);
		}
		if((*mediator).arg == value) //we found it and need to delete
		{
															//* -> retrieve object, & -> retrieve address
			if((*mediator).prev == NULL && (*mediator).child == NULL ) //one piece object
			{
				return(NULL); //thats it!
			}
			if((*mediator).prev != NULL) //Null check for previous
			{

				(*((*mediator).prev)).child = (*mediator).child; //the previous child is the this's child


			}
			
			

			
			if((*mediator).child != NULL) //Null check for child
			{
				(*((*mediator).child)).prev = (*mediator).prev; //the next's previous is this previous
			}
			
			(*mediator).prev = NULL;
			(*mediator).child = NULL;
			free(mediator); //frees it

			

			

			return(head); //returns the head that should now have the modification
		}

		mediator = (*mediator).child;
	}
}

void printContents(struct lNode *head) //Prints List Contents
{
	struct lNode *mediator = head;
	
	while(mediator != NULL)
	{
		//printf("%s", "Printing Node Goods \n");
		printf("%d", (*mediator).arg);
		mediator = (*mediator).child; //go to the next value
		if(mediator == NULL) //break out and don't tabify
		{
			break;
		}
		printf("%c", '\t'); //insert tabs once we know that the next isn't broken

	}

	printf("%c", '\n'); //print the newline
	return;
}
struct lNode *addNode(struct lNode *head, int value)
{
	struct lNode *mediator = head; //a new node equivalent to the head pointer

	//struct lNode x; //the node to be added
	struct lNode *x = malloc(sizeof(struct lNode)); //ALlocation of memory
	
	(*x).arg = value; //set its value accordingly

	if(mediator == NULL) //If the head itself was a null pointer
	{
		
		(*x).prev = NULL; //So that later additions will be simple
		(*x).child = NULL; //So that later additions will be simple
		//printf("Initialized with: %d \n", (*x).arg); //REMOVE 
		return(x); //returns the address
	}
	while(true)
	{
		//printf("Value: %d, Address: %p, Child Address: %p, Parent Address: %p: \n",(*mediator).arg, mediator,(*mediator).child, (*mediator).prev);
		if((*mediator).arg == value) //If its found don't do shit!
		{
			//printf("We already discovered %d \n", x.arg); //REMOVE
			return head;
		}
		if((*mediator).arg > value) //If the current value is too big pass to the previous point
		{
			if((*mediator).prev != NULL) //if the previous value isn't null
			{
				
				(*x).prev = (*mediator).prev; //past of x is the past of the current
				(*x).child = mediator; //child of x is the current pointer
				(*mediator).prev = x; //past of the current is x
				(*((*x).prev)).child = x; //child of the past of x is a pointer to x
				//printf("%d \n", x.arg); //REMOVE
				return(head); //return the address or pointer to x
			}

			
			(*x).prev = NULL;
			(*x).child = mediator;
			(*mediator).prev = x;
			//printf("%d \n", x.arg); //REMOVE
			return(x); //returns the pointer to x since x is the head (the head is only element with no previous)
		}

		if((*mediator).child == NULL) //the value isn't bigger since previous code would've applied and the child is NULL!
		{
			(*x).prev = mediator; //lock down the previous mohterufcker!
			(*mediator).child = x;
			(*x).child = NULL;
			//printf("%s","I have reached the last if! \n"); //REMOVE
			return(head); //returns the pointer to x

		}

		mediator = (*mediator).child;
	}
}

int main(int argc, char** argv)
{
	if(argc < 2 || argc > 2)
	{
		printf("%s", "Incorrect Number of Arguments");
		return(0);
	}

	struct lNode *head = NULL; //start off with a null pointer. This gets modified
	FILE *readfile;
	int value; //carries the value
	char type; //determines the type
	char buffer[100];  //To store character data

	readfile = fopen(argv[1], "r"); //TIME TO READDDDDD

	if(readfile == NULL)
	{
		printf("%s", "error\n"); //Lets us know if file not found
		return(0);
	}

	while(fgets(buffer, 100, readfile) != NULL) //process each line
	{
		if(sscanf(buffer, "%c %d",&type, &value ) != 2)
		{
			printf("%s", "error\n");
			return(0);
		}

		if(type == 'i')
		{
			//printf("Adding: %d \n", value);
			head = addNode(head,value); //add that shit!
			//printf("Added: %d \n", value);
			/*printf("%s", "Printing Goods \n");
			printf("%p \n", (*head).prev); //lets see stuff
			printf("%p \n", (*head).child); //lets see stuff*/
		}
		if(type == 'd')
		{
			
			head = removeNode(head,value);
		}

		//printContents(head);
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