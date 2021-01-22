class Solution:
    def defangIPaddr(self, address):
        return '[.]'.join(address.split('.'))