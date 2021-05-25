package isogram

import "unicode"

func IsIsogram(s string) bool {

	var alphabet [26]uint8

	for _, char := range s {
		pos := unicode.ToLower(char) - 'a'

		if pos < 0 || pos >= 26 {
			continue
		}

		if alphabet[pos] >= 1 {
			return false
		}

		alphabet[pos]++
	}

	return true

}
