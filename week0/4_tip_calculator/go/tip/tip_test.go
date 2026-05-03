package tip

import (
	"errors"
	"testing"
)

var dollarError InvalidDollarStr
var percentError InvalidPercentStr

func TestInvalidDollarsString(t *testing.T) {
	_, err := DollarsToFloat("$ 7.50")

	if err == nil {
		t.Error()
	}

	if !errors.As(err, &dollarError) {
		t.Error(err)
	}
}

func TestInvalidPercentString(t *testing.T) {
	_, err := PercentToFloat("5 %")

	if err == nil {
		t.Error()
	}

	if !errors.As(err, &percentError) {
		t.Error(err)
	}
}

func Test5DollarsToFloat(t *testing.T) {
	dollars, _ := DollarsToFloat("$5")
	dollarsExp := float32(5)
	if dollars != dollarsExp {
		t.Errorf("%f should be %f", dollars, dollarsExp)
	}
}

func Test5PercentToFloat(t *testing.T) {
	percent, _ := PercentToFloat("5%")
	percentExp := float32(5)
	if percent != percentExp {
		t.Errorf("%f should be %f", percent, percentExp)
	}
}

func Test50Dollars15Percent(t *testing.T) {
	tipStr, _ := TipCalculator("$50", "15%")
	tipStrExp := "Leave $7.50"
	if tipStr != tipStrExp {
		t.Errorf("%s should be %s", string(tipStr), string(tipStrExp))
	}
}

func Test100Dollars18Percent(t *testing.T) {
	tipStr, _ := TipCalculator("$100.00", "18%")
	tipStrExp := "Leave $18.00"
	if tipStr != tipStrExp {
		t.Errorf("%s should be %s", string(tipStr), string(tipStrExp))
	}
}

func Test15Dollars25Percent(t *testing.T) {
	tipStr, _ := TipCalculator("$15.00", "25%")
	tipStrExp := "Leave $3.75"
	if tipStr != tipStrExp {
		t.Errorf("%s should be %s", string(tipStr), string(tipStrExp))
	}
}
