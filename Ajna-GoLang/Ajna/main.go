package main

import (
    "fmt"
    "os"
    "strings"
    
)

var p = fmt.Println
var args string 
//var args strings 


func main() {
	args := os.Args
	//arg2 := os.Args[2]
	//p(args)
	parserArgs(args)

}
