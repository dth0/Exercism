#include "square_root.h"

#include <sys/types.h>

u_int16_t square_root(u_int16_t number) {

  u_int16_t min = 0;
  u_int16_t middle = 0;
  u_int16_t max = number;

  while (max >= min) {
    middle = min + ((max - min) / 2);

    u_int32_t result = middle * middle;

    if (result == number)
      return middle;

    if (result > number)
      max = middle - 1;
    else
      min = middle + 1;
  }

  return -1;
}
