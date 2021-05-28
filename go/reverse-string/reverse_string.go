package reverse

func Reverse(s string) string {
	word := []rune(s)

	for i := 0; i < len(word)/2; i++ {
		word[len(word)-1-i], word[i] = word[i], word[len(word)-1-i]
	}

	return string(word)
}
