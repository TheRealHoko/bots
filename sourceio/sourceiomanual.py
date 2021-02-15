#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description="Plays the game for you ;)")
parser.add_argument("dif", help="difficulty")
parser.add_argument("word", help="word", type=int)
args = parser.parse_args()

if args.dif == 'e':
	f = open("e.dict", 'r', newline=None)

if args.dif == 'm':
	f = open("m.dict", 'r', newline=None)

if args.dif == 'h':
	f = open("h.dict", 'r', newline=None)

if args.dif:
	contents = f.readlines()
	print(contents[args.word])
f.close()
