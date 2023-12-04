//
// Created by Jackie Gan on 11/21/23.
//

#include <cassert>
#include <iostream>
#include <string>
#include <fstream>

int part1(std::fstream &fs, std::string line, int floor){
    while (getline(fs,line)){
        for ( char& i : line){
            if(i == '('){
                floor += 1;
            }else if (i == ')'){
                floor -= 1;
            }
        }
    }
    return floor;
}

int part2(std::fstream &fs, std::string line, int floor, int pos) {
    while (getline(fs,line)){
        for (char& i : line) {
            if(i == '('){
                floor += 1;
            }else if (i == ')'){
                floor -= 1;
            }
            pos += 1;
            if (floor < 0){
                break;
            }
        }
    }
    return pos;
}

int main(int argc, char **argv) {

    std::string test("()(");
    std::fstream fs("/Users/jackiegan/fun/AOC/adventofcode15/input/d1/input.txt", std::fstream::in | std::fstream::out);
    std::string line;
    int floor = 0;
    int pos = 0;
    if (fs.is_open()) {
        int a = part1(fs, line, floor);
        fs.clear();
        fs.seekg(0);
        int b = part2(fs, line, floor, pos);

        std::cout << a << std::endl;
        std::cout << b;
    }
    fs.close();
    return 0;
}
