int factorial(int f) {
	int ret = 1;
	for (int i = 2; i <= f; i++) ret *= i;
	return ret;
}

char* getPermutation(int n, int k) {
	int tmp = 0, idx, i, j;
	char* ret = malloc((n + 1) * sizeof(char));
	int* notUsed = malloc((n + 1) * sizeof(int));
	for (i = 1; i <= n; i++) notUsed[i] = i;
	k--;
	for (i = n - 1; i >= 1; i--) {
		idx = 0;
		for (j = 0; j <= k / factorial(i); j++) {
			idx++;
			while (!notUsed[idx]) idx++;
		}
		tmp = tmp * 10 + idx;
		notUsed[idx] = 0;
		k %= factorial(i);
	}
	for (i = 1; i <= n; i++) if (notUsed[i]) tmp = tmp * 10 + i;
	sprintf(ret, "%d", tmp);
	return ret;
}