#include <iostream>
#include <vector>

using namespace std;

int removeElement(vector<int>& nums, int val) {
	if (nums.size() == 0) {
		return 0;
	}
	if (nums.size() == 1) {
		if (nums[0] == val) {
			return 0;
		}
		else {
			return 1;
		}
	}

	int slow = 0;
	for (int fast = 0; fast < nums.size(); fast++) {
		if (nums[fast] != val) {
			nums[slow] = nums[fast];
			slow++;
		}
	}
	return slow;

}
int main(){
	vector<int> nums{ 0, 1, 2, 2, 3, 0, 4, 2 };
	int val = 2;
	int len = removeElement(nums, val);
	cout << len<<endl;
	for (int i = 0; i < len; i++) {
		cout<<nums[i];
	}
}
