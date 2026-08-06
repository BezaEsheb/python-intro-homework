numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n=== MAIN MENU ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    user_option= input("Choose an option (1-5): ")

    if user_option == "1":
         min_num =[val for val in numbers if all(val <= item for item in numbers)]
         print("Minimum Value:", min_num)
    elif user_option == "2":
         max_num = [val for val in numbers if all(val >= item for item in numbers)]
         print("Maximum Value:", max_num)   
    elif user_option == "3":
         search_num = int(input("Enter a number to search for: "))
         index_matches = [i for i in range(len(numbers)) if numbers[i] == search_num]
         if index_matches:
             print("Found", {search_num}, "at index", index_matches[0])

         else:
             print(f"{search_num} is not in the list.")     

    elif user_option == "4":
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(numbers) - 1):
                    if numbers[i] > numbers[i + 1]:
                        temp = numbers[i]
                        numbers[i] = numbers[i + 1]
                        numbers[i + 1] = temp
                        swapped = True

            print("Sorted List:", numbers)

    elif user_option == "5":
         print("Goodbye!")
         break
    else: 
        print("Invalid option. Please choose a number between 1 and 5.")

