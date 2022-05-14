// Package weather is used to log city's weather
package weather

var (
	// CurrentCondition keeps track of the condition of the city
	CurrentCondition string

	// CurrentLocation keeps the city location
	CurrentLocation string
)

// Log just return an string '<city> - current weather condition: <condition>'
func Log(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
