#include "sum_of_multiples.h"

#include <stdbool.h>

unsigned int sum_of_multiples(const unsigned int *multiples,
                              const size_t number_of_multiples,
                              const unsigned int up_to) {

  unsigned int result = 0;

  if (multiples == NULL)
    return result;

  for (unsigned int i = 0; i < up_to; i++) {
    bool add = false;

    for (size_t s = 0; s < number_of_multiples; s++)
      if (multiples[s] && i % multiples[s] == 0) {
        add = true;
        break;
      }

    if (add)
      result += i;
  }
  return result;
}
