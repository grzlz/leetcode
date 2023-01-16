class Solution:
    def mntnArray(self, array): 
        i = 1
        if(len(array) < 3):
            return False

        while(i < len(array) and array[i] >= array[i-1]):
            i += 1

        if(i == 1 or i == len(array)):
            return False

        while(i < len(array) and array[i] < array[i-1]):
            i += 1
        
        return i == len(array)



a1 = Solution()

ans = a1.mntnArray([1, 2,2, 2,3, 4, 3])

print(ans)