package clock

import (
	"fmt"
)

type Clock struct {
	hour   int
	minute int
}

func New(hour, minute int) Clock {
	delta_h := minute / 60
	delta_m := minute % 60

	if delta_m < 0 {
		delta_h--
		minute = delta_m + 60
	}

	hour = (hour + delta_h) % 24

	if hour < 0 {
		hour += 24
	}

	minute %= 60

	return Clock{
		hour:   hour,
		minute: minute,
	}

}

func (c Clock) String() string {
	return fmt.Sprintf("%.2d:%.2d", c.hour, c.minute)
}

func (c Clock) Add(minutes int) Clock {
	return New(c.hour, c.minute+minutes)
}

func (c Clock) Subtract(minutes int) Clock {
	return New(c.hour, c.minute-minutes)
}
