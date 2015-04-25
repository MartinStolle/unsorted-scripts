package main

import (
	"fmt"
	"strings"
)

var braille = map[string]string{
        "O.....": "a",
        "O.O...": "b",
        "OO....": "c",
        "OO.O..": "d",
        "O..O..": "e",
        "OOO...": "f",
        "OOOO..": "g",
        "O.OO..": "h",
        ".OO...": "i",
        ".OOO..": "j",
        "O...O.": "k",
        "O.O.O.": "l",
        "OO..O.": "m",
        "OO.OO.": "n",
        "O..OO.": "o",
        "OOO.O.": "p",
        "OOOOO.": "q",
        "O.OOO.": "r",
        ".OO.O.": "s",
        ".OOOO.": "t",
        "O...OO": "u",
        "O.O.OO": "v",
        ".OOO.O": "w",
        "OO..OO": "x",
        "OO.OOO": "y",
        "O..OOO": "z",
}

func main() {
        fmt.Println("Enter braille, stop with q!")

        var input string
	// a := make([]string, 1)

        for {
                n, err := fmt.Scan(&input)
		fmt.Println(input)
		foo := strings.Fields(input)
		fmt.Println(len(foo))

                if err != nil || n != 1 {
			break
                }

                if input == "q" {
			break
                } else {
			// a = append(a, input)
			// fmt.Println(a)
		}
        }
}
