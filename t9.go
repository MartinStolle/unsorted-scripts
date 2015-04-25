package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	charset map[int][]byte = map[int][]byte{
		2: []byte{'a', 'b', 'c'},
		3: []byte{'d', 'e', 'f'},
		4: []byte{'g', 'h', 'i'},
		5: []byte{'j', 'k', 'l'},
		6: []byte{'m', 'n', 'o'},
		7: []byte{'p', 'q', 'r', 's'},
		8: []byte{'t', 'u', 'v'},
		9: []byte{'w', 'x', 'y', 'z'},
	}
	dict *bufio.Scanner
)

func init() {
	file, err := os.Open("brit-a-z.txt")

	if err != nil {
		fmt.Println("Could not open dictionary. QQ.")
		os.Exit(1)
	}

	dict = bufio.NewScanner(file)
}

func findWords(knownchars string) {
	dict.Split(bufio.ScanLines)
	for dict.Scan() {
		if strings.Index(dict.Text(), knownchars) == 0 {
			fmt.Printf("%s\n", dict.Text())
		}
	}
}

func main() {
	var (
		input []string = strings.Split("7777 666 555 3", " ")
		str   []string
	)

	// with split, count & search
	for _, v := range input {
		c, _ := strconv.Atoi(string(v[0]))
		n := strings.Count(v, string(v[0])) - 1
		str = append(str, string(charset[c][n]))
	}

	findWords(strings.Join(str, ""))
}
