#include <iostream>
using namespace std;


vector<int> Inorder(TreeNode* root){
    if (root == NULL)
        return;
    Inorder(root->left);
    ans.push_back(root-> val);
    Inorder(root->right);
    return ans;

}
