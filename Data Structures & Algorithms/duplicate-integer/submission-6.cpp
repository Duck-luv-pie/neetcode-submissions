#include <set>
#include <vector>
#include <iostream>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> set1(nums.begin(), nums.end());

        if ((nums).size() != (set1).size()){
            return true;
        } else{
            return false;
            }

    }
};