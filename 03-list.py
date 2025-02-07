list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

print(list1); 
print(list2); 
print(list3); 
print(list4); 

# Mengakses elemen
print(list1[0])  # Output: apple

# Mengubah elemen
list1[1] = "orange"
print(list1)  # Output: ['apple', 'orange', 'cherry']

# Menambahkan elemen
list2.append(10)
print(list2)  # Output: [1, 5, 7, 9, 3, 10]

# Menghapus elemen
list2.remove(9)
print(list2)  # Output: [1, 5, 7, 3, 10]

# Menghitung elemen
count_true = list3.count(True)
print(count_true)  # Output: 1

# Mengurutkan list
list2.sort()
print(list2)  # Output: [1, 3, 5, 7, 10]

# Menggabungkan list
combined_list = list1 + list2
print(combined_list)  # Output: ['apple', 'orange', 'cherry', 1, 3, 5, 7, 10]


