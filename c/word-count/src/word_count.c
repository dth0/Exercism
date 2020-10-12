#define _DEFAULT_SOURCE
#include "word_count.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static size_t fix_word(char **word) {
  int pos = 0;

  size_t word_s = strlen(*word);

  for (size_t i = 0; i < word_s; i++) {
    char ch = *((*word) + i);

    if (!isalnum(ch) && ch != '\'')
      continue;

    if (ch == '\'' && (i == 0 || i == word_s - 1))
      continue;

    if (isalpha(ch))
      ch = tolower(ch);

    *((*word) + pos) = ch;

    pos++;
  }

  *((*word) + pos) = '\0';

  return strlen(*word);
}

int word_count(const char *input_text, word_count_word_t *words) {

  int count_s = 0;
  char *word = NULL;
  char *string = strndup(input_text, strlen(input_text));

  memset(words, 0, sizeof(word_count_word_t));

  while ((word = strsep(&string, " \n\t,")) != NULL) {
    if (*word == '\0')
      continue;

    size_t size = fix_word(&word);

    if (size > MAX_WORD_LENGTH)
      return EXCESSIVE_LENGTH_WORD;

    bool found = false;
    for (int i = 0; i < count_s; i++) {
      if (strcmp(word, (words + i)->text) == 0) {
        (words + i)->count++;
        found = true;
        break;
      }
    }

    if (count_s == MAX_WORDS && found == false) {
      return EXCESSIVE_NUMBER_OF_WORDS;

    } else if (found == false) {
      strncpy((words + count_s)->text, word, size);
      (words + count_s)->count++;
      count_s++;
    }
  }

  return count_s;
}
