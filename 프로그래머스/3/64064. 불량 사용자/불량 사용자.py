def solution(user_id, banned_id):
    def is_match(user, banned):
        if len(user) != len(banned):
            return False
        for u, b in zip(user, banned):
            if b != '*' and u != b:
                return False
        return True

    idList = []
    for ban in banned_id:
        tempList = []
        for user in user_id:
            if len(ban) == len(user) and is_match(user, ban):
                tempList.append(user)
        idList.append(tempList)

    def backtrack(index, current_combination):
        if index == len(banned_id):
            result.add(tuple(sorted(current_combination)))
            return
        for user in idList[index]:
            if user not in current_combination:
                current_combination.append(user)
                backtrack(index + 1, current_combination)
                current_combination.pop()

    result = set()
    backtrack(0, [])

    return len(result)


