def is_valid_parenthesis_string(s: str) -> bool:
    pairs_dict = {"(": ")", "[": "]", "{": "}"}
    list_s = []
    for element in s:
        print(f"element={element}")
        if element in pairs_dict.keys():
            print(f"{element} is a key")
            list_s.append(element)
        elif element in pairs_dict.values():
            print(f"{element} is not a key")
            try:
                is_closing = element == pairs_dict[list_s[-1]]
                if is_closing:
                    list_s.pop()
                else:
                    list_s.append(element)
            except:
                list_s.append(element)
                print(f"{element} is not in the list")

    if list_s:
        return False
    else:
        return True
