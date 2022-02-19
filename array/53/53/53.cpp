// 53.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include <vector>
# include <cmath>

using namespace std;
int maxSubArray(vector<int>& nums) {
	if (nums.size() == 1){
		return nums[0];
	}
	int max_sub = nums[0]; /*整个数组的最大子数组值*/
	int i_max_sub = nums[0]; /*以第i个元素为结尾的最大子数组值*/
	for (int i = 1; i < nums.size(); i++) {
		i_max_sub = fmax(i_max_sub + nums[i], nums[i]);
		if (i_max_sub > max_sub) {
			max_sub = i_max_sub;
		}
	}
	return max_sub;
}

int main(){
	vector<int> nums{ -2, 1, -3, 4, -1, 2, 1, -5, 4 };
	cout << maxSubArray(nums);

}

