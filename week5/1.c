//Pointers
//Defining Custom Types
//Dynamic Memory Allocation
//Call stacks 
//File pointers

// Prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);
}

// Prints an integer via its address

#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", *&n);
}

// Stores and prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    printf("%p\n", p);
}

// Prints a string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "EMMA";
    printf("%s\n", s);
}

// Prints a string's address

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "EMMA";
    printf("%p\n", s);
}


// Prints a string's address as well the addresses of its chars

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "EMMA";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    printf("%p\n", &s[4]);
}

// Prints a string's chars

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "EMMA";
    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
    printf("%c\n", s[3]);
}

// Stores and prints a string without using the CS50 Library

#include <stdio.h>

int main(void)
{
    char *s = "EMMA";
    printf("%c\n", s[0]);
    printf("%c\n", s[1]);
    printf("%c\n", s[2]);
    printf("%c\n", s[3]);
}

// Stores and prints a string's address via pointer arithmetic

#include <stdio.h>

int main(void)
{
    char *s = "EMMA";
    printf("%c\n", *s);
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
    printf("%c\n", *(s+3));
}



