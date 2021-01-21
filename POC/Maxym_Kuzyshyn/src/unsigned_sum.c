#include "unsigned_sum.h"
#include<stdio.h>
#include<stdlib.h>

int digit_sum(unsigned int num) {
    int sum;  // int is enough here
    while (num > 0) {
        sum += num % 10;
        num = num / 10;
    }
    return sum;  // simple as it is:-)
}