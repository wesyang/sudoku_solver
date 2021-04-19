class Solution(object):
    def printMap(self, map):
        for r in map:
            for c in r:
                print(f'{c} ', end='')
            print()
        print('-----------------')

    def checkAndMarkIsland(self, map, x, y, cc, rc):
        if x < 0 or y < 0: return
        if x >= cc or y >= rc: return

        if map[y][x] == 1:
            map[y][x] = 'x'
            self.markIsland(map, x, y, cc, rc)

    def markIsland(self, map, x, y, cc, rc):
        self.checkAndMarkIsland(map, x - 1, y - 1, cc, rc)
        self.checkAndMarkIsland(map, x - 1, y, cc, rc)
        self.checkAndMarkIsland(map, x - 1, y + 1, cc, rc)

        self.checkAndMarkIsland(map, x, y - 1, cc, rc)
        self.checkAndMarkIsland(map, x, y + 1, cc, rc)

        self.checkAndMarkIsland(map, x + 1, y - 1, cc, rc)
        self.checkAndMarkIsland(map, x + 1, y, cc, rc)
        self.checkAndMarkIsland(map, x + 1, y + 1, cc, rc)

    def findIslands(self, map):
        pass
        if not map: return 0

        rc = len(map)
        cc = len(map[0])
        print(rc, cc)

        total = 0
        for y in range(rc):
            for x in range(cc):
                if map[y][x] == 1:
                    map[y][x] = 'x'
                    self.markIsland(map, x, y, cc, rc)
                    self.printMap(map)
                    total += 1

        return total


if __name__ == "__main__":
    solution = Solution()
    map = [
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
    ]

    solution.printMap(map)
    print(solution.findIslands(map))
