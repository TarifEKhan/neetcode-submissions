class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        s=0
        z=[]
        t1=set(t)
        if len(t1)==1:
            return [0]*len(t)
        for i in range(len(t)):
            for j in range(i+1,len(t)):
                if t[j]-t[i]>0:
                    z.append(s+1)
                    break
                if j==len(t)-1:
                    z.append(0)
                else:
                    s+=1
            s=0
        if len(t)-len(z)!=0:
            z.append(0)
        return z


        