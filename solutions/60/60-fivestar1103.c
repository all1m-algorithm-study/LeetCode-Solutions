int factorial(int f) {
	int ret = 1;
	for (int i = 2; i <= f; i++) ret *= i;
	return ret;
}

char * getPermutation(int n, int k){
    int tmp = 0, idx, i, j;
    char* ret = malloc((n + 1) * sizeof(char));
	int* used = calloc(n + 1, sizeof(int)); 
	k--;
	for (i = n - 1; i >= 1; i--) {
		idx = 0;
		for (j = 0; j <= k / factorial(i); j++) {
			idx++;
			while (used[idx]) idx++;
		}
		tmp = tmp * 10 + idx;
		used[idx] = 1;
		k %= factorial(i);
	}
	for (i = 1; i <= n; i++) if (!used[i]) {
        tmp = tmp * 10 + i;
        break;
    }
    sprintf(ret, "%d", tmp);
    return ret;
}