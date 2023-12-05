package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func getCalibrationValues(line string) int {
	digits := map[string]string{
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

	resultString := ""
	temp := ""

	// Replace spelled-out digits with actual digits
	for _, char := range line {
		if !unicode.IsLetter(char) {
			resultString += string(char)
		} else {
			temp += string(char)
			for digit, value := range digits {
				if strings.Contains(temp, digit) {
					resultString += value
					temp = strings.Replace(temp, digit, string(temp[len(temp)-1]), 1)
				}
			}
		}
	}

	// Extract the first and last digits
	firstDigit := resultString[0]
	lastDigit := resultString[len(resultString)-1]

	// Convert to a two-digit number
	calibrationValue := int(firstDigit-'0')*10 + int(lastDigit-'0')

	return calibrationValue
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Calculate calibration values for each line
	var calibrationValues []int
	for _, line := range lines {
		calibrationValues = append(calibrationValues, getCalibrationValues(strings.TrimSpace(line)))
	}

	// Sum up all calibration values
	totalSum := 0
	for _, value := range calibrationValues {
		totalSum += value
	}

	fmt.Printf("The sum of all calibration values is: %d\n", totalSum)
}
