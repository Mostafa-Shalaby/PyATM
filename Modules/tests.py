from colorama import Fore
import CalculationModule

def test_func( test_number,  func_name, test, expected):
    if test == expected:
        print(Fore.GREEN + "({}) {}: Success :)".format(test_number, func_name) + Fore.WHITE)
    else:
        print(Fore.RED + "({}) {}: Fail :(\n\tExpected: {}\n\tActual: {}".format(test_number, func_name, expected, test) + Fore.WHITE)


test_func(1, "ToDictOfBills", CalculationModule.ToDictOfBills(CalculationModule.GetMinBills([20, 50, 100, 200],930), [20, 50, 100, 200]), {20: 4, 50: 1, 100: 0, 200: 4})
test_func(2, "ToDictOfBills", CalculationModule.ToDictOfBills((20, 20, 20, 50, 100, 200, 100), [20, 50, 100, 200]), {20: 3, 50: 1, 100: 2, 200: 1})


test_func(1, "CountTotalPapers", CalculationModule.CountTotalPapers({20: 12, 50: 3, 100: 20, 200: 5}), 40)


test_func(1, "BalancingRequirements", CalculationModule.BalancingRequirements({20: 60, 50: 30, 100: 13, 200: 9}), ({20: 0, 50: 6, 100: 1, 200: 3}, 1000))
test_func(2, "BalancingRequirements", CalculationModule.BalancingRequirements({20: 60, 50: 30, 100: 13, 200: 0}), ({20: 0, 50: 6, 100: 1, 200: 0}, 400))
test_func(3, "BalancingRequirements", CalculationModule.BalancingRequirements({20: 0, 50: 0, 100: 0, 200: 0}), ({20: 0, 50: 0, 100: 0, 200: 0}, 0))


test_func(1, "ValidateCriteria", CalculationModule.ValidateCriteria({20: 12, 50: 3, 100: 20, 200: 5}), True)
test_func(2, "ValidateCriteria", CalculationModule.ValidateCriteria({20: 12, 50: 3, 100: 20, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}), False)
test_func(3, "ValidateCriteria", CalculationModule.ValidateCriteria({20: 12, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 20, 50: 5, 100: 5, 200: 5}), True)
test_func(4, "ValidateCriteria", CalculationModule.ValidateCriteria({20: 32, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, maxBillCount=40), False)
test_func(5, "ValidateCriteria", CalculationModule.ValidateCriteria({20: 12, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 9}, maxBillCount=40), False)
test_func(6, "ValidateCriteria", CalculationModule.ValidateCriteria({20: 0, 50: 4, 100: 1, 200: 3}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 3}, maxBillCount=40), True)


test_func(1, "DistributeAmount", CalculationModule.DistributeAmount(200, {100: 2, 50: 4, 20: 10}), (0, {100: 2, 50: 0, 20: 0}))
test_func(2, "DistributeAmount", CalculationModule.DistributeAmount(200, {50: 4, 20: 10}), (0, {50: 4, 20: 0}))
test_func(3, "DistributeAmount", CalculationModule.DistributeAmount(200, {100: 1, 50: 4, 20: 10}), (0, {100: 1, 50: 2, 20: 0}))
test_func(4, "DistributeAmount", CalculationModule.DistributeAmount(200, {100: 0, 50: 0, 20: 10}), (0, {100: 0, 50: 0, 20: 10}))
test_func(5, "DistributeAmount", CalculationModule.DistributeAmount(100, {50: 1, 20: 2}), (10, {50: 1, 20: 2}))
test_func(6, "DistributeAmount", CalculationModule.DistributeAmount(200, {50: 1, 20: 6}), (30, {50: 1, 20: 6}))


test_func(1, "BalancedLimits", CalculationModule.BalancedLimits({20: 60, 50: 24, 100: 12, 200: 6}, 1300), {20: 20, 50: 8, 100: 4, 200: 2})
test_func(2, "BalancedLimits", CalculationModule.BalancedLimits({20: 60, 50: 24, 100: 12, 200: 6}, 800), {20: 10, 50: 4, 100: 2, 200: 1})
test_func(3, "BalancedLimits", CalculationModule.BalancedLimits({20: 8, 50: 5, 100: 2, 200: 1}, 300), {20: 8, 50: 4, 100: 2, 200: 1})
test_func(4, "BalancedLimits", CalculationModule.BalancedLimits({20: 8, 50: 5, 100: 2, 200: 1}, 1300), {20: 8, 50: 5, 100: 2, 200: 1})


test_func(1, "AdjustPapers", CalculationModule.AdjustPapers({20: 3, 50: 3, 100: 2, 200: 0}, {20: 3, 50: 7, 100: 1, 200: 0}), True)
test_func(2, "AdjustPapers", CalculationModule.AdjustPapers({20: 3, 50: 3, 100: 2, 200: 0}, {20: 3, 50: 3, 100: 1, 200: 0}), False)
test_func(3, "AdjustPapers", CalculationModule.AdjustPapers({20: 4, 50: 3, 100: 2, 200: 0}, {20: 3, 50: 3, 100: 2, 200: 0}), False)
test_func(4, "AdjustPapers", CalculationModule.AdjustPapers({20: 4, 50: 4, 100: 2, 200: 0}, {20: 100, 50: 3, 100: 1, 200: 0}), False)


test_func(1, "BalancePapers", CalculationModule.BalancePapers({20: 4, 50: 1, 100: 0, 200: 4}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 3}), {20: 4, 50: 3, 100: 1, 200: 3})
test_func(2, "BalancePapers", CalculationModule.BalancePapers({20: 0, 50: 0, 100: 0, 200: 1}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 9, 50: 1, 100: 0, 200: 0}), {20: 0, 50: 0, 100: 0, 200: 1})
test_func(3, "BalancePapers", CalculationModule.BalancePapers({20: 0, 50: 0, 100: 0, 200: 40}, {20: 800, 50: 320, 100: 160, 200: 80}, {20: 100, 50: 40, 100: 20, 200: 10}), {20: 0, 50: 0, 100: 0, 200: 40})
#test_func(4, "BalancePapers", CalculationModule.BalancePapers({20: 0, 50: 0, 100: 0, 200: 7}, {20: 392, 50: 163, 100: 77, 200: 40}, {20: 12, 50: 11, 100: 1, 200: 2}), {20: 10, 50: 10, 100: 1, 200: 3})


test_func(1, 'GetBills', CalculationModule.GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 1300), ({20: 60, 50: 24, 100: 11, 200: 5}, {20: 0, 50: 6, 100: 2, 200: 4}))
test_func(2, 'GetBills', CalculationModule.GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 1000), ({20: 60, 50: 24, 100: 12, 200: 6}, {20: 0, 50: 6, 100: 1, 200: 3}))
test_func(3, 'GetBills', CalculationModule.GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 930), ({20: 56, 50: 27, 100: 12, 200: 6}, {20: 4, 50: 3, 100: 1, 200: 3}))
test_func(4, 'GetBills', CalculationModule.GetBills({20: 60, 50: 24, 100: 12, 200: 6}, 1200), ({20: 60, 50: 16, 100: 8, 200: 4}, {20: 0, 50: 8, 100: 4, 200: 2}))
test_func(5, 'GetBills', CalculationModule.GetBills({20: 489, 50: 191, 100: 100, 200: 42}, 5000), ({20: 489, 50: 183, 100: 84, 200: 27}, {20: 0, 50: 8, 100: 16, 200: 15}))
test_func(6, 'GetBills', CalculationModule.GetBills({20: 24, 50: 8, 100: 3, 200: 0}, 1080), ({20: 5, 50: 0, 100: 0, 200: 0}, {20: 19, 50: 8, 100: 3, 200: 0}))
test_func(7, 'GetBills', CalculationModule.GetBills({20: 10, 50: 1, 100: 0, 200: 0}, 200), ({20: 0, 50: 1, 100: 0, 200: 0}, {20: 10, 50: 0, 100: 0, 200: 0}))
