#include "hamming.h"

#include <string.h>
#include <sys/types.h>

int compute(const char *lhs, const char *rhs)
{
	if (lhs == NULL || rhs == NULL)
		return -1;

	size_t l_size = strlen(lhs);
	size_t r_size = strlen(rhs);

	if (l_size != r_size)
		return -1;

	int mistakes = 0;

	for (size_t i = 0; i < l_size; i++)
		if (lhs[i] != rhs[i])
			mistakes++;

	return mistakes;
}
