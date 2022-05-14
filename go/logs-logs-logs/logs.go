package logs

import (
	"fmt"
	"strings"
)

// Message extracts the message from the provided log line.
func Message(line string) string {

	msg := strings.Split(line, ":")

	return strings.TrimSpace(msg[1])

}

// MessageLen counts the amount of characters (runes) in the message of the log line.
func MessageLen(line string) int {
	msg := Message(line)
	return len([]rune(msg))
}

// LogLevel extracts the log level string from the provided log line.
func LogLevel(line string) string {
	msg := strings.Split(line, ":")

	return strings.ToLower(strings.Trim(msg[0], "[]"))
}

// Reformat reformats the log line in the format `message (logLevel)`.
func Reformat(line string) string {
	msg := Message(line)
	level := LogLevel(line)

	return fmt.Sprintf("%s (%s)", msg, level)
}
