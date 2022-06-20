package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, avg int) int {
	if avg <= 0 {
		avg = 2
	}

	return len(layers) * avg
}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (int, float64) {
	var (
		noodles int
		sauce   float64
	)

	for _, item := range layers {
		switch item {
		case "noodles":
			noodles += 50
		case "sauce":
			sauce += 0.2

		}
	}

	return noodles, sauce
}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendList, myList []string) {
	if len(friendList) == 0 {
		return
	}

	secretItem := friendList[len(friendList)-1]
	myList[len(myList)-1] = secretItem
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(amounts []float64, portions int) []float64 {
	result := make([]float64, len(amounts))

	for index, value := range amounts {
		result[index] = (value * float64(portions)) / 2.0
	}

	return result
}
