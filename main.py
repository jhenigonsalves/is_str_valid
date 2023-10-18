def isValid(s: str) -> bool:
    pairs_dict = {"(": ")", "[": "]", "{": "}"}
    list_s = []
    element_count = 0
    for idx, element in enumerate(s):
        if element in pairs_dict.keys():
            list_s.append(element)
            element_count = element_count + 1
        elif element in pairs_dict.values():
            if not list_s:
                list_s.append(element)
                element_count = element_count + 1
            elif element == pairs_dict[list_s[element_count - 1]]:
                element_count = element_count - 1
                list_s.pop()
            else:
                list_s.append(element)
                element_count = element_count + 1
    if list_s:
        return False
    else:
        return True
