##Codingbat python problem and solutions
#https://codingbat.com/python

List-2 > sum13

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 
is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

Solutions:

'''
def sum13(nums):
  
	tot = 0
	i = 0
	while i < len(nums):
		if nums[i] == 13:
			i += 1
		else:
			tot += nums[i]
		i += 1
	return tot
	'''
''' Or

def sum13(nums):

    total = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 2
            continue
        total += nums[i]
        i += 1

    return total
'''
''' Or

def sum13(nums):
  co=0
  if len(nums)<=0:
    return co
  for a in range(1,len(nums)):
    if nums[a]==13:
      continue
    elif nums[a-1]==13:
      continue
    else:
      co=co+nums[a]      
  if nums[0]!=13:
    co+=nums[0]
  return co
  '''
  
 #Or
def sum13(nums):
  while 13 in nums:
    if nums.index(13) < len(nums)-1:
      nums.pop(nums.index(13)+1)
    nums.pop(nums.index(13))
    
  return sum(nums)
  




List-2 > sum67

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4

Solution:

def sum67(nums):
  sum = 0
  flag = True
  for i in range(0, len(nums),1):
    if nums[i] == 6:
      flag = False
    elif flag == False and nums[i] == 7:
      flag = True
    elif flag == True:
      sum = sum + nums[i]
  return sum 