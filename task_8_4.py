def val_checker(verbosity):

    def get_num(func):

        def validator(*args):
            result = func(*args)
            if verbosity(result):
                return result
            else:
                raise ValueError(f'ValueError: некорректное значение {number}')

        return validator

    return get_num


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


print(f'result: {calc_cube(2)}')
