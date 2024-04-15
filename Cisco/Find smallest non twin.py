def funcTwins(inputArr):
	# Write your code here
	freq = {}

	for num in inputArr:
		freq[num] = freq.get(num,0) + 1
	not_twin = -1
	for num,f in freq.items():
		if f == 1 and (not_twin == -1 or num < not_twin):
			not_twin = num		
		
	return not_twin

print(funcTwins([1,1,5,3,3,4,2]))