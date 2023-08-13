#!/usr/bin/python3
""" a program called console.py """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ a program called console.py that contains the entry point
    of the command interpreter"""

    __class_list = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the
        JSON file) and prints the id. Ex: $ create BaseModel"""

        if arg is None or arg == '':
            print("** class name missing **")
        elif arg not in HBNBCommand.__class_list:
            print("** class doesn't exist **")
        else:
            obj = eval(arg.split()[0] + "()")
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234."""

        if arg is None or arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.__class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(key, None)
                if obj is None:
                    print("** no instance found **")
                else:
                    print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""

        if arg is None or arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.__class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(key, None)
                if obj is None:
                    print("** no instance found **")
                else:
                    storage.all().pop(key)
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all."""

        obj_list = []
        if arg is None or arg == "":
            for obj in storage.all().values():
                obj_list.append(obj.__str__())
            print(obj_list)
        else:
            args = arg.split()
            if arg in HBNBCommand.__class_list:
                for obj in storage.all().values():
                    if args[0] == obj.__class__.__name__:
                        obj_list.append(obj.__str__())
                print(obj_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the
        JSON file). Ex: $ update BaseModel 1234-1234-1234 email
        "aibnb@mail.com" """

        if arg is None or arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in HBNBCommand.__class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(key, None)
                if obj is None:
                    print("** no instance found **")
                else:
                    if len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        """value = obj.__dict__.get(args[2], None)"""
                        obj.__dict__[args[2]] = args[3].lstrip('"').rstrip('"')
                        obj.save()

    def do_quit(self, arg):
        """Command to quit the program"""

        return True

    def do_EOF(self, arg):
        """Ctr D to exit the program"""
        print('\n')
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
