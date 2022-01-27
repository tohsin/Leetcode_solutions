from re import T
from collections import Counter


def balancedString( s: str) -> int:
        avg=len(s)//4
        hashmap = Counter(s)
        extras={}
        for key in hashmap:
            if hashmap[key] > avg:
                extras[key] = hashmap[key] - avg
        if not extras:
            return 0
       
        i=j=0
        res = len(s)+1
        count=len(extras)
        while j<len(s):
            if s[j] in extras:
                extras[s[j]] -= 1
                if extras[s[j]] == 0:
                    count -= 1
                
            if count > 0:
                j += 1
                
            elif count == 0:
                while count == 0:
                    res = min(res,(j-i+1))
                    if s[i] in extras:
                        extras[s[i]] += 1
                        if extras[s[i]] == 1:
                            count += 1
                    i += 1
                j += 1
                
        # for left in range(len(s)):
        #     for right in range(left,len(s)):
        #         cache[s[right]]-=1
        #         if is_balaced(cache):
        #             min_len=min(min_len,right-left+1)
        #             cache[s[right]]+=1
        #             break
                    
        # return print(min_len)
        
balancedString("WWEQERQWQWWRWWERQWEQ")