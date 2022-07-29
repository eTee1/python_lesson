classroom_pupils_1 = int(input("How many pupils in first classroom:\n"))
classroom_pupils_2 = int(input("How many pupils in second classroom:\n"))
classroom_pupils_3 = int(input("How many pupils in third classroom:\n"))
classroom_pupils_1 = classroom_pupils_1 // 2 + classroom_pupils_1 % 2
classroom_pupils_2 = classroom_pupils_2 // 2 + classroom_pupils_2 % 2
classroom_pupils_3 = classroom_pupils_3 // 2 + classroom_pupils_3 % 2
print("Need to buy", classroom_pupils_1 + classroom_pupils_2 + classroom_pupils_3, "desks for 3 classrooms.")
