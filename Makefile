CFLAGS = -Wall -Wextra -Werror -pedantic -g


INCLUDEDIRS = -I. -I/usr/include -I/usr/local/include -I/usr/include/python3.11



main: main.obj tmmoc.obj
	$(CC) $(CFLAGS) $(INCLUDEDIRS) main.obj tmmoc.obj -o main


main.obj: main.c
	$(CC) $(CFLAGS) $(INCLUDEDIRS) -c main.c -o main.obj


tmmoc.obj: tmmoc.c
	$(CC) $(CFLAGS) $(INCLUDEDIRS) -c tmmoc.c -o tmmoc.obj



.PHONY: clean
clean:
	-rm *.obj main
