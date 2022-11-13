#Question 5
nums = [1,2,3,4,4,5,2,3,4,6,7,8,0,1,2,3,4,-1,4,30] #Get input from user
numDic = {} 
for num in nums:
    count = nums.count(num) #Get the number of occurence of each numbe
    numDic[num] = count
print(numDic)




