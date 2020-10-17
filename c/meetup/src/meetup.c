#define _XOPEN_SOURCE
#include "meetup.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <time.h>

#define DAY_SEC 86400

#define WEEK_DAYS 7

#define POSITIONS 5

char *week_days[] = {
    "sunday",   "monday", "tuesday",  "wednesday",
    "thursday", "friday", "saturday",
};

char *positions[] = {"first", "second", "third", "fourth", "fifth"};

static int find_item(const char *word, char **list, size_t size) {

  size_t word_s = strlen(word);

  for (size_t i = 0; i < size; i++) {

    const char *w = *(list + i);

    if (strlen(w) != word_s)
      continue;

    if (strcasecmp(w, word) == 0)
      return i;
  }

  return -1;
}

static int get_list_of_days(unsigned int year, unsigned int month, int week_day,
                            struct tm *time_ptr) {

  int count = 0;
  struct tm time_date;

  char buffer[BUFSIZ] = {0};

  sprintf(buffer, "%u-%u-1\n", year, month);
  strptime(buffer, "%Y-%m-%d", &time_date);

  do {
    time_t t = mktime(&time_date);

    while (time_date.tm_wday != week_day) {
      t += DAY_SEC;
      time_date = *(localtime(&t));
    }

    memcpy(time_ptr + count, &time_date, sizeof(struct tm));
    count++;

    t += DAY_SEC * WEEK_DAYS;
    time_date = *(localtime(&t));

  } while (time_date.tm_mon == (int)(month - 1));

  return count;
}

int meetup_day_of_month(unsigned int year, unsigned int month, const char *week,
                        const char *day_of_week) {

  int week_day = find_item(day_of_week, week_days, WEEK_DAYS);
  if (week_day == -1)
    return -1;

  struct tm timed[6];

  int days = get_list_of_days(year, month, week_day, timed);

  if (strcmp("first", week) == 0)
    return timed[0].tm_mday;
  else if (strcmp("last", week) == 0)
    return timed[days - 1].tm_mday;
  else if (strcmp("teenth", week) == 0) {
    int ret;
    for (int i = 0; i < days; i++) {
      if (timed[i].tm_mday >= 10 && timed[i].tm_mday < 20)
        ret = timed[i].tm_mday;
    }

    return ret;
  }

  int w = find_item(week, positions, POSITIONS);
  if (w == -1)
    return -1;

  return (w >= days) ? 0 : timed[w].tm_mday;
}
