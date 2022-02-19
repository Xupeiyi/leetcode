#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
	if (n == 0) {
		return;
	}
	if (m == 0) {
		nums1 = nums2;
		return;
	}
	int index1 = m - 1;
	int index2 = n - 1;
	for (int k = nums1.size() - 1; k >= 0; k--) {
		if (nums2[index2] >= nums1[index1]) {
			nums1[k] = nums2[index2];
			index2--;
		}
		else {
			nums1[k] = nums1[index1];
			index1--;
		}
		if (index2 < 0) break;
		if (index1 < 0) {
			for (int j = k - 1; j >= 0; j--) {
				nums1[j] = nums2[index2];
				index2--;
			}
			break;
		}
	}
}

int main(){
	vector<int> nums1{};
	vector<int> nums2{ 2, 5, 6 };
	merge(nums1, 0, nums2, 3);
	for (int n : nums1) {
		cout << n;
	}
}
