def quicksort(arr):
	if len(arr) < 2:
		return arr
	else:
		pivot = arr[-1]
		smaller, equal, larger = [], [], []
		for num in arr:
			if num < pivot:
				smaller.append(num)
			elif num == pivot:
				equal.append(num)
			else:
				larger.append(num)
		return quicksort(smaller) + equal + quicksort(larger)

def merge_sorted(arr1,arr2):
	sorted_arr = []
	i, j = 0, 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			sorted_arr.append(arr1[i])
			i += 1
		else:
			sorted_arr.append(arr2[j])
			j += 1
	while i < len(arr1):
		sorted_arr.append(arr1[i])
		i += 1
	while j < len(arr2):
		sorted_arr.append(arr2[j])
		j += 1
	return sorted_arr

def mergesort(arr):
	if len(arr) < 2:
		return arr[:]
	else:
		middle = len(arr)//2
		l1 = mergesort(arr[:middle])
		l2 = mergesort(arr[middle:])
		return merge_sorted(l1, l2)

def bubblesort(arr):
	swap_happened = True
	while swap_happened:
		swap_happened = False
		for num in range(len(arr)-1):
			if arr[num] > arr[num+1]:
				swap_happened = True
				arr[num], arr[num+1] = arr[num+1], arr[num]

def insertion_sort(arr):
	key = 1
	for num in range(key, len(arr)):
		if arr[key] < arr[key-1]:
			arr[key], arr[key-1] = arr[key-1], arr[key]
			working_index = arr.index(arr[key-1])
			while working_index > 0:
				if arr[working_index] < arr[working_index-1]:
					arr[working_index], arr[working_index-1] = arr[working_index-1], arr[working_index]
				working_index -= 1
		key += 1
	return(arr)