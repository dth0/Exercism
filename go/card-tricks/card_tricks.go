package cards

// GetItem retrieves an item from a slice at given position. The second return value indicates whether
// a the given index existed in the slice or not.
func GetItem(slice []uint8, index int) (uint8, bool) {
	if index >= len(slice) || index < 0 {
		return 0, false
	}

	return slice[index], true
}

// SetItem writes an item to a slice at given position overwriting an existing value.
// If the index is out of range it is be appended.
func SetItem(slice []uint8, index int, value uint8) []uint8 {

	if index >= len(slice) || index < 0 {
		return append(slice, value)
	}

	slice[index] = value

	return slice
}

// PrefilledSlice creates a slice of given length and prefills it with the given value.
func PrefilledSlice(value, length int) []int {

	if length <= 0 {
		return nil
	}

	stack := make([]int, length)

	for i := 0; i < length; i++ {
		stack[i] = value
	}

	return stack

}

// RemoveItem removes an item from a slice by modifying the existing slice.
func RemoveItem(slice []int, index int) []int {
	if index >= len(slice) || index < 0 {
		return slice
	}

	return append(slice[:index], slice[index+1:]...)

}
