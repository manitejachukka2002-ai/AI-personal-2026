# # Loops in Python

# # For loop
# for i in range(5,1,-1):
#     print(i, end=" ")

# While loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1
count = 1
while count <= 10:
    if count == 5:
        count = count + 1
        continue
    print(count, end=" ")
    count += 1 
   
   