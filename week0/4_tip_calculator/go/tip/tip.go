package tip

import "fmt"

type InvalidDollarStr string

func (txt InvalidDollarStr) Error() string {
	return fmt.Sprintf("dollar: %s should be formatted as $##.##", string(txt))
}

type InvalidPercentStr string

func (txt InvalidPercentStr) Error() string {
	return fmt.Sprintf("percent: %s should be formatted as ##%%", string(txt))
}

// DollarsToFloat accepts a str as input  and returns the amount as float.
// Input should be formatted as $##.##, wherein each # is decimal digit.
// For instance, given $50.00, it should return 50.0
func DollarsToFloat(dollars string) (float32, error) {
	return 0.0, nil;
}

// PercentToFloat accepts a str as input and returns the amount as float.
// Input should be formatted as ##%, wherein each # is a decimal digit.
// For instance, given 15% as input, it should return 0.15
func PercentToFloat(percent string) (float32, error) {
	return 0.0, nil
}

func TipCalculator(dollars string, percent string) (string, error) {
	return "", nil
}