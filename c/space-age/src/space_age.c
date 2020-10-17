#include "space_age.h"
#include <stdint.h>

#define YEAR 31557600.00

const float seconds[] = {0.2408467, 0.61519726, 1.0,       1.8808158,
                         11.862615, 29.447498,  84.016846, 164.79132};

float convert_planet_age(planet_t planet, int64_t input) {

  return input / (YEAR * seconds[planet]);
}
