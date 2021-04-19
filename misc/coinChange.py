class Solution(object):

    def tryCoinChange(self, coins, amount, changes):
        cur = coins[0]

        d = amount // cur
        r = amount % cur

        if d >0:
            if r == 0:
                return True, d
            else:
                return True, 0
        else:
            return True, 1





    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        sortedCoins = sorted(coins, reverse=True, key=lambda x: x)
        print(sortedCoins)
        changes = {c: 0 for c in coins}

        print(1, end=' ')

        total = amount
        l = len(sortedCoins)
        idx = 0
        while 0 <= idx < l:
            cur = sortedCoins[idx]

            d = total // cur
            r = total % cur

            if d > 0:
                changes[cur] = d
                total = r

                # done
                if r == 0:
                    return sum(changes.values())

                idx += 1

            elif d == 0:
                if idx < (l - 1):
                    idx += 1
                else:
                    while idx > 0:
                        idx -= 1
                        coin = sortedCoins[idx]
                        count = changes[idx]
                        if count > 0 :
                            total += coin
                            changes[coin] = changes[coin] -1
                            break;

        # failed it should not be here
        return 0


if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(solution.coinChange(coins, amount))
