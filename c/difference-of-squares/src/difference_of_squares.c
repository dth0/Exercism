#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number) {
  return ((number * (number + 1)) * ((2 * number) + 1)) / 6;
}

unsigned int square_of_sum(unsigned int number) {
  unsigned int result = (((1 + number) * number) / 2);
  return result * result;
}
unsigned int difference_of_squares(unsigned int number) {
  return square_of_sum(number) - sum_of_squares(number);
}
