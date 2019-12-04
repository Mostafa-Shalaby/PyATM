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

# Testing Functions
print("210 =")
print(GetMinBills([20,50,100,200], 210))