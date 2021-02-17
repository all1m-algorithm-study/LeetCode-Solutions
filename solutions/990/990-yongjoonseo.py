class Solution:
    def find(self, x, parents):
        if parents[x] == x: return x
        parents[x] = self.find(parents[x], parents)
        return parents[x]
    
    def union(self, x, y, parents, ranks):
        xr, yr = self.find(x, parents), self.find(y, parents)
        if ranks[xr] >= ranks[yr]: parents[yr] = xr
        else: parents[xr] = yr
        if ranks[xr] == ranks[yr]: ranks[xr] += 1
        
    def equationsPossible(self, equations: List[str]) -> bool:
        not_equals = []
        converter = dict()
        conv_idx = 0
        parents = []
        ranks = []
        for i in range(len(equations)):
            a, is_equal, blank, b = equations[i]
            for char in (a, b):
                if char not in converter:
                    converter[char] = conv_idx
                    parents.append(conv_idx)
                    ranks.append(0)                    
                    conv_idx += 1
            is_equal = False if is_equal == '!' else True
            x, y = converter.get(a), converter.get(b)
            if not is_equal:
                not_equals.append((x, y))
                continue
            self.union(x, y, parents, ranks)
        
        for x, y in not_equals:
            if self.find(x, parents) == self.find(y, parents):
                return False
        return True
            
        