package luhn

import (
	"strconv"
	"strings"
)

func Valid(s string) bool {

	var (
		total int
		j     int
	)

	code := strings.ReplaceAll(s, " ", "")
	numbers := make([]int, len(code))

	if len(code) <= 1 {
		return false
	}

	for i, v := range code {

		number, err := strconv.Atoi(string(v))
		if err != nil {
			return false
		}

		numbers[i] = number

	}

	for i := len(code) - 1; i >= 0; i-- {
		if (j % 2) == 0 {
			total += numbers[i]
		} else {
			total += calc(numbers[i])
		}
		j++

	}

	return (total % 10) == 0
}

func calc(n int) int {
	result := n * 2

	if result > 9 {
		result -= 9
	}

	return result
}
