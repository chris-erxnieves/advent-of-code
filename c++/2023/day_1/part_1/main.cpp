#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string>* read_from_file(string fileName) {
    vector<string>* v = new vector<string>;
    string str;

    ifstream fin(fileName);
    while (fin >> str) {
        v -> push_back(str);
    }
    fin.close();

    return v;
}

int get_calibration_value(string *str) {
    char last, first = '\0';

    for (int i = 0; i < str -> length(); i++) {
        if (isdigit(str -> at(i))) {
            if (first == '\0') {
                first = str -> at(i);
            }
            last = str -> at(i);
        }
    }

    stringstream ss;
    ss << first << last;
    return stoi(ss.str());
}

int sum_calibration_values(string fileName) {
    vector<string>* v = read_from_file(fileName);

    int sum = 0;
    for (int i = 0; i < v -> size(); i++) {
        sum += get_calibration_value(&v -> at(i));
    }

    return sum;
}

int main() {
    cout << "---Example---" << endl << sum_calibration_values("example.txt") << endl;
    cout << "---Input---" << endl << sum_calibration_values("input.txt") << endl;

    return 0;
}