package main

import (
	"testing"
)

func Test42(t *testing.T) {
	answer := Deep("42")
	if answer != "Yes" {
		t.Error()
	}
}


func TestFortyTwo(t *testing.T) {
	answer := Deep("Forty Two")
	if answer != "Yes" {
		t.Error()
	}
}

func TestForty_two(t *testing.T) {
	answer := Deep("forty-two")
	if answer != "Yes" {
		t.Error()
	}
}

func Test50(t *testing.T) {
	answer := Deep("50")
	if answer != "No" {
		t.Error()
	}
}
