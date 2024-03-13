#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <list>

using namespace std;

/*
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
    }
};
*/

// CPP Maps order in ascending order or alphabetically
int main()
{
    map<string, list<string> > pokedex;

    list<string> pikachuAttacks { "thunder shock", "tail whip", "quick attack" };
    list<string> charmanderAttacks { "flame thrower", "ember", "scary face" };
    list<string> chikoritaAttacks { "razor leaf", "tail poison powder", "vine whip" };

    pokedex.insert(pair<string, list<string> >("Pikachu", pikachuAttacks));
    pokedex.insert(pair<string, list<string> >("Charmander", charmanderAttacks));
    pokedex.insert(pair<string, list<string> >("Chikorita", chikoritaAttacks));

    for (auto pair : pokedex) {
        cout << pair.first << " - ";
        for (auto attack : pair.second)
            cout << attack << ", ";

        cout << endl;
    };
    // system("pause>0");
}

// int main()
// {
//     // First example
    
//     map<string, string> myDictionary;
//     myDictionary.insert(pair<string, string>("strawberry", "fresa"));
//     myDictionary.insert(pair<string, string>("banana", "platano"));
//     myDictionary.insert(pair<string, string>("orange", "naranja"));
//     myDictionary.insert(pair<string, string>("apple", "manzana"));

//     myDictionary["strawberry"] = "FRESA";
//     // myDictionary.clear();
//     cout << myDictionary.size() << endl;

//     for (auto pair : myDictionary) {
//         cout << pair.first << " - " << pair.second << endl;
//     }


//     system("pause>0");
// }





/*
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 0
            else:
                return True
        return False
*/