def number():
  nums=input("please enter a word :")
  reverse=nums[::-1]
  caution=("Oops! sorry your input is not same as the reverse one!")
  if reverse==nums:
    return nums
  return caution
  
  
  
print(number())
