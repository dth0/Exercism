#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H
   
#include <sys/types.h>

#define OHMS 0
#define KILOOHMS 1

typedef enum {
  BLACK,
  BROWN,
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  BLUE,
  VIOLET,
  GREY,
  WHITE,
} resistor_band_t;

typedef struct {
        u_int16_t value;
        u_int8_t unit;
} resistor_value_t;

resistor_value_t color_code(resistor_band_t *colors);

#endif
