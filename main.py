
def hello_world():
  print("Hello World!")



def sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)):
  
      if arr[i] < arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  print(arr)


def factorial(max_number):
    for each in range(max_number):
        print(each)
        factorial(max_number - 1)


factorial(8)
