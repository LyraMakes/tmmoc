#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

const char* indxSym[] = {"H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"};
const double indxMM[] = {1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180, 22.99, 24.305, 26.982, 28.085, 30.974, 32.06, 35.45, 39.948, 39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546, 65.38, 69.723, 72.630, 74.922, 78.971, 79.904, 83.798, 85.468, 87.62, 88.906, 91.224, 92.906, 95.95, 98, 101.07, 102.91, 106.42, 107.87, 112.41, 114.82, 118.71, 102.76, 127.6, 126.9, 131.29, 132.91, 137.33, 138.91, 140.12, 140.91, 144.24, 145, 150.36, 151.96, 157.25, 158.93, 162.5, 164.93, 167.26, 168.93, 173.05, 174.97, 178.49, 180.95, 183.84, 186.21, 190.23, 192.22, 195.08, 196.97, 200.59, 204.38, 207.2, 208.98, 209, 210, 222, 223, 226, 227, 232.04, 231.04, 238.03, 237, 244, 243, 247, 247, 251, 252, 257, 258, 259, 266, 267, 268, 269, 270, 270, 278, 281, 282, 285, 286, 289, 290, 293, 294, 294};

#define ARR_SIZE 118


// bool stringInArray(char* string, char** array, int arraySize)
// {
//     for (int i = 0; i < arraySize; i++)
//     {
//         if (strcmp(string, array[i]) == 0)
//         {
//             return true;
//         }
//     }
//     return false;
// }

int stringIndexInArray(const char* string, const char** array, int arraySize)
{
    for (int i = 0; i < arraySize; i++)
    {
        if (strcmp(string, array[i]) == 0)
        {
            return i;
        }
    }
    return -1;
}


int getNumber(const char* string, int start)
{
    int res = 0;

    int i = start;
    while (isdigit(string[i]))
    {
        res *= 10;
        res += string[i] - '0';
        i++;
    }

    return res;
}

double getMassFromSymbol(char* symbol)
{
    int indx = stringIndexInArray(symbol, indxSym, ARR_SIZE);
    if (indx == -1)
    {
        printf("Error: Symbol not found in array\n");
        return -1;
    }

    return indxMM[indx];
}


double totalMolarMassOfCompound(const char* formula)
{

    double masses[100];
    int amount[100];

    int formulaLength = strlen(formula);
    int resIndx = 0;

    char sym_buf[3];

    for (int i = 0; i < formulaLength; i++)
    {
        if (!isupper(formula[i])) continue;

        bool nextLower = islower(formula[i+1]);
        int offset = (nextLower) ? 2 : 1;

        sym_buf[0] = formula[i];
        sym_buf[1] = (nextLower) ? formula[i+1] : '\0';
        sym_buf[2] = '\0';

        double mass = getMassFromSymbol(sym_buf);
        int amt = (isdigit(formula[i+offset])) ? getNumber(formula, i+offset) : 1;

        amount[resIndx] = amt;
        masses[resIndx] = mass;

        resIndx++;
    }

    double res = 0;
    for (int i = 0; i < resIndx; i++)
    {
        res += masses[i] * amount[i];
    }

    return res;
}
