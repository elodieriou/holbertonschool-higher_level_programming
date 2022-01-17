def safe_print_division(a, b):
    result = 0
    try:
        if b != 0:
            result = a / b
            return result
        else:
            result = None
    except ValueError:
        pass
    finally:
        print("Inside result: {}".format(result))
