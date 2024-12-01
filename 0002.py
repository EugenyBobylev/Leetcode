from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f'val={self.val}; next -> {self.next}'
    
    @classmethod
    def get_list(cls, src: list[int]):
        # src = src[-1::-1]
        last_node = None
        lst = None
        for item in src:
            node = cls(item, None)
            if lst is None:
                lst = node
            if last_node:
                last_node.next = node
            last_node = node
        return lst


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def get_list(src: list[int]):
        last_node = None
        lst = None
        for item in src:
            node = ListNode(item, None)
            if lst is None:
                lst = node
            if last_node:
                last_node.next = node
            last_node = node
        return lst

    def list2int(lst: Optional[ListNode]) -> int:
        node = lst
        str_of_int = str(node.val)
        while node.next:
            node = node.next
            if node:
                str_of_int = str(node.val) + str_of_int
        return int(str_of_int)
    
    add1 = list2int(l1)
    add2 = list2int(l2)
    res_str = str(add1 + add2)
    res_str = res_str[-1::-1]
    res_int = [int(digit) for digit in res_str]
    print(res_str)
    print(res_int)
    
    res_lst = get_list(res_int)
    print(isinstance(res_lst, ListNode))
    return res_lst


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    ll1 = ListNode.get_list(l1)
    ll2 = ListNode.get_list(l2)
    l3 = addTwoNumbers(ll1, ll2)
    print(l3)

    