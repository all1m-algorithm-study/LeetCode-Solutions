class Solution:
    f = {}
    def countVowelStrings(self, n):
        return self.nHr(5, n)

    def nHr(self, n, r):
        return self.fact(n+r-1) // self.fact(n-1) // self.fact(r)

    def fact(self, n):
        if n <= 1:
            return 1
        elif n not in self.f:
            self.f[n] = n * self.fact(n-1)
        return self.f[n]
