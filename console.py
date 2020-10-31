#!/usr/bin/python3
""" entry point to the console """

import cmd, sys
import readline
from models.base_model import BaseModel
import json
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __dirtec = {"BaseModel":BaseModel}

    def r_dic(self):
        return self.__dirtec

    def do_create(self, arg):
        args = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif(args[0] not in self.r_dic().keys()):
            print("** class doesn't exist **")
        else:
            instance = self.r_dic()[args[0]]()
            instance.save()
            print(instance.id)
        
    def do_show(self, arg):
        if len(arg) < 3:
            print("** class name missing **")
        elif(arg[2] is not BaseModel):
            print("** class doesn't exist **")
        elif(len(arg < 4)):
            print("** instance id missing **")
        else:
            all_dic = storage.all()
            for key in all_dic:
                id_copy = key.get(id)
                if arg[4] is id_copy:
                    print(key)
                    return
            print("** no instance found **")

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
