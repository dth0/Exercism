package reverse

func Reverse(s string) string {
	word := make([]rune, len(s))

	count := 0
	for _, i := range s {
		word[count] = i
		count++
	}

	word = word[0:count]

	for i := 0; i < count/2; i++ {
		word[i], word[count-1-i] = word[count-1-i], word[i]
	}

	return string(word)
}
