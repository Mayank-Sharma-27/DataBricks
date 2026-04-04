# https://www.hack2hire.com/companies/databricks/coding-questions/6854486ad887027976facf61/practice?questionId=6855e42cc201117d348a2630

from typing import List, Optional
import heapq
from collections import defaultdict
class RevenueSystem:
    def __init__(self, ):
        self.customers = -1
        self.customer_revenues = defaultdict(int)
        self.cusomers_heap = []

    def add(self, revenue: int) -> int:
       self.customers += 1
       self.customer_revenues[self.customers] += revenue
       heapq.heappush(self.cusomers_heap, (-self.customer_revenues[self.customers], self.customers))
       return self.customers

    def addByReferral(self, revenue: int, referrerId: int) -> int:
        if referrerId not in self.customer_revenues:
            return -1
        self.customer_revenues[referrerId] += revenue
        heapq.heappush(self.cusomers_heap, (-self.customer_revenues[referrerId], referrerId))
        return self.add(revenue)

    def getTopKCustomer(self, k: int, minRevenue: int) -> List[int]:
        res = []
        temp = []
        while self.cusomers_heap and len(res) < k:
            neg_rev, cid = heapq.heappop(self.cusomers_heap)
            rev = -(neg_rev)
            if cid not in self.customer_revenues:
                continue
            if self.customer_revenues[cid] != -(neg_rev):
                continue
            if rev >= minRevenue:
                res.append(cid)

            temp.append((neg_rev, cid))
        for item in temp:
            heapq.heappush(self.cusomers_heap, item)
        return res
