#Question no. 1
number_of_rows = int(input("Enter number of rows:"))
number_series=10
number_series1=number_of_rows * (number_of_rows+1)
for row in range(1,number_of_rows+1):
    print("*" * ((2 * row) -2), end="")
    last_part=[]
    for column in range(number_of_rows,0,-1):
        print(str(number_series), end="")
        last_part.insert(0,str(number_series1))
        number_series+=10
        number_series1-=1
    number_of_rows-=1
    print("0".join(last_part))