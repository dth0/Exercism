package grains

import (
	"errors"
	"math"
)

func Square(square int) (uint64, error) {
	if square <= 0 || square > 64 {
		return 0, errors.New("square must be between 1-64")
	}
	return uint64(math.Pow(2, float64(square-1))), nil
}

func Total() uint64 {
	return ^uint64(0)
}
