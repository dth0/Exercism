package lasagna

// TODO: define the 'OvenTime()' function

func OvenTime() int {
	return 40
}

// TODO: define the 'RemainingOvenTime()' function

func RemainingOvenTime(time int) int {
	if time < 0 {
		return OvenTime()
	}

	total := OvenTime() - time

	if total < 0 {
		return 0
	}

	return total

}

// TODO: define the 'PreparationTime()' function

func PreparationTime(layer int) int {
	if layer <= 0 {
		return 0
	}

	return layer * 2
}

// TODO: define the 'ElapsedTime()' function

func ElapsedTime(layer, time int) int {
	return time + PreparationTime(layer)
}
