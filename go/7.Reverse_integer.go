//package main

func reverse(x int) int {
    result := 0
    sign := 1
    if x < 0 {
        sign = -1
        x *= -1
    }
    for x > 0 {
        result = result * 10 + x % 10
        x = x / 10
        if result > 2147483647 {
            return 0
        }
    }
    return result * sign
}

/*func main(){
	x := 123
	y := -123
	z := 1323124315353124

	println(reverse(x))
	println(reverse(y))
	println(reverse(z))
}*/