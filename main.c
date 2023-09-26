#include <stdio.h>

#include "tmmoc.h"


int main(int argc, char** argv)
{
    if (argc < 2)
    {
        printf("Usage: %s <formula>\n", argv[0]);
        return 1;
    }

    double res = totalMolarMassOfCompound(argv[1]);

    printf("Molar mass of %s: %f\n", argv[1], res);


    return 0;
}