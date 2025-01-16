from typing import List


def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    hash_table = {}
    index_sum = float('inf')
    ans = {}
    for i, k in enumerate(list1):
        hash_table[k] = i
    for j, v in enumerate(list2):
        check = hash_table.get(v)
        if check is not None:
            summ = check + j
            if summ <= index_sum:
                index_sum = summ
                ans.setdefault(summ, []).append(v)
    return ans.get(index_sum)

def findRestaurant2(list1: List[str], list2: List[str]) -> List[str]:
    mp = {}
    for i in range(len(list1)):
        mp[list1[i]] = i
    min_sum = float('inf')
    res = []
    for j in range(len(list2)):
        if list2[j] in mp:
            curr_sum = j + mp[list2[j]]
            if curr_sum < min_sum:
                min_sum = curr_sum
                res = [list2[j]]
            elif curr_sum == min_sum:
                res.append(list2[j])
    return res


# print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC"]))
# print(findRestaurant2(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC"]))
# print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
# print(findRestaurant2(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
# print(findRestaurant(["happy","sad","good"], ["sad","happy","good"]))
# print(findRestaurant2(["happy","sad","good"], ["sad","happy","good"]))
# print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC", "happy","sad","good"], ["good","Tapioca Express","Piatti","The Grill at Torrey Pines"]))
print(findRestaurant2(["Shogun","Tapioca Express","Burger King","KFC", "happy","sad","good"], ["good","Tapioca Express","Piatti","The Grill at Torrey Pines"]))

