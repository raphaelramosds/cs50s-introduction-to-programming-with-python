package main

func Deep(userAnswer string) string {
	if userAnswer == "42" || userAnswer == "Forty Two" || userAnswer == "forty-two" {
		return "Yes"
	} 
	return "No"
}
