package tip

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

type InvalidDollarStr string

func (txt InvalidDollarStr) Error() string {
	return fmt.Sprintf("dollar: %s should be formatted as $##.##", string(txt))
}

type InvalidPercentStr string

func (txt InvalidPercentStr) Error() string {
	return fmt.Sprintf("percent: %s should be formatted as ##%%", string(txt))
}

// DollarsToFloat accepts a str as input  and returns the amount as float.
// Input should be formatted as $###.##, wherein each # is decimal digit.
// For instance, given $50.00, it should return 50.0
func DollarsToFloat(dollars string) (float32, error) {
	reDollars := regexp.MustCompile(`\$\d{1,3}(\.\d{1,2})?$`)

	if !reDollars.MatchString(dollars) {
		return 0, InvalidDollarStr(dollars)
	}

	dollarsStrParsed := strings.ReplaceAll(dollars, "$", "")
	dollarsParsed, err := strconv.ParseFloat(dollarsStrParsed, 32)

	if err != nil {
		return 0, err
	}

	return float32(dollarsParsed), nil
}

// PercentToFloat accepts a str as input and returns the amount as float.
// Input should be formatted as ##%, wherein each # is a decimal digit.
// For instance, given 15% as input, it should return 0.15
func PercentToFloat(percent string) (float32, error) {
	rePercent := regexp.MustCompile(`\d{1,2}\%$`)

	if !rePercent.MatchString(percent) {
		return 0, InvalidPercentStr(percent)
	}

	percentStrParsed := strings.ReplaceAll(percent, "%", "")
	percentParsed, err := strconv.ParseFloat(percentStrParsed, 32)

	if err != nil {
		return 0, err
	}

	return float32(percentParsed), nil
}

func TipCalculator(dollars string, percent string) (string, error) {
	dollarsFloat, errDollars := DollarsToFloat(dollars)
	percentFloat, errPercent := PercentToFloat(percent)

	if errDollars != nil {
		return "", errDollars
	}

	if errPercent != nil {
		return "", errPercent
	}

	tip := dollarsFloat * (percentFloat/100)

	return "Leave $" + strconv.FormatFloat(float64(tip), 'f', 2, 32), nil
}
