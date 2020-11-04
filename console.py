#!/usr/bin/python3
""" entry point to the console """


import cmd
import sys
from models.base_model import BaseModel
import json
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """commands interpreter class"""

    prompt = '(hbnb) '
    __dirtec = {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity, "Place": Place,
                "Review": Review}

    def r_dic(self):
        return self.__dirtec

    def do_create(self, arg):
        """
        Function to create instance of class

        Usage:
            create <class_name>
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.r_dic().keys():
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
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.r_dic().keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_dic = storage.all()
            if all_dic:
                id_copy = all_dic.get(str(args[0]) + "." + str(args[1]))
                if id_copy:
                    print(id_copy)
                else:
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
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.r_dic().keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_dic = storage.all()
            id_copy = all_dic.get(str(args[0]) + "." + str(args[1]))
            if id_copy:
                all_dic.pop(args[0] + "." + args[1])
                storage.save()
            else:
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
        if len(args) < 1:
            list1 = []
            all_dict = storage.all()
            for key, value in all_dict.items():
                list1.append(str(value))
            print(list1)
        elif args[0] not in self.r_dic().keys():
            print("** class doesn't exist **")
        elif args[0] in self.r_dic().keys():
            list1 = []
            all_dict = storage.all()
            for key, value in all_dict.items():
                if args[0] in key:
                    list1.append(str(value))
            print(list1)

    def do_update(self, arg):
        """
        Updates an instance based on the keys
        by adding or updating attribute

        Usage:
            Class_name: instance class to be updated.
            Id: unique id of instance to be updated.
            Attribute name: atribute to be add or
            updated on instance dictionary.
            Attribute value: value of attribute name.

            $ update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif(args[0] not in self.r_dic().keys()):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all().keys():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            all_dict = storage.all()
            instance = all_dict.get(str(args[0]) + "." + str(args[1]))
            if instance and args[2] not in ["id", "created_at", "updated_at"]:
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
                d1 = {args[2]: x}
                instance.__dict__.update(d1)
                """storage.save()"""
            else:
                print("** no instance found **")

    def default(self, inp):
        """ Method for the advanced tasks """
        inp_split = inp.split(".")
        if inp_split[1] == "all()":
            return self.do_all(inp_split[0])
        elif inp_split[1] == "count()":
            return self.do_count(inp_split[0])
        elif "show" in inp_split[1]:
            try:
                id_ = inp_split[1].split("\"")
                return self.do_show(str(inp_split[0]) + " " + id_[1])
            except:
                print("Usage: <class name>.show(\"<id>\")")
        elif "destroy" in inp_split[1]:
            try:
                id_ = inp_split[1].split("\"")
                return self.do_destroy(str(inp_split[0]) + " " + id_[1])
            except:
                print("Usage: <class name>.destroy(\"<id>\")")
        elif "update" in inp_split[1]:
            try:
                s = str(inp_split[1])
                args = s[s.find("(")+1:s.find(")")].replace(",", " ")\
                    .replace("\"", "")
                return self.do_update(str(inp_split[0]) + " " + args)
            except:
                print("Usage: <class name>.update(\"<id>\",\
                        \"<attribute name>\", \"<attribute value>\")")

    def do_count(self, arg):
        """
        Count number of class instances
        """
        count = 0
        args = arg.split()
        if(args[0] not in self.r_dic().keys()):
            print("** class doesn't exist **")
        else:
            list1 = []
            all_dict = storage.all()
            for key, value in all_dict.items():
                if args[0] in key:
                    count += 1
            print(count)

    def do_quit(self, arg):
        """ quit method """
        return True

    def do_EOF(self, arg):
        """ EOF method """
        return True

    def emptyline(self):
        """ emptyline method """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
