package main

// Libraries
import (
    "fmt"
    "os"
    "strings"
)

var p = fmt.Println
var args string 
//var args strings 

// Main
func main() {
	args := os.Args
	//arg2 := os.Args[2]
	//p(args)
	parserArgs(args)

}

//Let's parse arguments to discovery where do we go
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

//for now i'm commiting IP func here, i might change it in the future.
func ip(args string) string{
    var ip string = args
    //s := strings.Split("127.0.0.1:5432", ":")
    //ip, port := s[0], s[1]
    //p("IP:", ip)
    //p("Porta:", port)
    p(ip)
    return args
}
