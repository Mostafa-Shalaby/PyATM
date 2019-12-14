from tests import test_func
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

# listOfBills, listOfBills -> dictOfBills
# Counts each bill in the tuple and represents it in a dictOfBills form

def ToDictOfBills(lob, bills):
	billDict = {bill: lob.count(bill) for bill in bills}
	return billDict

test_func(1, "ToDictOfBills", ToDictOfBills(GetMinBills([20, 50, 100, 200],930), [20, 50, 100, 200]), {20: 4, 50: 1, 100: 0, 200: 4})
test_func(2, "ToDictOfBills", ToDictOfBills((20, 20, 20, 50, 100, 200, 100), [20, 50, 100, 200]), {20: 3, 50: 1, 100: 2, 200: 1})


# dictOfBills -> INTEGER
# Returns the total count of bills of a given dict of Bills

def CountTotalPapers(dob):
	return sum([billCount for billCount in dob.values()])

test_func(1, "CountTotalPapers", CountTotalPapers({20: 12, 50: 3, 100: 20, 200: 5}), 40)


# dictOfBills -> int
# Calculates the money value of the given dob

def CalculateMoneyValue(dob):
	return sum([bill * billCount for bill, billCount in dob.items()])


# dictOfBills -> perfectAmount
# Calculates the billLimits and perfectAmount of a given dictOfBills
# TODO: If the minBillValue is zero ignore it and take the next minBillValue
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


test_func(1, "BalancingRequirements", BalancingRequirements(billDict1), ({20: 6, 50: 3, 100: 2, 200: 3}, 1070))
test_func(2, "BalancingRequirements", BalancingRequirements(billDict2), ({20: 0, 50: 6, 100: 1, 200: 3}, 1000))


# dictOfBills, dictOfBills(OPTIONAL), int(OPTIONAL) -> boolean
# Validates if the total bill paper count of the first dob is <=
# the given int and if each bill paper count is <= its counter part in
# any given dictOfBills in the args

def ValidateCriteria(dob, *args, maxBillCount=None):
	if maxBillCount:
		if CountTotalPapers(dob) > maxBillCount:
			return False
	for dobLimits in args:
		for bill in dob:
			if dob[bill] > dobLimits[bill]:
				return False
	return True

test_func(1, "ValidateCriteria", ValidateCriteria({20: 12, 50: 3, 100: 20, 200: 5}), True)
test_func(2, "ValidateCriteria", ValidateCriteria({20: 12, 50: 3, 100: 20, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}), False)
test_func(3, "ValidateCriteria", ValidateCriteria({20: 12, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 20, 50: 5, 100: 5, 200: 5}), True)
test_func(4, "ValidateCriteria", ValidateCriteria({20: 32, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, maxBillCount=40), False)
test_func(5, "ValidateCriteria", ValidateCriteria({20: 12, 50: 3, 100: 2, 200: 5}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 9}, maxBillCount=40), False)
test_func(6, "ValidateCriteria", ValidateCriteria({20: 0, 50: 4, 100: 1, 200: 3}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 3}, maxBillCount=40), True)


# amount, dictOfBills -> amount, dictOfBills
# Makes(distributes) the given amount using the papers in the given dictOfBills
# and returns a dob representing the number of bills used to make the amount and
# the remaining undistributed amount

def DistributeAmount(amount, expendableBills, expendedBills=None):
	# Initiate the expended bills
	if not expendedBills:
		expendedBills = {bill: 0 for bill in expendableBills}

	# If no remaining expendable bills, return
	if expendableBills == dict():
		return (amount, expendedBills)

	# If the amount is fully distributed, return
	elif amount == 0:
		return (0, expendedBills)

	# We're still distributing
	else:
		# Get the minimum number of papers to make the amount using the expendable bills
		minPapers = ToDictOfBills(GetMinBills([bill for bill in expendableBills], amount), [bill for bill in expendableBills])

		# If the paper count is zero try to reduce the amount so that it becomes dividable by the minimum bill
		if CountTotalPapers(minPapers) == 0:
			minBill = min(expendableBills)
			minPapers = ToDictOfBills(GetMinBills([bill for bill in expendableBills], amount - amount % minBill), [bill for bill in expendableBills])

			# If the zero paper count insists then the amount is not representable using the given expendableBills
			if CountTotalPapers(minPapers) == 0:
				return amount, expendedBills

		# Get the appropriate paper count of the max bill
		maxBill = max(expendableBills)
		expendedBills[maxBill] += min(expendableBills[maxBill], minPapers[maxBill])

		# Reduce the paper count of the max bill in the expendableBills and deduct from amount
		expendableBills[maxBill] -= expendedBills[maxBill]
		amount -= expendedBills[maxBill] * maxBill
		if expendableBills[maxBill] == 0:
			del expendableBills[maxBill]

		return DistributeAmount(amount, expendableBills, expendedBills)

test_func(1, "DistributeAmount", DistributeAmount(200, {100: 2, 50: 4, 20: 10}), (0, {100: 2, 50: 0, 20: 0}))
test_func(2, "DistributeAmount", DistributeAmount(200, {50: 4, 20: 10}), (0, {50: 4, 20: 0}))
test_func(3, "DistributeAmount", DistributeAmount(200, {100: 1, 50: 4, 20: 10}), (0, {100: 1, 50: 2, 20: 0}))
test_func(4, "DistributeAmount", DistributeAmount(200, {100: 0, 50: 0, 20: 10}), (0, {100: 0, 50: 0, 20: 10}))
test_func(5, "DistributeAmount", DistributeAmount(100, {50: 1, 20: 2}), (10, {50: 1, 20: 2}))
test_func(6, "DistributeAmount", DistributeAmount(200, {50: 1, 20: 6}), (30, {50: 1, 20: 6}))


# dictOfBills, amount -> dictOfBills
# Returns the limits to balance the result of the given amount using the bills
# in the given dictOfBills

def BalancedLimits(dob, amount):
	maxBill = max(dob)
	minBalancingAmount = maxBill * len(dob)
	perfectAmount = ceil(amount/minBalancingAmount) * minBalancingAmount
	billLimits = {bill:min(ceil(perfectAmount/len(dob)/bill), dob[bill]) for bill in dob}
	return billLimits

test_func(1, "BalancedLimits", BalancedLimits({20: 60, 50: 24, 100: 12, 200: 6}, 1300), {20: 20, 50: 8, 100: 4, 200: 2})
test_func(2, "BalancedLimits", BalancedLimits({20: 60, 50: 24, 100: 12, 200: 6}, 800), {20: 10, 50: 4, 100: 2, 200: 1})
test_func(3, "BalancedLimits", BalancedLimits({20: 8, 50: 5, 100: 2, 200: 1}, 300), {20: 8, 50: 4, 100: 2, 200: 1})
test_func(4, "BalancedLimits", BalancedLimits({20: 8, 50: 5, 100: 2, 200: 1}, 1300), {20: 8, 50: 5, 100: 2, 200: 1})


# dictOfBills, dictOfBills -> boolean
# Adjusts the first dob to make each bill have papers less than or
# equal to its counterpart in the second dob

def AdjustPapers(dob1, dob2):
	for bill in dob1:
		# If the paper count of a bill exceeds the limit
		if dob1[bill] > dob2[bill]:
			# Get how many papers exceed the limit
			delta = dob1[bill] - dob2[bill]

			# # Get the papers of lower value that could be expended in the distribution
			expendableBills = dict()
			for expendableBill in dob1:
				if expendableBill >= bill:
					continue
				expendableBills[expendableBill] = dob2[expendableBill] - dob1[expendableBill]

			# Distribute the bill over the expendadble bills
			remainder, expendedBills = DistributeAmount(delta*bill, expendableBills)
			if remainder != 0:
				return False
			else:
				dob1[bill] -= delta
				for expendedBill in expendedBills:
					dob1[expendedBill] += expendedBills[expendedBill]
	return True

test_func(1, "AdjustPapers", AdjustPapers({20: 3, 50: 3, 100: 2, 200: 0}, {20: 3, 50: 7, 100: 1, 200: 0}), True)
test_func(2, "AdjustPapers", AdjustPapers({20: 3, 50: 3, 100: 2, 200: 0}, {20: 3, 50: 3, 100: 1, 200: 0}), False)
test_func(3, "AdjustPapers", AdjustPapers({20: 4, 50: 3, 100: 2, 200: 0}, {20: 3, 50: 3, 100: 2, 200: 0}), False)
test_func(4, "AdjustPapers", AdjustPapers({20: 4, 50: 4, 100: 2, 200: 0}, {20: 100, 50: 3, 100: 1, 200: 0}), False)


# dictOfBills, dictOfBills -> None
# Balances the second dict so that all the bill values are equal but is
# bound to the given limits in the dictOfBills and max bill count

def BalancePapers(dob, avbills, billLimits, maxBillCount=maximumBillCount, dynamic=False):
	maxBill = max(avbills)

	while(dob[maxBill] > min(billLimits[maxBill], avbills[maxBill])):
		# The max bill is to be distributed over the rest of the bills
		distributableAmount = maxBill

		# Make a dict of the expendable bills and their count (delta)
		expendableBills = {bill: (billLimit - billCount) if billLimit > billCount else 0 for (bill, billCount), billLimit in zip(dob.items(), billLimits.values())}

		# Check if the distributableAmount could be distributed over the rest of the bills
		distributableAmount, expendedBills = DistributeAmount(distributableAmount, expendableBills)

		# If not fully distributed, break out of the while loop if balancing is not dynamic
		# but if it is dynamic adjust the limits and try to redistribute the distributableAmount
		if distributableAmount != 0:
			if dynamic:
				dynamic = False

				# Apply changes
				# Add the expendedBills to the dob
				for bill in dob:
					dob[bill] += expendedBills[bill]

				# Validate that the new dob paper count doesn't exceed maximumBillCount
				if not ValidateCriteria(dob, maxBillCount=maximumBillCount):
					# undo the changes
					# Subtract the expendedBills from the dob
					for bill in dob:
						dob[bill] -= expendedBills[bill]
					break

				# Adjust the billLimits
				newBillLimits = BalancedLimits(avbills, CalculateMoneyValue(dob) + distributableAmount - CalculateMoneyValue(billLimits))
				billLimits = {bill: billLimit + newBillLimit for (bill, billLimit), newBillLimit in zip(billLimits.items(), newBillLimits.values())}

				# Make a dict of the expendable bills and their count (delta)
				expendableBills = {bill: min((billLimit - billCount), avbills[bill]) if billLimit > billCount else 0 for (bill, billCount), billLimit in zip(dob.items(), billLimits.values())}

				# Try to redistribute the distributableAmount
				distributableAmount, expendedBills = DistributeAmount(distributableAmount, expendableBills)
				if distributableAmount != 0:
					break
			else:
				break

		## Apply changes
		# Reduce 1 paper from maxBill
		dob[maxBill] -= 1

		# Add the expendedBills to the dob
		for bill in dob:
			dob[bill] += expendedBills[bill]

		# Validate that the new dob paper count doesn't exceed maximumBillCount
		if not ValidateCriteria(dob, maxBillCount=maximumBillCount):
			# undo the changes
			# Add 1 paper to maxBill
			dob[maxBill] += 1

			# Subtract the expendedBills from the dob
			for bill in dob:
				dob[bill] -= expendedBills[bill]
			break

	print(dob)
	return True if dob[maxBill] <= avbills[maxBill] else False

test_func(1, "BalancePapers", BalancePapers({20: 4, 50: 1, 100: 0, 200: 4}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 0, 50: 6, 100: 1, 200: 3}), {20: 4, 50: 3, 100: 1, 200: 3})
test_func(2, "BalancePapers", BalancePapers({20: 0, 50: 0, 100: 0, 200: 1}, {20: 60, 50: 30, 100: 13, 200: 9}, {20: 9, 50: 1, 100: 0, 200: 0}), {20: 0, 50: 0, 100: 0, 200: 1})
test_func(3, "BalancePapers", BalancePapers({20: 0, 50: 0, 100: 0, 200: 40}, {20: 800, 50: 320, 100: 160, 200: 80}, {20: 100, 50: 40, 100: 20, 200: 10}), {20: 0, 50: 0, 100: 0, 200: 40})
#test_func(4, "BalancePapers", BalancePapers({20: 0, 50: 0, 100: 0, 200: 7}, {20: 392, 50: 163, 100: 77, 200: 40}, {20: 12, 50: 11, 100: 1, 200: 2}), {20: 10, 50: 10, 100: 1, 200: 3})


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

	# Get the min bills solution
	resultDob = ToDictOfBills(GetMinBills([bill for bill in avbills], amount), [bill for bill in avbills])

	# Validate that the total paper count of the min solution is <= maxBillCount
	if not ValidateCriteria(resultDob, maxBillCount=maxBillCount):
		return avbills, False

	# Validate that the required papers of each bill is available in the ATM
	maxBill = max(avbills)
	paperCountValidator = avbills.copy()
	paperCountValidator[maxBill] = float("inf")
	if not ValidateCriteria(resultDob, paperCountValidator):
		if not AdjustPapers(resultDob, paperCountValidator):
			return avbills, False
	del paperCountValidator

	# Check if the avbills are balanced #

	# Get the amount to balance the sum of values of available bills
	billLimits, perfectAmount = BalancingRequirements(avbills)

	# If balanced,just balance the output papers
	if perfectAmount == 0:
		billLimits = BalancedLimits(avbills, amount)
		wasBalanced = BalancePapers(resultDob, avbills, billLimits)
		if not wasBalanced:
			return avbills, False

	# Else if not balanced, use the dynamic balancing for the output papers
	else:
		billLimits = {bill: min(avbillCount, billLimit) for (bill, avbillCount), billLimit in zip(avbills.items(), billLimits.values())}
		wasBalanced = BalancePapers(resultDob, avbills, billLimits, dynamic=True)
		if not wasBalanced:
			return avbills, False

	# Deduct the the results from the avbills
	for bill in avbills:
		avbills[bill] -= resultDob[bill]

	return avbills, resultDob

test_func(1, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 1300), ({20: 60, 50: 24, 100: 11, 200: 5}, {20: 0, 50: 6, 100: 2, 200: 4}))
test_func(2, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 1000), ({20: 60, 50: 24, 100: 12, 200: 6}, {20: 0, 50: 6, 100: 1, 200: 3}))
test_func(3, 'GetBills', GetBills({20: 60, 50: 30, 100: 13, 200: 9}, 930), ({20: 56, 50: 27, 100: 12, 200: 6}, {20: 4, 50: 3, 100: 1, 200: 3}))
test_func(4, 'GetBills', GetBills({20: 60, 50: 24, 100: 12, 200: 6}, 1200), ({20: 60, 50: 16, 100: 8, 200: 4}, {20: 0, 50: 8, 100: 4, 200: 2}))
test_func(5, 'GetBills', GetBills({20: 489, 50: 191, 100: 100, 200: 42}, 5000), ({20: 489, 50: 183, 100: 84, 200: 27}, {20: 0, 50: 8, 100: 16, 200: 15}))
test_func(6, 'GetBills', GetBills({20: 24, 50: 8, 100: 3, 200: 0}, 1080), ({20: 5, 50: 0, 100: 0, 200: 0}, {20: 19, 50: 8, 100: 3, 200: 0}))

print(GetBills({20: 60, 50: 30, 100: 9, 200: 10}, 130))
