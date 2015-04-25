    package main
    
    import (
            "bufio"
            "fmt"
            "os"
            "regexp"
            "strings"
    )
    
    var braille = map[string]string{
            "0.....": "a",
            "0.0...": "b",
            "00....": "c",
            "00.0..": "d",
            "0..0..": "e",
            "000...": "f",
            "0000..": "g",
            "0.00..": "h",
            ".00...": "i",
            ".000..": "j",
            "0...0.": "k",
            "0.0.0.": "l",
            "00..0.": "m",
            "00.00.": "n",
            "0..00.": "o",
            "000.0.": "p",
            "00000.": "q",
            "0.000.": "r",
            ".00.0.": "s",
            ".0000.": "t",
            "0...00": "u",
            "0.0.00": "v",
            ".000.0": "w",
            "00..00": "x",
            "00.000": "y",
            "0..000": "z",
    }

    func isValid(input string) bool {
            // check if only valid symbols are used . or 0
            var valid_braille = regexp.MustCompile(`^([\.0]{2}\s?)+$`)
            return valid_braille.MatchString(input)
    }
    
    func main() {
            input := make([][]string, 0)
            scanner := bufio.NewScanner(os.Stdin)
            for scanner.Scan() {
                    if isValid(scanner.Text()) == false {
                            fmt.Println("Invalid braille.")
                            break
                    }
                    splitted := strings.Fields(scanner.Text())
                    if len(input) > 0 {
                            braille_length := len(input[len(input)-1])
                            if braille_length != len(splitted) {
                                    fmt.Println("Rows have different sizes")
                                    break
                            }
                    }
    
                    input = append(input, splitted)
                    // braille consists of 3 rows, therefore stop
                    // after we have all input we need
                    if len(input) == 3 {
                            break
                    }
            }
    
            if len(input) == 3 {
                    decoded := make([]string, 0)
                    for i := range input[0] {
                            tmp_braille := make([]string, 0)
                            tmp_braille = append(tmp_braille, input[0][i])
                            tmp_braille = append(tmp_braille, input[1][i])
                            tmp_braille = append(tmp_braille, input[2][i])
                            result := strings.Join(tmp_braille, "")
                            decoded = append(decoded, braille[result])
                    }
                    fmt.Println(strings.Join(decoded, ""))
            }
    
            if err := scanner.Err(); err != nil {
                    fmt.Fprintln(os.Stderr, "reading standard input:", err)
            }
    }
