
#basic operations


def basic_operation(x, y):
  result = {
      "sum": x + y,
      "sub": x - y,
      "mult": x * y,
      "div": round((x / y), 2)
  }
  return result


print(basic_operation(5, 6))

#power function
def power(base,exponent, **kwargs):
  try:
    result = base ** exponent
    if 'modulo' in kwargs:
        result %= kwargs['modulo']
        return result
  except Exception as e:
    print("error occured= ",e)


#exception handling


def exception_handling(x, y):
  result = None
  try:
    result = round((x / y), 2)
  except ZeroDivisionError:
    print("error occur= division by zero")
  except Exception:
    print("error occur= invalid input")

  return result


print(exception_handling(5, 7))


#higher order function

def apply_operations(func_args_list):
  try:
    result =list(map(lambda x: x[0](*x[1]), func_args_list))
    print (result)
  except Exception as e:
    print("error occured= ",e)
