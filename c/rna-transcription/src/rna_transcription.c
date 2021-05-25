#include "rna_transcription.h"

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define DNASZ 4

const char DNA[] = "GCTA";
const char RNA[] = "CGAU";

char *to_rna(const char *dna) {

  if (dna == NULL)
    return NULL;

  size_t dna_size = strlen(dna);

  char *ret = (char *)malloc(dna_size + 1);
  if (ret == NULL)
    return NULL;

  char *p = (char *)dna;
  int r = 0;

  while (*p != '\0') {
    bool found = false;
    for (size_t i = 0; i < DNASZ; i++) {
      if (*p == DNA[i]) {
        ret[r] = RNA[i];
        found = true;
        r++;
        break;
      }
    }

    if (!found)
      goto cleanup;

    p++;
  }

  ret[r] = '\0';

  return ret;

cleanup:
  free(ret);
  return NULL;
}
