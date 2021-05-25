#include "nucleotide_count.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define exit_error(msg)                                                        \
  do {                                                                         \
    perror(msg);                                                               \
    exit(EXIT_FAILURE);                                                        \
  } while (0)

char *count(const char *dna_strand) {
  char DNA[4] = {0};
  const char *p = dna_strand;

  char *buffer = (char *)malloc(BUFSIZ);
  if (buffer == NULL)
    exit_error("Error to allocate memory");

  if (dna_strand == NULL)
    goto empty;

  memset(buffer, 0, BUFSIZ);

  while (*p != '\0') {
    int pos = 0;
    switch (*p) {
    case 'A':
      pos = 0;
      break;
    case 'C':
      pos = 1;
      break;
    case 'G':
      pos = 2;
      break;
    case 'T':
      pos = 3;
      break;
    default:
      goto empty;
    }

    DNA[pos]++;
    p++;
  }

  sprintf(buffer, "A:%d C:%d G:%d T:%d", DNA[0], DNA[1], DNA[2], DNA[3]);

  return buffer;
empty:
  buffer[0] = '\0';

  return buffer;
}
