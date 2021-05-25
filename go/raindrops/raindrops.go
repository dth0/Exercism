package raindrops

import "fmt"

var numTable = map[int]string{
	3: "Pling",
	5: "Plang",
	7: "Plong",
}

func Convert(number int) string {

	var result string

	for k, v := range numTable {
		if number%k == 0 {
			result += v
		}
	}

	if len(result) == 0 {
		result = fmt.Sprintf("%d", number)
	}

	return result
}
