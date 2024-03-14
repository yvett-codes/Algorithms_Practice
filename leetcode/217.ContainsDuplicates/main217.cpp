// STATUS: IN PROGRESS

#include <iostream>
#include <vector>
#include <map>

using namespace std;

bool containsDuplicate(vector<int>& nums) {
    map<int, int> pokedex;

    for (int i = 0; i < nums.size(); i++)
    {
        if (!pokedex[nums[i]]) {
            pokedex[nums[i]] = 1;
        }
        else {
            return true;
        }
    };
    return false;
};

int main()
{
    vector<int> input1 = {1, 2, 3, 1};
    vector<int> input2 = {1, 2, 3, 4};
    vector<int> input3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
    containsDuplicate(input1);
    containsDuplicate(input2);
    containsDuplicate(input3);
};