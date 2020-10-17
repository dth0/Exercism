#include "pangram.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define ALPHASZ 26

bool is_pangram(const char *sentence) {

  char bucket[ALPHASZ] = {0};
  int size = 0;

  if (sentence == NULL || sentence[0] == '\0')
    return false;

  for (size_t i = 0; i < strlen(sentence); i++) {

    char ch = *(sentence + i);

    if (!isalpha(ch))
      continue;

    int pos = tolower(ch) - 97;

    if (bucket[pos] == 0) {
      bucket[pos] = 1;
      size++;
    }
  }

  return (size == ALPHASZ) ? true : false;
}
