package main

import "fmt"

func clumsy(N int) int {
	/*
		因为运算顺序是固定的，所以"*", "/", "+"都可以立即运算，只有"-"不能立即运算，需要结合后面的数字，
		但是被减的内容也是固定的，是N*(N-1)/(N-2)，因此遇到减法直接把-N*(N-1)/(N-2)算出来即可，后续必定是一个"+"（如果有后续的话）
		其他运算立即执行即可
	*/
	ops := []string{"*", "/", "+", "-"}
	num := 0
	opLast := "+"
	for i := 0; N > 0; {
		op := ops[i%4]
		switch opLast {
		case "*":
			num *= N
			i++
			N--
		case "/":
			num /= N
			i++
			N--
		case "+":
			num += N
			i++
			N--
		case "-":
			if N >= 3 {
				num = num - N*(N-1)/(N-2)
				i += 3
				N -= 3
			} else if N >= 2 {
				num = num - N*(N-1)
				i += 2
				N -= 2
			} else {
				num -= N
				i++
				N--
			}
			op = "+"
		}
		opLast = op
	}
	return num
}

func main() {
	inputs := []int{8, 1, 2, 3, 4, 5, 6, 7}
	for _, input := range inputs {
		ret := clumsy(input)
		fmt.Printf(" input = %v\noutput = %v\n\n", input, ret)
	}
}
