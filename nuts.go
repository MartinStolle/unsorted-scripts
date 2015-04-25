    package main
    
    import (
    	"bufio"
    	"fmt"
    	"os"
    	"strconv"
    	"strings"
    )
    
    type Inventory struct {
    	item string
    	cost int
    }
    
    func main() {
    	inventory := make([]map[string]int, 2)
    	// initialize maps
    	for i := range inventory {
    		inventory[i] = make(map[string]int)
    	}
    
    	count, rows, item := 0, 0, 0
    	var err error
    
    	scanner := bufio.NewScanner(os.Stdin)
    
    	fmt.Println("How many rows for each list?")
    	for scanner.Scan() {
    		scanned_text := scanner.Text()
    		if rows == 0 {
    			// get the number of rows
    			rows, err = strconv.Atoi(scanned_text)
    			if err != nil {
    				// handle error
    				fmt.Println("Please enter a valid number")
    			}
    			count = rows
    		} else {
    			if count == 0 {
    				count = rows
    				item++
    			}
    
    			splitted := strings.Fields(scanned_text)
    			if len(splitted) != 2 {
    				fmt.Println("Missing argument")
    				continue
    			}
    
    			// convert the string price to int
    			nr, err := strconv.Atoi(splitted[1])
    			if err != nil {
    				// handle error
    				fmt.Println("Please enter a valid number")
    				continue
    			}
    
    			// add the new inventory to our list
    			inventory[item][splitted[0]] = nr
    			count--
    		}
    
    		// we have all the information we need
    		if len(inventory) == 2 && len(inventory[0]) == rows && len(inventory[1]) == rows {
    			break
    		}
    
    	}
    
    	for k, _ := range inventory[0] {
    		difference := inventory[1][k] - inventory[0][k]
    		if difference != 0 {
    			fmt.Println("k:", k, "v:", difference)
    		}
    	}
    }
