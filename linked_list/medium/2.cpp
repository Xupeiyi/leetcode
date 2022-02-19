#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

    void print(){
        ListNode* curr = this;
        while(curr != NULL){
            cout << curr->val << "->";
            curr = curr->next;
        }
        cout << endl;
    }
 };


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode* head = NULL;
        ListNode** curr = &head;
        while (l1 != NULL || l2 != NULL || carry){
            int v1 = l1 != NULL? l1->val : 0;
            int v2 = l2 != NULL? l2->val : 0;
            
            int sum = v1 + v2 + carry;
            int digit = sum % 10;
            carry = sum / 10;

            (*curr) = new ListNode(digit);
            curr = &(*curr)->next;
            if (l1 != NULL) l1 = l1->next;
            if (l2 != NULL) l2 = l2->next; 
        }
        return head;
    }
};


ListNode* build_list(const vector<int>& v){
    ListNode* head = NULL;
    ListNode** curr = &head;
    for (auto it = v.begin(); it != v.end(); it++){
        (*curr) = new ListNode(*it);
       curr = &(*curr)->next; 
    }
    return head;
}


int main(int argc, char** argv){
    Solution s;
    ListNode* n1 = build_list({9, 9});
    ListNode* n2 = build_list({9, 9});
    ListNode* n3 = s.addTwoNumbers(n1, n2);
    n3->print();
}