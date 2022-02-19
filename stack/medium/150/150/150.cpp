#include <iostream>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int binOperation(char op, int lhs, int rhs) {
	int result;
	switch(op){
		case '+':
			result = lhs + rhs;
			break;
		case '-':
			result = lhs - rhs;
			break;
		case '*':
			result = lhs * rhs;
			break;
		case '/':
			result = lhs / rhs;
			break;
	}
	return result;
}

bool isOperator(const string& token) {
	return (token == "+" || token == "-" || token == "*" || token == "/");
}

class Solution {
public:
	int evalRPN(vector<string>& tokens) {
		stack<int> expression;
		for (string token : tokens) {
			if (isOperator(token)) {
				int rhs = expression.top();
				expression.pop();
				
				int lhs = expression.top();
				expression.pop();
				
				int result = binOperation(token[0], lhs, rhs);
				expression.push(result);
			}
			else {
				int num = atoi(token.c_str());
				expression.push(num);
			}
		}
		return expression.top();
	}
};

int main() {
	Solution s;
	vector<string> nums{ "2", "1", "+", "3", "*" };
	cout << s.evalRPN(nums) << endl;
}

