#include <iostream>
#include <vector>

using namespace std;

int removeDuplicates(vector<int>& nums) {
	if (nums.size() == 0) {
		return 0;
	}
	if (nums.size() == 1) {
		return 1;
	}

	int cur = 0;
	for (int i = 1; i < nums.size(); i++) {
		if (nums[i] != nums[cur]) {
			nums[cur + 1] = nums[i];
			cur++;
		}
	}
	return cur + 1;
}

int main(){
	vector<int> nums{ 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
	int len = removeDuplicates(nums);
	for (int i = 0; i < len; i++) {
		printf("%d", nums[i]);
	}
	return 0;
}

