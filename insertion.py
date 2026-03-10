def longest_vowel(nums,k):
    vowel="aeiou"
    leng=0
    
    for i in range(k):
        if nums[i] in vowel:
            leng+=1
    max_len=leng
    for j in range(k,len(nums)):
        if nums[j] in vowel:
            leng+=1
        if nums[j-k] in vowel:
            leng-=1
        max_len=max(max_len,leng)
    return max_len
a="abciiidef"
print(longest_vowel(a,3))