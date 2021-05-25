#include "grade_school.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int compare_data(const void *left, const void *right) {

  student_t *std1 = (student_t *)left;
  student_t *std2 = (student_t *)right;

  if (std1->grade < std2->grade)
    return -1;
  else if (std1->grade > std2->grade)
    return 1;
  return strcmp(std1->name, std2->name);
}

static roster_t roster = {0};

roster_t get_roster(void) { return roster; }

void clear_roster(void) {
  for (int i = 0; i < roster.count; i++) {
    if (roster.students[i].name != NULL)
      free(roster.students[i].name);

    roster.students[i].grade = 0;
  }

  roster.count = 0;
}

bool add_student(char *name, int grade) {
  if (roster.count >= MAX_STUDENTS)
    return false;

  roster.students[roster.count].name = name;
  roster.students[roster.count].grade = grade;

  roster.count++;

  qsort(&roster, roster.count, sizeof(student_t), compare_data);

  return true;
}
