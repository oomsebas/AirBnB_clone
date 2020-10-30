#!/usr/bin/python3
""" entry point to the console """

import cmd, sys
import readline

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ quit method """
        exit()

    def do_EOF(self, arg):
        """ EOF method """
        exit()

    def do_emptyline(self, arg):
        """ emptyline method """

    def do_precmd(self, line):
        """ post line """
        print("\n")


if __name__  == "__main__":
    HBNBCommand().cmdloop()
    HBNBCommand().postloop()
