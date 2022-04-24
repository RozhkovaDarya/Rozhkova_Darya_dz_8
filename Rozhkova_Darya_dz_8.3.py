# def type_logger(x):
#   return type
  
# @type_logger
# def calc_cube(x):
#   return x ** 3

# a = calc_cube(5.5)
# print('5.5:', a)


def type_logger(func):
  def wrapper(arg):
    print("Run function: " + str(func.__name__) + "(), with param: " + str(arg))
    func(arg)
    print(type(arg))
     
  return wrapper

@type_logger
def calc_cube(num):
  print(num ** 3)

calc_cube(5.5)