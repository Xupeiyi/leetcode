#include <iostream>
#include<vector>

using namespace std;

int breakfastNumber(vector<int>& staple, vector<int>& drinks, int x) {
	// x 取 i 时，staple 中有 less_than[i] 个元素小于等于 x。
	vector<int> less_than(x + 1, 0);
	for (auto i = staple.begin(); i != staple.end(); i++) {
		if (*i <= x) {
			less_than[*i]++;
		}
	}
	for (auto i = 1; i <= x; i++) {
		less_than[i] = less_than[i] + less_than[i - 1];
	}
	
	// 对于 drinks 中的第 i 个元素， 
	// staple 中价格不超过 max_staple_price = x - drinks[i] 的元素有
	// count[max_staple_price]个（若 max_staple_price >= 0)。
	int max_staple_price;	long int ans = 0;
	for (auto i = drinks.begin(); i != drinks.end(); i++) {
		max_staple_price = x - *i;
		if (max_staple_price >= 0) {
			ans += less_than[max_staple_price];
		}
	}
	return ans % 100'000'0007;
}

int main(){
	vector<int> staple{ 2, 1, 1 };
	vector<int> drinks{ 8, 9, 5, 1 };
	cout << breakfastNumber(staple, drinks, 9);
}

