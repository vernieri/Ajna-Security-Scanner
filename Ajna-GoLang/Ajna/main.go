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

func parserArgs(args []string) string{
	var d string
	p(args)
	pArgs := strings.Join(args, "\n")
	//p(pArgs)
	s := strings.Split(pArgs, "\n")
	p(s[1])
	
	//s := strings.Split(pArgs, "./Ajna")
	//p(s)
	//x := strings.Join(s, " ")
	//p(x)
	//first := strings.Split(x, "-")
	//p(first)
	

	return d
}
