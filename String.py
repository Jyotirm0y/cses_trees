def strStr(haystack, needle):
    nl, hl = len(needle), len(haystack)
    print(nl, hl)
    if nl == 0:
        return nl
    if hl < nl:
        return -1
    for i in range(hl-nl+1):
        print(hl-nl+1)
        print(haystack[i:i+nl])
        print(i,i+nl)
        if haystack[i:i+nl] == needle:
            return i
    return -1


def main():

    haystack = "leecodeleet" 
    needle = "leet"

    dis = strStr(haystack, needle)

    print(dis)
if __name__ == "__main__":
    main()