#include "gigasecond.h"

#include <math.h>
#include <time.h>

time_t gigasecond_after(time_t time) { return time + pow(10, 9); }
