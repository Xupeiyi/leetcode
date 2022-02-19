#include <iostream>
#include <utility>

using namespace std;
 //Definition for a binary tree node.


  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
	void flatten(TreeNode* root) {
		/*a greedy approach. always move the right tree to left tree's rightest leaf*/
		TreeNode* curr = root;
		while (curr != nullptr) {
			if (curr->left != nullptr) {
				auto next = curr->left;
				// right_pre means curr->right's predecessor. it's the rightest leaf of curr->left
				auto right_pre = curr->left;
				while (right_pre->right != nullptr) {
					right_pre = right_pre->right;
				}
				//move the right child of curr to right's predecessor
				right_pre->right = curr->right;
				// modify curr
				curr->left = nullptr;
				curr->right = next;
			}
			curr = curr->right;
		}
	}
};


void printBT(const std::string& prefix, const TreeNode* node, bool isLeft){
	if (node != nullptr){
		cout << prefix;

		cout << (isLeft ? "├──  " : "└──  ");

		// print the value of the node
		cout << node->val << endl;

		// enter the next tree level - left and right branch
		printBT(prefix + (isLeft ? "│   " : "    "), node->left, true);
		printBT(prefix + (isLeft ? "│   " : "    "), node->right, false);
	}
}

void printBT(const TreeNode* node){
	printBT("", node, false);
}

// pass the root node of your binary tree

int main(){
	Solution s;

	TreeNode n0(3);
	TreeNode n1(4);
	TreeNode n2(2, &n0, &n1);
	printBT(&n2);
	s.flatten(&n2);
	printBT(&n2);
	
	return 0;
}

