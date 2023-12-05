package main

import (
	"fmt"
	"strings"
	"io/ioutil"
	"log"
)

func convertStringToInt(str string) string {
	// Define a mapping of string representations to integers
	numberMapping := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
	}

	// Loop through the mapping and replace occurrences in the string
	for key, value := range numberMapping {
		str = strings.ReplaceAll(str, key, value)
	}

	return str
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

func main() {
	content, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	// Convert byte slice to string
	input := string(content)

	for _, line := range splitLines(input) {
		// Find the first and last digits
		line = convertStringToInt(line)
	}

	fmt.Println(input)
}
