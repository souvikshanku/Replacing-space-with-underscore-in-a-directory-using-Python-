import os

folder = input("Type in the folder location: \n")
path = os.walk(folder, topdown = False)

for root, dirs, files in path:
    for item in dirs:
        if " " in item:
            source = os.path.join(root, item)
            destination = os.path.join(root, item.replace(" ", "_"))
            os.rename(source, destination)
            print(destination + "   ✔")
    for item in files:
        if " " in item:
            source = os.path.join(root, item)
            destination = os.path.join(root, item.replace(" ", "_"))
            os.rename(source, destination)
            print(destination + "   ✔")
print("Successfully Renamed!")