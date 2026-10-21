
# For loop even-odd numbers

i = int(input("Enter the number: "))

for n in range(5):
    if i > 0:
        if i % 2 == 0:
            print(i, "is an even number")
        else:
            print(i, "is an odd number")
    i += 1


Input/Output


input	Actual Output
2	2	is a even number
3	is a odd number
4	is a even number
5	is a odd number
6	is a even number
Test cases:
Test case No:1
Test Case name : positive Number within range
 
 

input	Expected Output	Actual Output	Remark
2	2 is a even number	2 is an even number	Success
	3 is a odd number	3 is an odd number	
	4 is a even number	4 is an even number	
	5 is a odd number	5 is an odd number	
	6 is a even number	6 is an eve number	
Test case No:2
Test Case name : negative Number within range



input	Expected Output	Actual Output	Remark
-2		No output	Failure
Test case no:3
Test Case Name: Positive numbers within the range

 
input	Expected Output	Actual Output	Remark
123424558896475646	123424558896475646
is a even number	123424558896475646
is a even number	Success
-341165657867897676	-341165657867897676
is a even number	-341165657867897676
is a even number	

