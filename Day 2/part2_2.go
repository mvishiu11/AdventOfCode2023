package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
	"strings"
	"strconv"
	"math"
)

type Entry struct {
	amount int
	color  string
}

func New(amount int, color string) Entry {
	return Entry{amount, color}
}

type Set struct {
	entries []Entry
}

type Game struct {
	id   int
	sets []Set
}

func main() {
	// Read input from the file
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var games []Game 

	// Create a scanner to read the file line by line
	scanner := bufio.NewScanner(file)
    scanner.Split(bufio.ScanLines)
    for scanner.Scan() {
       games = append(games, parseGame(scanner.Text()))
    }

	// Part 2: Finding the sum of powers
	powerSum := calculatePowerSum(games)
	fmt.Println("Sum of powers of minimum sets is:", powerSum)

	file.Close()
}

func parseGame(line string) Game {
	var game Game

	init_split := strings.Split(line, ":")
	id, _ := strconv.Atoi(strings.Split(init_split[0], " ")[1])
	game.id = id


	for _, set := range strings.Split(init_split[1], ";") {
		var sett Set
		for _, entry := range strings.Split(set, ",") {
			amount, color := strings.Split(entry, " ")[1], strings.Split(entry, " ")[2]
			amount_int, _ := strconv.Atoi(amount)
			sett.entries = append(sett.entries, New(amount_int, color))
		}
		game.sets = append(game.sets, sett)
	}

	return game
}

func calculatePowerGame(game Game) int {
	redMin, greenMin, blueMin := 0, 0, 0
	for _, set := range game.sets {
		for _, entry := range set.entries {
			switch entry.color {
			case "red":
				redMin = int(math.Max(float64(entry.amount), float64(redMin)))
			case "green":
				greenMin = int(math.Max(float64(entry.amount), float64(greenMin)))
			case "blue":
				blueMin = int(math.Max(float64(entry.amount), float64(blueMin)))
			}
		}
	}
	return redMin * greenMin * blueMin
}

func calculatePowerSum(games []Game) int {
	sum := 0
	for _, game := range games {
		sum += calculatePowerGame(game)
	}
	return sum
}