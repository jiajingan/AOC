//
// Created by Jackie Gan on 11/24/23.
//
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>



int main(int argc, char **argv) {

    std::string test("()(");
    std::fstream fs("/Users/jackiegan/fun/AOC/adventofcode15/input/d2/input.txt", std::fstream::in | std::fstream::out);
    std::string line;
    int floor = 0;
    int pos = 0;



    int length, width, height;
    std::string delim = "x";
    if (fs.is_open()) {
        while(getline(fs, line, '\n')){
            std::string token

//            std::cout<<line<<std::endl;
        }
//        int a = part1(fs, line, floor);
//        fs.clear();
//        fs.seekg(0);
//        int b = part2(fs, line, floor, pos);
//
//        std::cout << a << std::endl;
//        std::cout << b;
    }
    fs.close();
    return 0;
}
