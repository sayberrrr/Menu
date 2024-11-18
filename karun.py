data = []

def display():
    if len(data) == 0:
        print("no data to display.")
    else:
        for i, item in enumerate(data):
            print(f"{i+1}.{item}")

def add():
    new_data = input("enter data:")
    data.append(new_data)
    print("data added successfully")

def multiple():
    num = int(input("enter number of entries:"))
    for i in range(num):
        new_data = input(f"enter new data{i+1}:")
        data.append(new_data)
        print("data added successfully.")

def delete():
    data.clear()
    print("data deleted successfully.")

def update():
    if len(data) == 0:
        print("no data to update.")
        return
    display()
    index = int(input("Enter index to update:"))-1
    if index == 0:
        print("invalid index.")
    else:
        new_data = input("Enter new data to update:")
        data[index] = new_data
        print("Data updated successfully")

def reverse():
    data.reverse()
    print("Data reverse successfully.")

while True:
    print("\n        menu")
    print("press [1] to Add data")
    print("press [2] to Add multiple data")
    print("press [3] to Display data")
    print("press [4] to Delete data")
    print("press [5] to Update data")
    print("press [6] to Reverse data")

    choose = input("Enter your choice:")
    if choose == "1":
        add()
    elif choose == "2":
        multiple()
    elif choose == "3":
        display()
    elif choose == "4":
        delete()
    elif choose == "5":
        update()
    elif choose == "6":
        reverse()
    else:
        print("Laga Laga HAHAHAHA")

