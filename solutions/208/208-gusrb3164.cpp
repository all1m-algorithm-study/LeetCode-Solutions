struct TrieNode
{
    bool word = false;
    unordered_map<char, TrieNode *> children;
};
class Trie
{
public:
    TrieNode *root;
    /** Initialize your data structure here. */
    Trie()
    {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    void insert(string word)
    {
        TrieNode *node = root;
        for (auto ch : word)
        {
            if (node->children.find(ch) != node->children.end())
            {
                node = node->children[ch];
            }
            else
                node = node->children[ch] = new TrieNode();
        }
        node->word = true;
    }

    /** Returns if the word is in the trie. */
    bool search(string word)
    {
        TrieNode *node = root;
        for (auto ch : word)
        {
            if (node->children.find(ch) == node->children.end())
            {
                return false;
            }
            node = node->children[ch];
        }
        return node->word;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix)
    {
        TrieNode *node = root;
        for (auto ch : prefix)
        {
            if (node->children.find(ch) == node->children.end())
            {
                return false;
            }
            node = node->children[ch];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */