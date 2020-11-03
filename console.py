#!/usr/bin/python3
""" entry point to the console """

import cmd
import sys
from models.base_model import BaseModel
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """commans interpreter class"""

    prompt = '(hbnb) '
    __dirtec = {"BaseModel": BaseModel}

    def r_dic(self):
        return self.__dirtec

    def do_create(self, arg):
        """
        Function to create instance of class

        Usage:
            create <class_name>
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif(args[0] not in self.r_dic().keys()):
            print("** class doesn't exist **")
        else:
            instance = self.r_dic()[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Print string representation of an instance

        Usage:
            $ show <class_name> <id>
        Example:
            $ show BaseModel 1234-1234-1234
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.r_dic().keys():
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            all_dic = storage.all()
            if(all_dic):
                id_copy = all_dic.get(str(args[0]) + "." + str(args[1]))
                if(id_copy):
                    print(id_copy)
                    return
        print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance using the key

        Usage:
            $ destroy <class_name> <id>
        Example:
            $ destroy BaseModel 1234-1234-1234
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif(args[0] not in self.r_dic().keys()):
            print("** class doesn't exist **")
        elif((len(args) == 1) and (args[0] not in self.r_dic().keys())):
            print("** instance id missing **")
        else:
            all_dic = storage.all()
            if(all_dic):
                id_copy = all_dic.get(str(args[0]) + "." + str(args[1]))
                if(id_copy):
                    del all_dic[str(args[0]) + "." + str(args[1])]
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of
        all instances based or not on the class name

        Usage:
            Class_name is optional to print only
            all instances based on class_name

            $ all <class_name>
        """

        args = arg.split()
        lista = []
        all_dic = storage.all()
        if arg:
            if args[0] not in self.r_dic().keys():
                print("** class doesn't exist **")
                return
            else:
                for key, value in all_dic.items():
                    a = key.split(".")
                    if args[0] == a[0]:
                        lista.append(str(value))
                print(lista)
                return
        if all_dic:
            for key, value in all_dic.items():
                lista.append(str(value))
        print(lista)

    def do_update(self, arg):
        """
        Updates an instance based on the keys
        by adding or updating attribute

        Usage:
            Class_name --> instance class to be updated.
            Id --> unique id of instance to be updated.
            Attribute name --> atribute to be add or
            updated on instance dictionary.
            Attribute value --> value of attribute name.

            $ update <class name> <id> <attribute name> "<attribute value>"
        """

        args = arg.split()
        all_dic = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            if args[0] not in self.r_dic().keys():
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        if len(args) == 2:
            id_copy = all_dic.get(str(args[0]) + "." + str(args[1]))
            if id_copy is None:
                print("** no instance found **")
                return
            elif id_copy:
                print("** attribute name missing **")
                return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            x = int(args[3].replace('"', ''))
        except:
            try:
                x = float(args[3].replace('"', ''))
            except:
                try:
                    x = str(args[3].replace('"', ''))
                except:
                    pass
        setattr(all_dic[str(args[0]) + "." + str(args[1])], args[2], x)

    def do_quit(self, arg):
        """ quit method """
        exit()

    def do_EOF(self, arg):
        """ EOF method """
        exit()

    def do_emptyline(self, arg):
        """ emptyline method """

if __name__ == "__main__":
    HBNBCommand().cmdloop()
