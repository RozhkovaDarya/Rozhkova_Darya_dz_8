def val_checker(func):
  def wrapper(arg):
    func(arg)
         
  return wrapper

@val_checker
def calc_cube(x):
  if x > 0:
    print(x ** 3)
  else:
    print('Error')
calc_cube(-5)