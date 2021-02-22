class Solution {
    public Map<Character, Character> trans = new HashMap<Character, Character>();
    public Set<Character> used = new HashSet<Character>();
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        int sz = pattern.length();
        List<String> ans = new ArrayList<String>();
        for(String w: words) {
            Boolean ok = true;
            trans.clear();
            used.clear();
            for(int i=0; i<sz && ok; i++) {
                if(!trans.containsKey(pattern.charAt(i))) {
                    ok &= !used.contains(w.charAt(i));
                    trans.put(pattern.charAt(i), w.charAt(i));
                    used.add(w.charAt(i));
                }
                else {
                    ok &= (trans.get(pattern.charAt(i)) == w.charAt(i));
                }
            }
            if(ok)
                ans.add(w);
        }
        return ans;
    }
}
