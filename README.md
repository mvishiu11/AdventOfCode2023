# AdventOfCode2023
This repository contains my solutions to Advent of Code 2023. I have chosen to solve those problems using Go (and learn it in the process). I may solve some problems with C/C++ if I feel like it. If a problem will prove too hard to solve with those (since I do not know them all that great) I will probably default to Python.

## Day 1
### Part 1
The first part of the first day was pretty easy. I just had to read the input file and find the first and last integer in each line of the input. I used the `ioutil` package to read the file and wrote my own func to split input lines. I then wrote another function to find the first and last integers by simple `for` loops.

### Part 2
The second part was a bit more tricky. I had to find integers spelled out as their word representation. My initial approach with replacing the words with `strings.ReplaceAll` did not work because of edge cases such as: 

"twone" -> "2ne" instead of "21"

which proved to be a problem when calculating the sum. I wrote a quick program in Python since I am more familiar with it to solve it quickly by using `for` loops to iterate over string char by char and replacing the words with their number representation while leaving the last letter of the word intact. This proved to be a good enough solution for the problem. I then rewrote the solution in Go. My first approach can be seen in `helper.go` file. 
