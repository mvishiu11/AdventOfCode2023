package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"unicode"
)

func main() {
	// Read input from the file
	content, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	// Convert byte slice to string
	input := string(content)

	// Calculate the sum of calibration values
	sum := calculateSum(input)

	// Print the result
	fmt.Println("The sum of all calibration values is:", sum)
}

func calculateSum(input string) int {
	var sum int

	// Iterate through each line in the input
	for _, line := range splitLines(input) {
		// Find the first and last digits
		firstDigit, lastDigit := findFirstAndLastDigits(line)

		// Convert characters to integers
		firstDigitInt := int(firstDigit - '0')
		lastDigitInt := int(lastDigit - '0')

		// Combine digits to form a two-digit number
		calibrationValue := firstDigitInt*10 + lastDigitInt

		// Add the calibration value to the sum
		sum += calibrationValue
	}

	return sum
}

func splitLines(s string) []string {
	var lines []string
	var currentLine []rune

	for _, char := range s {
		if char == '\n' {
			lines = append(lines, string(currentLine))
			currentLine = nil
		} else {
			currentLine = append(currentLine, char)
		}
	}

	if len(currentLine) > 0 {
		lines = append(lines, string(currentLine))
	}

	return lines
}

func findFirstAndLastDigits(s string) (rune, rune) {
	var firstDigit, lastDigit rune

	// Find the first digit
	for _, char := range s {
		if unicode.IsDigit(char) {
			firstDigit = char
			break
		}
	}

	// Find the last digit
	for i := len(s) - 1; i >= 0; i-- {
		if unicode.IsDigit(rune(s[i])) {
			lastDigit = rune(s[i])
			break
		}
	}

	return firstDigit, lastDigit
}
