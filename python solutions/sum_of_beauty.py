def beautySum( s):
    ans=0
    for i in range(len(s)):
        cache={}
        for j in range(i,len(s)):
            if s[j] not in cache:
                cache[s[j]]=1
            else:
                cache[s[j]]+=1
            lowest=10000000
            highest=-10000000
            for key in cache:
                lowest=min(lowest,cache[key])
                highest=max(highest,cache[key])
            ans+=highest-lowest
            
            
    return ans
print(beautySum("aabcb"))