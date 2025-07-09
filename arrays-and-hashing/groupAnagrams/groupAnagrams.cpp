#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

vector<vector<string>> groupAnagrams(vector<string> strs) {
    unordered_map<string, vector<string>> anagramsMap;

    for (const string word : strs) {
        int charCount[26] = {0};

        for (char c : word) {
            charCount[c - 'a']++;
        }

        string key;
        for (int count : charCount) {
            key += to_string(count) + "#";
        }

        anagramsMap[key].push_back(word);
    }

    vector<vector<string>> result;
    for (auto& entry : anagramsMap) {
        result.push_back(entry.second);
    }

    return result;
}

int main() {
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};

    vector<vector<string>> groups = groupAnagrams(strs);

    for (const auto& group : groups) {
        cout << "[ ";
        for (const auto& word : group) {
            cout << word << " ";
        }
        cout << "]\n";
    }

    return 0;
}