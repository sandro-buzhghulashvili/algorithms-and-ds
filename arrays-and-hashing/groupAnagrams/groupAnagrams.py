def groupAnagrams(strs):
    res = {}  # Mapping charCount to list of Anagrams

    for s in strs:
        count = [0] * 26  # a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1
            # It is used to map ASCII values into 0 to 25 indexes

        key = tuple(count)

        if key not in res:
            res[key] = []

        res[key].append(s)
    
    return res.values()

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
