#include "grains.h"
#include <math.h>
#include <stdint.h>
#include <stdio.h>

#define MAXSQR 64

uint64_t total(void) { return UINT64_MAX; }

uint64_t square(uint8_t index) {
  return (index > MAXSQR || index <= 0) ? 0 : (uint64_t)1 << (index - 1);
}
