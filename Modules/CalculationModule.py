from math import ceil

maximumBillCount = 40

## Data Definitions ##
# -----------------------

# bill is INTEGER
# Interp. represents the value of a bill

# billCount is INTEGER
# Interp. represents the paper count of a bill

# billValue is INTEGER
# Interp. bill * billCount

# amount is INTEGER
# Interp. represents an amount of money to be ejected

# dictOfBills is a dictionary
# Interp. represents bills and their count
# form -> {bill: billCount}

## Functions ##
# -----------------------

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


# listOfBills, listOfBills -> dictOfBills
# Counts each bill in the tuple and represents it in a dictOfBills form

def ToDictOfBills(lob, bills):
	billDict = {bill: lob.count(bill) for bill in bills}
	return billDict


# dictOfBills -> INTEGER
# Returns the total count of bills of a given dict of Bills

def CountTotalPapers(dob):
	return sum([billCount for billCount in dob.values()])


# dictOfBills -> int
# Calculates the money value of the given dob

def CalculateMoneyValue(dob):
	return sum([bill * billCount for bill, billCount in dob.items()])


# dictOfBills -> perfectAmount
# Calculates the billLimits and perfectAmount of a given dictOfBills

def BalancingRequirements(dob):
	# Get the minimum bill value and the max bill in the given dictOfBills
	minBillValue = min([bill * billCount if billCount != 0 else float("inf") for bill, billCount in dob.items()])
	maxBill = max([bill for bill in dob])

	# Initiate the bill limits and the perfect amount
	billLimits = {bill: 0 for bill in dob}
	perfectAmount = 0

	# Get the perfect amount and the bill limit values
	if minBillValue != float("inf"):
		# Adjust the minimum bill value so that it becomes a multiple of maxBill
		minBillValue = minBillValue - minBillValue % maxBill

		# Calculate the bill limits and the perfect amount
		for bill in billLimits:
			billLimitValue = int(dob[bill] * bill - minBillValue)
			billLimitValue = 0 if billLimitValue <= 0 else billLimitValue
			perfectAmount += billLimitValue
			billLimits[bill] = int((billLimitValue) / bill)
	return billLimits, perfectAmount


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


# dictOfBills, amount -> dictOfBills
# Returns the limits to balance the result of the given amount using the bills
# in the given dictOfBills

def BalancedLimits(dob, amount):
	maxBill = max(dob)
	minBalancingAmount = maxBill * len(dob)
	perfectAmount = ceil(amount/minBalancingAmount) * minBalancingAmount
	billLimits = {bill:min(ceil(perfectAmount/len(dob)/bill), dob[bill]) for bill in dob}
	return billLimits


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
				distributableAmount, newExpendedBills = DistributeAmount(distributableAmount, expendableBills)
				if distributableAmount != 0:
					# undo the changes
					# Subtract the expendedBills from the dob
					for bill in dob:
						dob[bill] -= expendedBills[bill]
					break
				else:
					expendedBills = newExpendedBills
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
	return True if dob[maxBill] <= avbills[maxBill] else False


# dictOfBills, amount -> dictOfBills, dictOfBills
# Consumes a dictOfBills, which represents the available bills in the
# machine and an amount of money to be ejected from the machine and
# returns a dictOfBills representing the bills to make the amount
# and another dictOfBills representing the available bills after ejection
# and if it is not possible to get the bills, return false instead of
# the dictOfBills to make the amount

def GetBills(availablebills, amount, maxBillCount=maximumBillCount):
	avbills = availablebills.copy()
	# Check if the amount is <= the total amount in the machine
	totalAmount = sum([bill * billCount for bill, billCount in avbills.items()])
	if amount > totalAmount:
		return availablebills, False

	# Delete the bills with 0 billCount in avbills
	billList = [bill for bill in avbills]
	for bill in billList:
		if avbills[bill] == 0:
			del avbills[bill]
	del billList

	# Decide the maxBill in the avbills
	maxBill = max(avbills)

	# Get the min bills solution
	resultDob = ToDictOfBills(GetMinBills([bill for bill in avbills], amount), [bill for bill in avbills])

	# If GetMinBills can't solve the amount return
	if CountTotalPapers(resultDob) == 0:
		return availablebills, False

	# Validate that the total paper count of the min solution is <= maxBillCount
	if not ValidateCriteria(resultDob, maxBillCount=maxBillCount):
		return availablebills, False

	# Validate that the required papers of each bill is available in the ATM
	paperCountValidator = avbills.copy()
	paperCountValidator[maxBill] = float("inf")
	if not ValidateCriteria(resultDob, paperCountValidator):
		if not AdjustPapers(resultDob, paperCountValidator):
			return availablebills, False
	del paperCountValidator

	# Check if the avbills are balanced #

	# Get the amount to balance the sum of values of available bills
	billLimits, perfectAmount = BalancingRequirements(avbills)

	# If balanced,just balance the output papers
	if perfectAmount == 0:
		billLimits = BalancedLimits(avbills, amount)
		wasBalanced = BalancePapers(resultDob, avbills, billLimits)
		if not wasBalanced:
			return availablebills, False

	# Else if not balanced, use the dynamic balancing for the output papers
	else:
		billLimits = {bill: min(avbillCount, billLimit) for (bill, avbillCount), billLimit in zip(avbills.items(), billLimits.values())}
		wasBalanced = BalancePapers(resultDob, avbills, billLimits, dynamic=True)
		if not wasBalanced:
			return availablebills, False

	# Deduct the the results from the avbills
	for bill in availablebills:
		try:
			availablebills[bill] -= resultDob[bill]
		except KeyError:
			resultDob[bill] = 0

	return availablebills, resultDob
