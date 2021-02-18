class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        HashMap<Integer, Integer> cnt = new HashMap<Integer, Integer>();
        int[] t = Arrays.copyOf(nums, nums.length);
        Arrays.sort(t);
        for(int i=0; i<t.length; i++)
            if(!cnt.containsKey(t[i]))
                cnt.put(t[i], i);
        
        int[] ans = new int[nums.length];
        for(int i=0; i<nums.length; i++)
            ans[i] = cnt.get(nums[i]);
        return ans;
    }
}
