package zero

// EmptyBool returns an empty (zero value) bool
func EmptyBool() bool {
	var b bool
	return b
}

// EmptyInt returns an empty (zero value) int
func EmptyInt() int {
	var i int
	return i
}

// EmptyString returns an empty (zero value) string
func EmptyString() string {
	var v string
	return v
}

// EmptyFunc returns an empty (zero value) func
func EmptyFunc() func() {
	return nil
}

// EmptyPointer returns an empty (zero value) pointer
func EmptyPointer() *int {
	return nil
}

// EmptyMap returns an empty (zero value) map
func EmptyMap() map[int]int {
	return nil
}

// EmptySlice returns an empty (zero value) slice
func EmptySlice() []int {
	return nil
}

// EmptyChannel returns an empty (zero value) channel
func EmptyChannel() chan int {
	var c chan int
	return c
}

// EmptyInterface returns an empty (zero value) interface
func EmptyInterface() interface{} {
	var i interface{}
	return i
}
