#include "resistor_color.h"
#include <stdlib.h>

resistor_band_t *colors(void) {
  resistor_band_t *c = NULL;

  c = (resistor_band_t *)malloc(sizeof(resistor_band_t) * COLORSZ);
  if (c == NULL)
    exit(EXIT_FAILURE);

  for (resistor_band_t i = 0; i < COLORSZ; i++)
    *(c + i) = i;

  return c;
}
