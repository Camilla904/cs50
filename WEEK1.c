// Logical operators

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user to agree
    char c = get_char("Do you agree?\n");

    // Check whether agreed
    if (c == 'Y' || c == 'y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("Not agreed.\n");
    }
}

// Abstraction
#include <stdio.h>

void cough(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        cough();
    }
}

// Cough once
void cough(void)
{
    printf("cough\n");
}

// Abstraction with parameterization

#include <stdio.h>

void cough(int n);

int main(void)
{
    cough(3);
}

// Cough some number of times
void cough(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("cough\n");
    }
}

// get_float and printf with %f

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float price = get_float("What's the price?\n$");
    printf("Your total is $%.2f.\n", price * 1.0625);
}

// Floating-point arithmetic with float

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for x
    float x = get_float("x: ");

    // Prompt user for y
    float y = get_float("y: ");

    // Perform division
    printf("x / y = %.50f\n", x / y);
}

// Prints an n-by-n grid of bricks with a loop

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

// Calculates a remainder

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt user for integer
    int n = get_int("n: ");

    // Check parity of integer
    if (n % 2 == 0)
    {
        printf("even\n");
    }
    else
    {
        printf("odd\n");
    }
}

// Abstraction and scope

#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);

int main(void)
{
    int i = get_positive_int();
    printf("%i\n", i);
}

// Prompt user for positive integer
int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Positive Integer: ");
    }
    while (n < 1);
    return n;
}

// Math library

#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    double base = get_double("Base: ");
    double exponent = get_double("Exponent: ");
    printf("Output: %.0f\n", pow(base, exponent));
}

// Return value

#include <cs50.h>
#include <stdio.h>

int square(int n);

int main(void)
{
    int input = get_int("Input: ");
    printf("Output: %i\n", square(input));
}

// Square n
int square(int n)
{
    return n * n;
}

// get_string and printf with %s

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("What's your name?\n");
    printf("hello, %s\n", s);
}
