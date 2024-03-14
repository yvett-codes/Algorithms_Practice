// STATUS: IN PROGRESS

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <list>

using namespace std;

// CPP Maps order in ascending order or alphabetically
int main()
{
    map<string, list<string> > pokedex;

    list<string> pikachuAttacks { "thunder shock", "tail whip", "quick attack" };
    list<string> charmanderAttacks { "flame thrower", "ember", "scary face" };
    list<string> chikoritaAttacks { "razor leaf", "tail poison powder", "vine whip" };
    list<string> articunoAttacks { "flappy bird", "ice bean", "blizzard" };

    pokedex.insert(pair<string, list<string> >("Pikachu", pikachuAttacks));
    pokedex.insert(pair<string, list<string> >("Charmander", charmanderAttacks));
    pokedex.insert(pair<string, list<string> >("Chikorita", chikoritaAttacks));
    pokedex.insert(pair<string, list<string> >("Articuno", articunoAttacks));

    for (auto pair : pokedex) {
        cout << pair.first << " - ";
        for (auto attack : pair.second)
            cout << attack << ", ";

        cout << endl;
    };
    // system("pause>0");
}