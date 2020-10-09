#include "resistor_color_trio.h"

#include <math.h>
#include <stdlib.h>
#include <sys/types.h>

#define MAXSZ 3

resistor_value_t color_code(resistor_band_t *colors) {
  resistor_value_t color_data;
  u_int64_t count = 0;

  for (int i = 0; i < MAXSZ; i++)
    if ((i + 1) == MAXSZ)
      count *= pow(10, colors[i]);
    else
      count += colors[MAXSZ - 2 - i] * pow(10, i);

  if (count >= 1000) {
    color_data.unit = KILOOHMS;
    count /= 1000;
  } else {
    color_data.unit = OHMS;
  }

  color_data.value = (u_int16_t)count;

  return color_data;
}
