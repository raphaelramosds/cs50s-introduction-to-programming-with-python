package indoor

import "testing"

func TestHELLO(t *testing.T) {
	txt := Indoor("HELLO")
	if txt != "hello" {
		t.Errorf("%s should be lowercase", txt)
	}
}