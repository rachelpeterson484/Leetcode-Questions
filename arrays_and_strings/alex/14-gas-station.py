class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasMinusCost = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(gasMinusCost) < 0:
            return -1

        start = 0
        gas = 0
        for i, x in enumerate(gasMinusCost):
            gas += x
            if gas < 0:
                gas = 0
                start = i+1

        return start
