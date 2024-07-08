import numpy as np


num = 8

while num > 0:
  print(num)
  num = num - 1
else:
  print("Done!")

roles = ["admin", "user"]

for role in roles:
  if role == "admin":
    print("Hello admin, would you like to see a status report?")
  else:
    print("Hello " + role + ", thank you for logging in again.")

for index, role in enumerate(roles):
  if role == "admin":
    print(f"{index} - Hello admin, would you like to see a status report?")
  else:
    print(f"{index} - Hello " + role + ", thank you for logging in again.")

users = {
  "nowshad": "nowshad@gmail.com",
  "rahat": "rahat@gmail.com",
  "rohan": "rohan@gmail.com"
}

for key in users:
  print(f"Key: {key}, Value: {users[key]}")

print("\n")

for key, val in users.items():
  print(f"Key: {key}, Value: {val}")

print("\n")

np_arr = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])

for num in np.nditer(np_arr):
  print(num)

