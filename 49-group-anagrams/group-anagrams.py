class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #anagrams = sorted characters are same
         groups = defaultdict(list)   #hashmap initialise

         for s in strs:   #break chars , sorting , and joining again
            key = "".join(sorted(s)) 
            groups[key].append(s)

         return list(groups.values())

        