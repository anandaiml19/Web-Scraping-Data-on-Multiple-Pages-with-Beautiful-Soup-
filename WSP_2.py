# try and except error
new_list = [2,4,6,'California']

for element in new_list:
    try:
        print(element/2)
    except:
        print("The element is not a number")

n = 5
while n > 0:
    print(n)
    n = n - 1
    if n == 2:
        break

print("Loop ended")