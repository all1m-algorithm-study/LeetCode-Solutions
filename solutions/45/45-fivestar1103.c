int jump(int* nums, int numsSize){
    int i, j;
    int* DP = malloc(sizeof(int)*numsSize);
    DP[0] = 0;
    for(i=1;i<numsSize;i++) DP[i] = 30001;
    for(i=0;i<numsSize-1;i++) for(j=1;j<=nums[i];j++){
        if(i+j<numsSize && DP[i+j]>DP[i]+1) DP[i+j] = DP[i]+1;
    }
    return DP[numsSize-1];
}