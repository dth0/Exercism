#include "armstrong_numbers.h"
#include <math.h>


int is_armstrong_number(int candidate)
{
	int result;
	int control;
	double count;

	count = ceil(log10(candidate));

	result = 0;
	control = candidate;
	while (control) {
		result += (int) pow((double) (control % 10), count);
		control /= 10;
	}

	return (result == candidate) ? 1 : 0;
}
