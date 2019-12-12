#from #tests import #test_func
from math import ceil

maximumBillCount = 40

def GetMinBills(bills, amount):
	# Method Description
	"""Gives Back the List of Min Bills Needed to Reach A Given Amount"""
	# Number of Columns with equal the amount + 1 making an array from (0 to amount)
	cols = amount + 1
	# Creates an array where the first value is 0, rest is inf: # 0 inf inf inf inf ...
	T = [0 if col == 0 else float("inf") for col in range(cols)]
	# Create an Array Where All Values = -1
	R = [-1 for col in range(cols)]

	# Finds The Minimum Bill Count and Creates R array which u can extract the exact Bills Used.
	for j in range(len(bills)):
		for i in range(1, cols):
			selectBill = bills[j]
			if i >= selectBill:
				if T[i] > 1 + T[i - selectBill]:
					T[i] = 1 + T[i - selectBill]
					R[i] = j
	# Code to extract the different bills used into an array.
	result = []
	value = len(R) - 1
	if R[value] == -1:
		# An empty array means that amount can not be exactly reproduced with the given bills.
		return result
	while value != 0:
		bill = bills[R[value]]
		value = value - bill
		result.append(bill)
	return result

## Data Definations ##
# -----------------------

# bill is INTEGER
# Interp. represents the value of a bill

"""
def	func-for-bill(bill):
	return (... bill)
"""

# billCount is INTEGER
# Interp. represents the paper count of a bill

"""
def	func-for-billCount(billCount):
	return (... billCount)
"""

# amount is INTEGER
# Interp. represents an amount of money to be ejected

"""
def	func-for-amount(amount):
	return (... amount)
"""

# billValue is INTEGER
# Interp. bill * billCount

"""
def	func-for-billValue(billValue):
	return (... billValue)
"""

# perfectAmount is INTEGER
# Interp. represents the amount which will balance the values of
# the available bills if subtracted from the total value of the bills

"""
def	func-for-perfectAmount(perfectAmount):
	return (... perfectAmount)
"""

# dictOfBills is a dictionary
# Interp. represents bills and their count
# form -> {bill: billCount}

billDict1 = {20: 36, 50: 15, 100: 8, 200: 6}
billDict2 = {20: 60, 50: 30, 100: 13, 200: 9}

"""
def func-for-dictOfBills(dob):
	for bill, billCount in avbills.items():
		(... bill billCount)
"""

## Functions ##
# -----------------------

# dictOfBills -> perfectAmount
# Calculates the billLimits and perfectAmount of a given dictOfBills

def BalancingRequirements(dob):
	# Get the minimum bill value and the max bill in the given dictOfBills
	minBillValue = min([bill * billCount for bill, billCount in dob.items()])
	maxBill = max([bill for bill in dob])
	# Adjust the minimum bill value so that it becomes a multiple of maxBill
	minBillValue = minBillValue - minBillValue % maxBill
	# Initiate the bill limits and the perfect amount
	billLimits = {bill: 0 for bill in dob}
	perfectAmount = 0
	# Get the perfect amount and the bill limit values
	for bill in billLimits:
		billLimitValue = int(dob[bill] * bill - minBillValue)
		perfectAmount += billLimitValue
		billLimits[bill] = int((billLimitValue) / bill)
	return billLimits, perfectAmount


#test_func(1, "BalancingRequirements", BalancingRequirements(billDict1), ({20: 6, 50: 3, 100: 2, 200: 3}, 1070))
#test_func(2, "BalancingRequirements", BalancingRequirements(billDict2), ({20: 0, 50: 6, 100: 1, 200: 3}, 1000))

# listOfBills, listOfBills -> dictOfBills
# Counts each bill in the tuple and represents it in a dictOfBills form

def ToDictOfBills(lob, bills):
	billDict = {bill: lob.count(bill) for bill in bills}
	return billDict

#test_func(1, "ToDictOfBills", ToDictOfBills(GetMinBills([20, 50, 100, 200],930), [20, 50, 100, 200]), {20: 4, 50: 1, 100: 0, 200: 4})
#test_func(2, "ToDictOfBills", ToDictOfBills((20, 20, 20, 50, 100, 200, 100), [20, 50, 100, 200]), {20: 3, 50: 1, 100: 2, 200: 1})

# dictOfBills -> INTEGER
# Returns the total count of bills of a given dict of Bills

def CountTotalBills(dob):
	return sum([billCount for billCount in dob.values()])

#test_func(1, "CountTotalBills", CountTotalBills({20: 12, 50: 3, 100: 20, 200: 5}), 40)

# dictOfBills, dictOfBills(OPTIONAL), int(OPTIONAL) -> boolean
# Validates if the total bill paper count of the first dob is <=
# the given int and if each bill paper count is <= its counter part in
# any given dictOfBills in the args

def ValidateCriteria(dob, *args, maxBillCount=None):
	if maxBillCount:
		if CountTotalBills(dob) > maxBillCount:
			return False
	for dobLimits in args:
		for bill in dob:
			if dob[bill] > dobLimits[bill]:
				return False
	return True

#test_func(1, "ValidateCriteria", ValidateCriteria({20: 12, 50: 3, 100: 20, 200: 5}), True)
#test_func(2, "ValidateCriteria", ValidateCriteria({20: 12, 50: 3, 100: 20, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}), False)
#test_func(3, "ValidateCriteria", ValidateCriteria({20: 12, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 20, 50: 5, 100: 5, 200: 5}), True)
#test_func(4, "ValidateCriteria", ValidateCriteria({20: 32, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, maxBillCount=40), False)
#test_func(5, "ValidateCriteria", ValidateCriteria({20: 12, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 9}, maxBillCount=40), False)
#test_func(6, "ValidateCriteria", ValidateCriteria({20: 0, 50: 4, 100: 1, 200: 3}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 3}, maxBillCount=40), True)

# int -> int
# Returns the minimum divisor of n other than 1 and returns n if n is prime

def minimumDivisor(n):
	for m in range(2, n):
		if n % m == 0:
			return m
	return n

#test_func(1, "minimumDivisor", minimumDivisor(20), 2)

# list -> dict
# Checks if each bill could be represented by the lower valued bills or not and
# returns the bills that can't and their harmonizer, which is minimum paper count
# of this bill to be representable by lower valued bills

def getInharmonicCeil(lob):
	lob = lob.copy()
	dob = {}
	lob = sorted(lob, reverse=True)
	for i, b in enumerate(lob):
		for n in lob[i+1: ]:
			if b % n != 0:
				dob[b] = minimumDivisor(n)
	return dob

#test_func(1, "getInharmonicCeil", getInharmonicCeil([20, 50, 100, 200]), {50: 2})

# dictOfBills, dictOfBills -> None
# Balances the second dict so that all the bill values are equal but is
# bound to the given limits in the dictOfBills and max bill count

def BalanceBills(dob, availableBills, billLimits, maxBillCount=maximumBillCount):
	# Get the bill list
	billList = [bill for bill in dob]
	# Get the inharmonic bills (i.e. the bills that can't be assembled by the lower valued bills)
	inharmonicBills = getInharmonicCeil(billList)
	# Sort the billList descendingly
	billList = sorted(billList, reverse = True)
	# Get the max bill
	maxBill = billList[0]

	while(dob[maxBill] > billLimits[maxBill]):
		distributableAmount = maxBill
		expendedBills = {bill: 0 for bill in dob}

		# Make a dict of the expendable bills and their count (delta)
		expendableBills = {bill: (billLimit - billCount) if billLimit > billCount else 0 for (bill, billCount), billLimit in zip(dob.items(), billLimits.values())}
		# Calculate the expendableAmount
		expendableAmount = 0
		for bill, delta in expendableBills.items():
			expendableAmount += bill * delta
			if bill in inharmonicBills:
				if delta % inharmonicBills[bill] != 0:
					expendableAmount -= bill * 1

		# Check if the distributableAmount could be distributed over the rest of the bills
		if expendableAmount >= distributableAmount:
			# Iterate over the bills in the bill list igonring the first element
			# which is the maxBill
			for bill in billList[1:]:
				# If we could expend some papers of the bill,
				if expendableBills[bill] > 0:
					# Get the expended paper count
					expendedBills[bill] += min(expendableBills[bill], distributableAmount//bill)
					# A harmonized number of papers only is allowed for the inharmonic bills
					if bill in inharmonicBills:
						if expendedBills[bill] % inharmonicBills[bill] != 0:
							expendedBills[bill] -= 1
					# Reduce the distributableAmount
					distributableAmount -= bill * expendedBills[bill]
					if distributableAmount == 0:
						break
		else:
			break

		# If no distribution happened, break out of the while loop
		if expendedBills == {bill: 0 for bill in dob}:
			break
		else:
			# Apply changes
			# Reduce 1 paper from maxBill
			dob[maxBill] -= 1
			# Add the expendedBills to the dob
			for bill in dob:
				dob[bill] += expendedBills[bill]
			# Validate that the new dob doesn't exceed the availableBills
			# and their total paper count doesn't exceed maximumBillCount
			if not ValidateCriteria(dob, availableBills, maxBillCount=maximumBillCount):
				# undo the changes
				# Add 1 paper to maxBill
				dob[maxBill] += 1
				# Subtract the expendedBills from the dob
				for bill in dob:
					dob[bill] -= expendedBills[bill]
				breaks

#test_func(1, "BalanceBills", BalanceBills({20: 4, 50: 1, 100: 0, 200: 4}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 3}), {20: 4, 50: 3, 100: 1, 200: 3})
#test_func(2, "BalanceBills", BalanceBills({20: 0, 50: 0, 100: 0, 200: 1}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 9, 50: 1, 100: 0, 200: 0}), {20: 0, 50: 0, 100: 0, 200: 1})
#test_func(3, "BalanceBills", BalanceBills({20: 0, 50: 0, 100: 0, 200: 40}, {20: 800, 50: 320, 100: 160, 200: 80}, {20: 100, 50: 40, 100: 20, 200: 10}), {20: 0, 50: 0, 100: 0, 200: 40})
#test_func(4, "BalanceBills", BalanceBills({20: 0, 50: 0, 100: 0, 200: 7}, {20: 392, 50: 163, 100: 77, 200: 40}, {20: 12, 50: 11, 100: 1, 200: 2}), {20: 10, 50: 10, 100: 1, 200: 3})

# dictOfBills, amount -> dictOfBills, dictOfBills
# Consumes a dictOfBills, which represents the available bills in the
# machine and an amount of money to be ejected from the machine and
# returns a dictOfBills representing the bills to make the amount
# and another dictOfBills representing the available bills after ejection
# and if it is not possible to get the bills, return false instead of
# the dictOfBills to make the amount

def GetBills(avbills, amount, maxBillCount=maximumBillCount):
	# Check if the amount is <= the total amount in the machine
	totalAmount = sum([bill * billCount for bill, billCount in avbills.items()])
	if amount > totalAmount:
		return avbills, False

	# Get the amount to balance the sum of values of available bills
	billLimits, perfectAmount = BalancingRequirements(avbills)

	# If not balanced

	# if amount > perfectAmount and perfectAmount > 0:
	# 	amount = amount - perfectAmount
	# 	# Make a dictOfBills that holds the balancing result dict
	# 	balancingResultDict = {bill: billCount for bill, billCount in billLimits}
	# 	# Deduct the the results from the avbills
	# 	for bill in avbills:
	# 		avbills[bill] -= billLimits[bill]
	# 	ValidateCriteria(billLimits, maxBillCount=maximumBillCount)
	# 	avbills, resultDict = GetBills(avbills, amount)
	# 	for bill in resultDict:
	# 		resultDict[bill] += billLimits[bill]
	# 	return avbills, resultDict

	# If balanced
	if perfectAmount == 0:
		maxBill = max(avbills)
		minBalancingAmount = maxBill * len(avbills)
		perfectAmount = ceil(amount/minBalancingAmount) * minBalancingAmount
		billLimits = {bill:ceil(perfectAmount/len(avbills)/bill) for bill in avbills}

	resultDict = ToDictOfBills(GetMinBills([bill for bill in avbills], amount), [bill for bill in avbills])

	if CountTotalBills(resultDict) == 0 or not ValidateCriteria(resultDict, avbills, maxBillCount=maxBillCount):
		return avbills, False

	BalanceBills(resultDict, avbills, billLimits)

	# Deduct the the results from the avbills
	for bill in avbills:
		avbills[bill] -= resultDict[bill]

	return avbills, resultDict

#test_func(1, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 1300), ({20: 60, 50: 24, 100: 11, 200: 5}, {20: 0, 50: 6, 100: 2, 200: 4}))
#test_func(2, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 1000), ({20: 60, 50: 24, 100: 12, 200: 6}, {20: 0, 50: 6, 100: 1, 200: 3}))
#test_func(3, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 930), ({20: 56, 50: 27, 100: 12, 200: 6}, {20: 4, 50: 3, 100: 1, 200: 3}))

print(GetBills({20: 1250, 50: 500, 100: 250, 200: 124}, 312))
print(GetMinBills([20, 50, 100, 200], 312))
print(ToDictOfBills([], [20, 50, 100, 200]))
