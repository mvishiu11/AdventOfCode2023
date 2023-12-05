package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
	"strings"
)

func main() {
	// Read input from the file
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Create a scanner to read the file line by line
	scanner := bufio.NewScanner(file)
    scanner.Split(bufio.ScanLines)
    for scanner.Scan() {
	   fmt.Println("\n", scanner.Text())
       init_split := strings.Split(scanner.Text(), ":")
	   fmt.Println(init_split[0])
	   fmt.Println(init_split[1])
	   fmt.Println(strings.Split(init_split[0], " ")[1])
	   for _, v := range strings.Split(init_split[1], ";") {
		   fmt.Println(v)
		   for _, v2 := range strings.Split(v, ",") {
			   fmt.Println(v2)
			   for _, v3 := range strings.Split(v2, " ") {
				   fmt.Println(v3)
			   }
		   }
	   }
    }

	file.Close()
}