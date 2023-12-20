
def longestConsecutive(nums):
        print("hello")
        nums.sort()
        print(nums)
        currentmax = 1
        counter = 1
        i = 0
        while i<len(nums)-1:
            if nums[i]+1==nums[i+1]: 
                print(counter)
                counter+=1
                i+=1 

            elif (nums[i]+1!=nums[i+1]) and (counter > currentmax):
                currentmax = counter
                counter = 1
                i+=1
            else:
                i+=1
           
        print(currentmax)
    

longestConsecutive([100, 102, 101, 404, 403, 405,406,100])
        