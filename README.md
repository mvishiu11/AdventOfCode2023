# AdventOfCode2023
This repository contains my solutions to <a style=text-decoration:none href="https://adventofcode.com/2023">Advent of Code 2023</a>. I have chosen to solve those problems using Go (and learn it in the process). I may solve some problems with C/C++ if I feel like it. If a problem will prove too hard to solve with those (since I do not know them all that great) I will probably default to Python.

## Progress
| Day | Part 1 | Part 2 |
|:---:|:------:|:------:|
|  1  |   ✔️   |   ✔️   |
|  2  |   ✔️   |   ✔️   |

## Quick navigation
- [Day 1](#day-1)
  - [Part 1](#part-1)
  - [Part 2](#part-2)
- [Day 2](#day-2)
    - [Part 1](#part-1-1)
    - [Part 2](#part-2-1)


## Day 1
### Part 1
The first part of the first day was pretty easy. I just had to read the input file and find the first and last integer in each line of the input. I used the `ioutil` package to read the file and wrote my own func to split input lines. I then wrote another function to find the first and last integers by simple `for` loops.

### Part 2
The second part was a bit more tricky. I had to find integers spelled out as their word representation. My initial approach with replacing the words with `strings.ReplaceAll` did not work because of edge cases such as: 

"twone" -> "2ne" instead of "21"

which proved to be a problem when calculating the sum. I wrote a quick program in Python since I am more familiar with it to solve it quickly by using `for` loops to iterate over string char by char and replacing the words with their number representation while leaving the last letter of the word intact. This proved to be a good enough solution for the problem. I then rewrote the solution in Go. My first approach can be seen in `helper.go` file.

## Day 2
### Part 1
The first part took me a little bit of time, mostly because of a weird quirk of splitting in Go - when you split the following string " 2 red" it splits into **3** elements: "", "2" and "red". Other than that, it was pretty straigthforward. I got to know the OOP side of Go (if you can call it that) a bit better. 

### Part 2
The second part was actually fairly easy, after I figured out the splitting in the previous part. I just added some new functions to calculate minimum number of cubes per color and called them in corresponding `for` loops. *Easy peasy*
