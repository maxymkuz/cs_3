#include<stdio.h>
#include "unsigned_sum.h"

int main() {
    unsigned int x;
    int result;

    x = (unsigned int) 1234567890;
    result = digit_sum(x);
    printf("Sum of digits of %u is %u \n", x, result); // should return 10
    return 0;
}