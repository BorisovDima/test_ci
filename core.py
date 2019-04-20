import random

class Core:

    def binary_search(self, m, goal):
        return self._binary_search(m, goal, 0, len(m)-1)

    def _binary_search(self, m, goal, f, l):
        n = (f + l) // 2
        if m[n] == goal:
            return (n, True)
        elif f >= l:
            return (None, False)
        elif m[n] > goal:
            l = n -1
            return self._binary_search(m, goal, f, l)
        else:
            f = n + 1
            return self._binary_search(m, goal, f, l)



if __name__ == '__main__':
    c = Core()
    for i in range(11):
        m = [_ for _ in range(i+1)]
        goal = random.randrange(0, (i+1)*2)
        print(goal)
        print(m)
        print(c.binary_search(m, goal))
        print('-' * 30, ' next ', 30 * '-')

