
def type_logger(func):
   print(func)


   def type_variable(*args):
      if args:
         for number in args:
            print(f'number: {number}\ntype: {type(func(number))}\nresult calc_cube: {func(number)}')


   return type_variable


@type_logger
def calc_cube(x):
   return x ** 3


calc_cube(2, 1.2)
