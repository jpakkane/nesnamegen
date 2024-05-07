#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# © 2024 Jussi Pakkanen

import sys, os, random

def cleaned(text):
    return text.replace('[', ' ').replace(']', ' ').replace('|', ' ').replace('video game', ' ').replace('(', ' ').replace(')', ' ').replace(':', ' ').replace('#', ' ')

class NesGen:
    def __init__(self):
        words = set()
        entries = []
        current = []
        for line in open('list.txt'):
            line = line.strip()
            if line == '|-':
                if 'Unreleased' not in current[-1]:
                    for w in cleaned(current[0].split("''")[1]).split():
                        words.add(w)
                current = []
            else:
                current.append(line)
        self.wordlist = [x for x in words]

    def w(self):
        return random.choice(self.wordlist)
        
    def print_names(self):
        print('Three word game names\n')
        for i in range(10):
            print(self.w(), self.w(), self.w())
        print('\n\nFour word game names\n')
        for i in range(10):
            print(self.w(), self.w(), self.w(), self.w())

if __name__ == '__main__':
    nesg = NesGen()
    nesg.print_names()

