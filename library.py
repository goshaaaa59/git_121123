# def сm_to_inches_converter(length):
#     inch = str(round(eval(length + '/ 2.54'), 5))
#
#     return inch

def сm_to_inches_converter(length: float) -> float:
    inch = round(eval(str(length) + '/ 2.54'), 6)

    return inch