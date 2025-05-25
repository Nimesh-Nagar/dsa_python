def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Assume the first string is the prefix
    prefix = strs[0]

    for s in strs[1:]:
        i = 0
        # Compare characters until they mismatch or reach the end of either string
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]  # Update prefix to the matched part only

        # Early exit if prefix becomes empty
        if prefix == "":
            return ""

    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog","racecar","car"]))     # Output: ""
print(longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # Output: "inters"
print(longestCommonPrefix(["a"]))  # Output: "a"