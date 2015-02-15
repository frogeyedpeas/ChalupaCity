COMPILER = gcc
CCFLAGS  = -Wall -ansi -pedantic
all: second

second: second.o
	$(COMPILER) $(CCFLAGS) -o second second.o
second.o: second.c second.h
	$(COMPILER) $(CCFLAGS) -c second.c 
clean:
	rm -f second second.o