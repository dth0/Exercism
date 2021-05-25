// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package bob should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package bob

import (
	"strings"
)

var answer = [...]string{
	"Sure.",
	"Whoa, chill out!",
	"Calm down, I know what I'm doing!",
	"Fine. Be that way!",
	"Whatever.",
}

const alpha = "abcdefghijklmnopqrstuvwxyz"

// Hey should have a comment documenting it.
func Hey(remark string) string {

	isQuestion := strings.HasSuffix(strings.TrimSpace(remark), "?")

	newRemark := strings.TrimFunc(remark, func(r rune) bool {
		return !strings.Contains(alpha, strings.ToLower(string(r)))
	})

	if len(strings.TrimSpace(remark)) == 0 {
		return answer[3]
	}

	isUpper := newRemark == strings.ToUpper(newRemark) && len(newRemark) > 0

	if isQuestion {
		if isUpper {
			return answer[2]
		}

		return answer[0]
	}

	if isUpper {
		return answer[1]
	}

	return answer[4]
}
