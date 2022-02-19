#include <iostream>


struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
	void print() {
		ListNode* curr = this;
		while (curr != NULL) {
			std::cout << curr->val << "->";
			curr = curr->next;
		}
		std::cout << std::endl;
	}
};

ListNode* findMid(ListNode* head) {
	// mid is at the end of the first half (include the middle one)
	ListNode* fast = head;
	ListNode* slow = head;
	while (fast->next != NULL && fast->next->next != NULL) {
		fast = fast->next->next;
		slow = slow->next;
	}
	return slow;
}

ListNode* reverseList(ListNode* head) {
	ListNode* prev = NULL;
	ListNode* curr = head;
	ListNode* next;
	while (curr != NULL) {
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return prev;
}


class Solution {
public:
	bool isPalindrome(ListNode* head) {
		ListNode* mid = findMid(head);
		ListNode* reversed = reverseList(mid->next);

		bool res = true;
		ListNode* r = reversed;
		while (r != NULL) {
			if (head->val != r->val) {
				res = false;
				break;
			}
			head = head->next;
			r = r->next;
		}
		mid->next = reverseList(reversed);
		return res;
	}
};



int main(){
	Solution s;
	
	ListNode* n0 = new ListNode(1);
	ListNode* n1 = new ListNode(2, n0);

	std::cout << s.isPalindrome(n1) << std::endl;

	n1->print();
}

