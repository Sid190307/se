
# while even-odd numbers

i = int(input("Enter the number: "))
n = 5
j = 0

while i > 0 and j < n:
    if i % 2 == 0:
        print(i, "is an even number")
    else:
        print(i, "is an odd number")

    i += 1
    j += 1
 
Input/Output


input	Actual Output
2	2	is a even number
3	is a odd number
4	is a even number
5	is a odd number
6	is a even number











Test cases:
Test case no: 1
Test Case name: Positive Numbers Within Range
 
 


input	Expected Output	Actual Output	Remark
2	2 is a even number	2 is a even number	Success
	3 is a odd number	3 is a odd number	
	4 is a even number	4 is a even number	
	5 is a odd number	5 is a odd number	
	6 is a even number	6 is a even number	

Test case no: 2
Test Case name: Negative Numbers Within Range


input	Expected Output	Actual Output	Remark
-2	-2 is a even number-1 is a odd number0 is a even number1 is a odd number
2 is a even number	No Output	Fail
 
Test case no 3
Test case name: Number out of Range



input	Expected Output	Actual Output	Remark
12345678900003252656	12345678900003252656	12345678900003252656	Success
	is a even number	is a even number	
	12345678900003252657		
	is a odd number	1234567890000325265	
	12345678900003252658		
	is a even number		
	12345678900003252659	7 is a odd number	
	is a odd number		
	12345678900003252660
is a even number	1234567890000325265	
		8 is a even number	
		
1234567890000325265	
		
9 is a odd number	
		
1234567890000325266	
 
		0 is a even number	
2.	 if-else
