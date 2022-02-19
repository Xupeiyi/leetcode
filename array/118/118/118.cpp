#include <iostream>
#include<vector>

using namespace std;

vector<vector<int>> generate(int numRows) {
	vector<vector<int>> res{ vector<int>{1} };
	if (numRows == 1) {
		return res;
	}
	for (int r = 1; r < numRows; r++) {
		vector<int> row(r + 1, 1);
		for (int col = 1; col < row.size() - 1; col++) {
			row[col] = res[r - 1][col - 1] + res[r - 1][col];
		}
		res.push_back(row);
	}
	return res;
}

int main(){
	vector<vector<int>> res = generate(5);
	for (auto row : res) {
		for (auto n : row) {
			cout << n;
		}
		cout << endl;
	}
}
