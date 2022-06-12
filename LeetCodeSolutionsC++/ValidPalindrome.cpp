#include <cctype>
#include <iostream>
#include<string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        
        string fixedString = "";
        s.erase(remove_if(s.begin(), s.end(), ::isspace), s.end());
        s.erase(remove_if(s.begin(), s.end(), ::ispunct), s.end());
        
        for(auto i : s){
            fixedString += tolower(i);
        }
     
        int left = 0;
        int right = s.length() - 1;
        
        while(left < right){
            if(tolower(fixedString[left]) != tolower(fixedString[right]))
                return false;
            left++;
            right--;
        }
        
        return true;
        
    }
};
  
int main(){
    Solution c;
    bool ans = c.isPalindrome("A man, a plan, a canal: Panama");
    cout << ans;
    return 0;
}