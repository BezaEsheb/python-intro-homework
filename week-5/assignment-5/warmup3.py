name =["John", "Luke", "Mark", "Paul", "Peter"]

name_search = input("Enter a name to search for:")
finder = False

for i in range(len(name)):
    if name_search == name[i]:
        print(f"Found {name_search} at index {i}")
        finder = True
        break

if not finder:
    print(f"{name_search} not found in the list.")
    

