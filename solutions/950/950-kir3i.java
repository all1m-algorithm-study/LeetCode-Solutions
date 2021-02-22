class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        LinkedList<Integer> dq = new LinkedList<Integer>();
        dq.add(deck[deck.length-1]);
        for(int i=deck.length-2; i>=0; i--) {
            dq.addFirst(dq.pollLast());
            dq.addFirst(deck[i]);
        }
        int[] ans = new int[dq.size()];
        for(int i=0; !dq.isEmpty(); i++)
            ans[i] = dq.poll();
        return ans;
    }
}
