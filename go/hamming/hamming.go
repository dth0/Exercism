package hamming

import "errors"

func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return 0, errors.New("different size")
	}

	var length int = 0

	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			length++
		}
	}

	return length, nil
}
