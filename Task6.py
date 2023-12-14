

# 1. Create 2 lists for even and odd numbers:

list = [10 , 501 , 22, 37, 100 , 999 , 87 , 351]

even_num = []
odd_num = []

for numbers in list:
    if numbers % 2 == 0 :
        even_num.append(numbers)
    else:
        odd_num.append(numbers)

print ("Even numbers:", even_num)
print ("Odd numbers:", odd_num)


# 3. List of happy numbers: 

def find_happy_numbers (num):
    group = set()
    while num !=1 and num not in group :
        group.add(num)
        num = sum(int(place_values)**2 for place_values in str(num))
    return num == 1

list = [10,501,22,37,100,999,87,351]

happy_numbers = [ num for num in list if find_happy_numbers(num)] 

print ( "Happy numbers are: ", happy_numbers)
print ( "Number of happy numbers are: ", len(happy_numbers))



# 4. Sum of first and last digit of an integer: 

def sum_first_last_digit (num):
    num = str(num) # Convert the number into string to take the necessary digits

    first_digit = int(num[0]) # positive indexing
    last_digit = int(num[-1]) # negative indexing

    sum = first_digit + last_digit

    return sum

input_number = input("Please enter a number:")
input_number = int(input_number)

answer = sum_first_last_digit (input_number)

print(f"The sum of first and last digits of the integer {input_number} is: {answer}")



# 6. Find the duplicates in the three lists: 

# Assume the lists are as follows: 

a = [52, 69, 96, 12] 
b = [69, 15, 12, 88] 
c = [15, 69, 79, 12]

duplicates = set (a) & set(b)

if duplicates:
    print("The duplicate items are: ", list(duplicates))

else:
    print ("There are no duplicate items in the list.")


# 8. Find the minimum element:

given_list = [12, 56, 63, 14, 8, 95, 1]

list = sorted(given_list)

min_element = list[0]

print ( " The minimum element in the list is: ", min_element)


















    



