#include "resistor_color_duo.h"
#include <math.h>
#include <stdlib.h>
#include <sys/types.h>

#define MAXSZ 2

u_int16_t color_code(resistor_band_t *colors) {
  resistor_band_t ret = 0;

  if (colors == NULL)
    return 99;

  for (u_int16_t i = 0; i < 2; i++)
    ret += pow(10, (MAXSZ - i - 1)) * colors[i];

  return ret;
}
