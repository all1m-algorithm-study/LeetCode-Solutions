class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        deque<int> dq;
        sort(deck.begin(), deck.end(), greater<>());
        dq.push_front(deck[0]);
        for(int i=1; i<deck.size(); i++) {
            dq.push_front(dq.back());
            dq.pop_back();
            dq.push_front(deck[i]);
        }
        return vector<int>(dq.begin(), dq.end());
    }
};
