#define _GNU_SOURCE
#include "acronym.h"
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER 4096

char *abbreviate(const char *phrase) {

  char acronym[BUFFER] = {0};
  int control = 0;
  int pos = 0;

  if (phrase == NULL || phrase[0] == '\0')
    return NULL;

  for (size_t i = 0; i < strlen(phrase); i++) {
    char ch = phrase[i];

    if (ch == ' ' || ch == '-') {
      control = 0;
    } else if (control == 0 && isalpha(ch)) {
      acronym[pos] = toupper(ch);
      control = 1;
      pos++;
    }
  }

  return strndup(acronym, strlen(acronym));
}
