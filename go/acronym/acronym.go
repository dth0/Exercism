// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package acronym should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package acronym

import (
	"strings"
	"unicode"
)

// Abbreviate should have a comment documenting it.
func Abbreviate(s string) string {
	// Write some code here to pass the test suite.
	// Then remove all the stock comments.
	// They're here to help you get started but they only clutter a finished solution.
	// If you leave them in, reviewers may protest!

	letters := make([]rune, 0)

	for _, v := range strings.FieldsFunc(s, split_text) {
		if len(v) == 0 {
			continue
		}

		tmp := strings.TrimFunc(v, func(r rune) bool {
			return !unicode.IsLetter(r)
		})

		letters = append(letters, rune(tmp[0]))
	}

	return strings.ToUpper(string(letters))
}

func split_text(r rune) bool {
	return r == ' ' || r == '-'
}
