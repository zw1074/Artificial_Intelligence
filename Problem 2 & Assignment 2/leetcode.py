# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for a in xrange(len(nums)-1):
#         	for b in xrange(a,len(nums)):
#         		if nums[a] + nums[b] == target:
#         			return [a,b]

def hi(nums,target):
	dirc = {}
	for i in xrange(len(nums)):
		dirc[nums[i]] = i+1
	for i in dirc.keys():
		search = target - i
		if dirc.has_key(search):
			a = [dirc[i],dirc[search]]
			a.sort()
			return a
print hi([3,2,4],6)