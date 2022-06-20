package parsinglogfiles

import (
	"fmt"
	"regexp"
)

func IsValidLine(text string) bool {
	matched, err := regexp.MatchString(`^\[(ERR|TRC|DBG|INF|WRN|FTL)\]`, text)
	if err != nil {
		return false
	}

	return matched
}

func SplitLogLine(text string) []string {
	re := regexp.MustCompile(`(?:<[*~=-]*>)`)
	return re.Split(text, -1)
}

func CountQuotedPasswords(lines []string) int {
	var (
		count = 0
		re    = regexp.MustCompile(`(?i)\".*password.*\"`)
	)

	for _, line := range lines {
		count += len(re.FindAllString(line, -1))
	}

	return count
}

func RemoveEndOfLineText(text string) string {
	re := regexp.MustCompile(`end-of-line\d+`)
	return re.ReplaceAllString(text, "")
}

func TagWithUserName(lines []string) []string {
	var (
		result = make([]string, len(lines))
		re     = regexp.MustCompile(`User\s+(\S+)`)
	)

	for index, line := range lines {
		resp := re.FindStringSubmatch(line)
		if resp != nil {
			result[index] = fmt.Sprintf("[USR] %s %s", resp[1], line)
		} else {
			result[index] = line
		}

	}

	return result
}
