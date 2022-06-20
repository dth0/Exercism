package anagram

func Detect(subject string, candidates []string) []string {
	var (
		bucket = make(map[rune]int)
		ret    = make([]string, 0)
	)

	for _, v := range subject {
		bucket[v]++
	}

	for _, v := range candidates {
		check := func() {
		}
	}
}
