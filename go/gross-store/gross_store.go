package gross

// Units store the Gross Store unit measurement
func Units() map[string]int {
	return map[string]int{
		"quarter_of_a_dozen": 3,
		"half_of_a_dozen":    6,
		"dozen":              12,
		"small_gross":        120,
		"gross":              144,
		"great_gross":        1728,
	}
}

// NewBill create a new bill
func NewBill() map[string]int {
	return make(map[string]int)
}

// AddItem add item to customer bill
func AddItem(bill map[string]int, units map[string]int, item string, unit string) bool {
	valueUnit, ok := units[unit]

	if !ok {
		return false
	}

	bill[item] = valueUnit

	return true
}

// RemoveItem remove item from customer bill
func RemoveItem(bill map[string]int, units map[string]int, item string, unit string) bool {
	unitValue, ok := units[unit]
	if !ok {
		return false
	}

	itemValue, ok := bill[item]
	if !ok {
		return false
	}

	total := itemValue - unitValue

	if total < 0 {
		return false
	} else if total == 0 {
		delete(bill, item)
	} else {
		bill[item] -= unitValue
	}

	return true

}

// GetItem return the quantity of item that the customer has in his/her bill
func GetItem(bill map[string]int, item string) (int, bool) {
	itemValue, ok := bill[item]
	return itemValue, ok
}
