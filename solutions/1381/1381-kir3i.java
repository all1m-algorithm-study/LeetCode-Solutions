class CustomStack {
    public int top = 0;
    public int maxSize;
    public int[] data;
    
    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
        data = new int[maxSize];
    }
    
    public void push(int x) {
        if (top == maxSize)
            return;
        data[top++] = x;
    }
    
    public int pop() {
        if (top == 0)
            return -1;
        return data[--top];
    }
    
    public void increment(int k, int val) {
        int sz = k<top? k: top;
        for(int i=0; i<sz; i++)
            data[i] += val;
    }
}
