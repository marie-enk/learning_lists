#uzd1
# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29),
# kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
import random
numbers = []
for i in range(30):
    numbers.append(random.randint(5, 25))
print(numbers)

#uzd2a
count = 0
for number in numbers:
    if number > 10:
        count += 1
print(count," numbers are greater than 10.")

#uzd2b
max = numbers[0]
for i, number in enumerate(numbers):
    if max < numbers[i]:
        max = numbers[i]
print(max, " is the maximum number")

#uzd2c
sum = 0
for number in numbers:
    sum += number
print(sum, " is the sum of the numbers")

#uzd2d
arr=[]
for i, number in enumerate(numbers):
    arr.append(number-i)
print(arr)

#uzd2e
for i in range(30,40):
    arr.append(random.randint(5,25))
print(arr)

#uzd2f
odd = []
even = []
for i, number in enumerate(numbers):
    if i % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

#uzd2g
for i, number in enumerate(numbers):
    if i % 2 == 0 and number > 15:
        #number = 0 #enumerate makes a copy of array so it won't replace the values
        numbers[i] = 0
print(numbers)

#uzd2h
ind = 0
for i, number in enumerate(numbers):
    if number > 10:
        ind = i
        break
print("Smallest index with number > 10: ",ind)

#uzd3
letters = random.choices("ABCD",k=300)
print(letters)
a_count = 0
b_count = 0
c_count = 0
d_count = 0
for letter in letters:
    if letter == "A":
        a_count += 1
    elif letter == "B":
        b_count += 1
    elif letter == "C":
        c_count += 1
    elif letter == "D":
        d_count += 1
print("There are ",a_count,"As, ",b_count, "Bs ",c_count, "Cs ",d_count, "Ds")

#uzd4
sorted_letters = sorted(letters)
print(sorted_letters)

#uzd5
arr1 = random.choices("ABCD",k=300)
arr2 = random.choices("ABCD",k=300)
arr3 = random.choices("ABCD",k=300)
combos = []
for i in range(200):
    combos.append(arr1[i]+arr2[i]+arr3[i])
print(combos)
print(len(set(combos)),"unique combinations")

#uzd6
list1 = []
list2 = []
for i in range(100):
    element1 = random.randint(0,100)
    if element1 not in list1:
        list1.append(element1)
    element2 = random.randint(0,100)
    if element2 not in list2:
        list2.append(element2)
print(list1)
print(list2)

#uzd7
list3 = []
for i in range(len(list1)):
    if list1[i] not in list2:
        list3.append(list1[i])
    else:
        continue
print(list3)

#uzd8
list4 = []
for i in range(len(list1)):
    if list1[i] in list2:
        list4.append(list1[i])
    else:
        continue
print(list4)

#uzd9
elements = [0]*10
for i,element in enumerate(elements):
    if i == 0 or i == 1:
        elements[i] = random.randint(5,25)
    else:
        elements[i] = elements[i-1]+elements[i-2]
print(elements)

#uzd10
dalmatins = []
for i in range(7):
    rnd_value = random.randint(0,300)
    if rnd_value not in dalmatins:
        dalmatins.append(rnd_value)
    else:
        continue
print("Dalmatins from the start:\n",dalmatins)
sorted_dalmatins = sorted(dalmatins, reverse=True)
# for d in dalmatins:
#     for i in range(len(dalmatins)-1):
#         if dalmatins[i] < dalmatins[i + 1]:
#             temp = dalmatins[i + 1]
#             dalmatins[i + 1] = dalmatins[i]
#             dalmatins[i] = temp
print("Sorted:\n",sorted_dalmatins)
replaced_dalmatins = [0]*len(dalmatins)

for i in range(1,int((len(dalmatins)-1)/2+1)):
    current_pos_left = int((len(dalmatins)-1)/2)-i
    current_pos_right = int((len(dalmatins)-1)/2)+i
    replaced_dalmatins[current_pos_left] = sorted_dalmatins[2*i-1]
    replaced_dalmatins[current_pos_right] = sorted_dalmatins[2*i]

replaced_dalmatins[int((len(dalmatins)-1)/2)] = sorted_dalmatins[0]
print(replaced_dalmatins)