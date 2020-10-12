#include "isogram.h"

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

#define ASCII_START 97

bool is_isogram(const char phrase[]) {
  char tmp;
  char alphabet[26] = {0};

  if (phrase == NULL)
    return false;

  for (int i = 0; phrase[i] != '\0'; i++) {
    tmp = tolower(phrase[i]);
    if (!isalpha(tmp))
      continue;

    int pos = tmp - ASCII_START;

    if (alphabet[pos] >= 1)
      return false;

    alphabet[pos]++;
  }

  return true;
}
