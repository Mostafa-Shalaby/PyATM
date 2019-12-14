from colorama import Fore

def test_func( test_number,  func_name, test, expected):
    if test == expected:
        print(Fore.GREEN + "({}) {}: Success :)".format(test_number, func_name) + Fore.WHITE)
    else:
        print(Fore.RED + "({}) {}: Fail :(\n\tExpected: {}\n\tActual: {}".format(test_number, func_name, expected, test) + Fore.WHITE)
