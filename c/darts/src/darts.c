#include "darts.h"
#include <math.h>

uint8_t score(coordinate_t coordinate) {
  uint8_t retval = 0;

  double distance = sqrt((pow(coordinate.x, 2) + pow(coordinate.y, 2)));

  if (distance <= 1.0)
    retval = 10;
  else if (distance <= 5.0)
    retval = 5;
  else if (distance <= 10)
    retval = 1;

  return retval;
}
