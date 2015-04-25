package main

import (
	"fmt"
)

func main() {
	var n, price int
	var name string
	items := make(map[string]int)
	fmt.Scanln(&n)

	for i := 0; i < n; i++ {
		fmt.Scan(&name)
		fmt.Scan(&price)
		items[name] = price
	}

	for i := 0; i < n; i++ {
		fmt.Scan(&name)
		fmt.Scan(&price)
		diff := price - items[name]
		if diff != 0 {
			fmt.Printf("%s %+d\n", name, diff)
		}
	}
}
