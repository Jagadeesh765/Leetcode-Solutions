class Solution:
    def alternateDigitSum(self, n: int) -> int:
        x=str(n)
        ans=0
        for i in range(len(x)):
            if i % 2==0:
                ans+=int(x[i])
            else:
                ans-=int(x[i])
        return ans        