from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, length):
        self.parent = [i for i in range(length)]

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def join(self, p, q):
        self.parent[self.find(q)] = self.find(p)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind(len(accounts))

        email_to_account_id = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account_id:
                    union_find.join(email_to_account_id[email], i)
                else:
                    email_to_account_id[email] = i


        email_groups = defaultdict(list)
        for email, account_id in email_to_account_id.items():
            email_groups[union_find.find(account_id)].append(email)

        result = []
        for acc_id, emails in email_groups.items():
            name = accounts[acc_id][0]
            result.append([name] + sorted(emails))

        return result


print(Solution().accountsMerge(
    [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
     ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]))
