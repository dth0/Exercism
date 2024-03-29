package thefarm

import (
	"errors"
	"fmt"
)

// See types.go for the types defined for this exercise.

// TODO: Define the SillyNephewError type here.
type SillyNephewError struct {
	number int
}

func (s *SillyNephewError) Error() string {
	return fmt.Sprintf("silly nephew, there cannot be %d cows", s.number)
}

// DivideFood computes the fodder amount per cow for the given cows.
func DivideFood(weightFodder WeightFodder, cows int) (float64, error) {
	fodder, err := weightFodder.FodderAmount()
	if err != nil {
		if errors.Is(err, ErrScaleMalfunction) {
			if fodder > 0 {
				fodder *= 2
			}
		} else {
			return 0, err
		}
	}

	if fodder < 0 {
		return 0, errors.New("negative fodder")
	}

	if cows == 0 {
		return 0, errors.New("division by zero")
	} else if cows < 0 {
		return 0, &SillyNephewError{
			number: cows,
		}
	}

	return fodder / float64(cows), nil
}
