class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double median;
        vector<int> merge;
        int middle = (nums1.size() + nums2.size())/2;
        bool even = false;
        if ((nums1.size() + nums2.size()) % 2 == 0)
            even = true;
        
        for (int i=0;i<=middle;i++){
            if (nums1.size() == 0){
                merge.push_back(nums2[0]);
                nums2.erase(nums2.begin());
            }
            else if (nums2.size() == 0){
                merge.push_back(nums1[0]);
                nums1.erase(nums1.begin());
            }
            else if (nums1[0] > nums2[0]){
                merge.push_back(nums2[0]);
                nums2.erase(nums2.begin());
            } else {
                merge.push_back(nums1[0]);
                nums1.erase(nums1.begin());
            }
        }
        if (even){
            median = (double)(merge[middle-1] +merge[middle])/2;
        }
        else {
            median = merge[middle];
        }
        return median;
    }
};
