package scrabble

import (
	"strings"
	"unicode"
)

var wordList = map[string]int{
	"AEIOULNRST": 1,
	"DG":         2,
	"BCMP":       3,
	"FHVWY":      4,
	"K":          5,
	"JX":         8,
	"QZ":         10,
}

func Score(word string) int {
	var (
		cache      = map[rune]int{}
		result int = 0
	)

	for _, letter := range word {

		letter = unicode.ToUpper(letter)

		value, ok := cache[letter]
		if ok {
			result += value
			continue
		}

		for k, v := range wordList {
			if strings.ContainsRune(k, letter) {
				cache[letter] = v
				result += v
				break

			}
		}

	}

	return result
}
