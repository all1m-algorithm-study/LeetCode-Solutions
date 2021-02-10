class CustomStack {
public:
    int size = 0;
    int maxSize;
    vector<int> data;
    CustomStack(int maxSize) {
        this->maxSize = maxSize;
    }
    
    void push(int x) {
        if (size == maxSize)
            return;
        data.push_back(x);
        size++;
    }
    
    int pop() {
        if (size == 0)
            return -1;
        size--;
        int rtn = data.back();
        data.pop_back();
        return rtn;
    }
    
    void increment(int k, int val) {
        if (size <= k)
            for(int i=0; i<size; i++)
                data[i] += val;
        else
            for(int i=0; i<k; i++)
                data[i] += val;
    }
};
