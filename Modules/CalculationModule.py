#from tests import #test_func
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

# tupleOfBills -> dictOfBills
# Counts each bill in the tuple and represents it in a dictOfBills form

def CountedBills(tob, bills):
	billDict = {bill: tob.count(bill) for bill in bills}
	return billDict

#test_func(1, "CountedBills", CountedBills(GetMinBills([20, 50, 100, 200],930), [20, 50, 100, 200]), {20: 4, 50: 1, 100: 0, 200: 4})
#test_func(2, "CountedBills", CountedBills((20, 20, 20, 50, 100, 200, 100), [20, 50, 100, 200]), {20: 3, 50: 1, 100: 2, 200: 1})

# dictOfBills -> INTEGER
# Returns the total count of bills of a given dict of Bills
# TODO
def CountTotalBills(dob):
	return sum([billCount for billCount in dob.values()])

#test_func(1, "CountTotalBills", CountTotalBills({20: 12, 50: 3, 100: 20, 200: 5}), 40)

# dictOfBills, dictOfBills -> None
# Balances the second dict so that all the bill values are equal but is
# bound to the given limits in the dictOfBills and max bill count

def BalanceBills(billLimits, dob, maxBillCount=maximumBillCount):
	# Get the bill list
	billList = [bill for bill in dob]
	# Sort the billList descendingly
	billList = sorted(billList, reverse = True)
	# Iterate over each bill and try to distribute it over the other bills
	for maxBill in billList:
		# Iterate over the bills less than or equal to max bill to
		# distribute max bill over them
		for bill in billList:
			while(True):
				if bill >= maxBill:
					break
				# Reduce 1 paper from the max bill if possible
				if dob[maxBill] > billLimits[maxBill]:
					dob[maxBill] -= 1
					# Distribute the bill value of that 1 paper over the bill if possible
					newBillCount = int(dob[bill] + (maxBill/bill))
					if newBillCount <= billLimits[bill] and CountTotalBills(dob) + (maxBill/bill) <= maxBillCount:
						dob[bill] = newBillCount
					else:
						dob[maxBill] += 1
						break
				else:
					break
	return dob

#test_func(1, "BalanceBills", BalanceBills({20: 10, 50: 4, 100: 2, 200: 1}, {20: 4, 50: 1, 100: 0, 200: 4}), {20: 4, 50: 1, 100: 2, 200: 3})

# dictOfBills, amount -> dictOfBills, dictOfBills
# Consumes a dictOfBills, which represents the available bills in the
# machine and an amount of money to be ejected from the machine and
# returns a dictOfBills representing the bills to make the amount
# and another dictOfBills representing the available bills after ejection
# and if it is not possible to get the bills, return false instead of
# the dictOfBills to make the amount

def GetBills(avbills, amount):
	# Check if the amount is <= the total amount in the machine
	totalAmount = sum([bill * billCount for bill, billCount in avbills.items()])
	if amount > totalAmount:
		return avbills, False

	# Get the amount to balance the sum of values of available bills
	billLimits, perfectAmount = BalancingRequirements(avbills)

	# If the limit > available bill, replace the limit with the available bill
	for bill in avbills:
		billLimits[bill] = min(billLimits[bill], avbills[bill])

	## Check if the available bills are balanced ##

	# If not balanced
	if amount == perfectAmount:
		for bill in avbills:
			avbills[bill] -= billLimits[bill]
		return avbills, billLimits

	elif amount > perfectAmount and perfectAmount > 0:
		amount = amount - perfectAmount
		# Deduct the the results from the avbills
		for bill in avbills:
			avbills[bill] -= billLimits[bill]
		avbills, resultDict = GetBills(avbills, amount)
		for bill in resultDict:
			resultDict[bill] += billLimits[bill]
		return avbills, resultDict

	# If balanced
	elif perfectAmount == 0:
		maxBill = max(avbills)
		minBalancingAmount = maxBill * len(avbills)
		perfectAmount = ceil(amount/minBalancingAmount) * minBalancingAmount
		billLimits = {bill:ceil(perfectAmount/len(avbills)/bill) for bill in avbills}
		# If the limit > available bill, replace the limit with the available bill
		for bill in avbills:
			billLimits[bill] = min(billLimits[bill], avbills[bill])

	resultDict = CountedBills(GetMinBills([bill for bill in avbills], amount), [bill for bill in avbills])
	BalanceBills(billLimits, resultDict)

	# Deduct the the results from the avbills
	for bill in avbills:
		avbills[bill] -= resultDict[bill]

	return avbills, resultDict

#test_func(1, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 1300), ({20: 60, 50: 24, 100: 11, 200: 5}, {20: 0, 50: 6, 100: 2, 200: 4}))
#test_func(2, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 1000), ({20: 60, 50: 24, 100: 12, 200: 6}, {20: 0, 50: 6, 100: 1, 200: 3}))
#test_func(3, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 930), ({20: 56, 50: 25, 100: 13, 200: 6}, {20: 4, 50: 5, 100: 0, 200: 3}))
