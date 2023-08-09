#!/usr/bin/python3
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

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command to quit the program"""

        return True

    def do_EOF(self, arg):
        """Ctr D to exit the program"""

        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the
        JSON file) and prints the id. Ex: $ create BaseModel"""

        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        if arg is None or arg == '':
            print("** class name missing **")
        elif arg not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            obj = class_dict[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234."""

        class_list = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]

        if arg is None or arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(args[0], None)
                if obj is None:
                    print("** no instance found **")
                else:
                    print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234"""

        class_list = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]

        if arg is None or arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(args[0], None)
                if obj is None:
                    print("** no instance found **")
                else:
                    storage.all().pop(key)
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all."""

        class_list = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]

        if arg is None or arg == "":
            for key, value in storage.all().items():
                print(value)
        else:
            if arg in class_list:
                for key, value in storage.all().items():
                    class_name = key.split(".")[0]
                    if arg == class_name:
                        print(value)
                        break
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the
        JSON file). Ex: $ update BaseModel 1234-1234-1234 email
        "aibnb@mail.com" """

        class_list = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]

        if arg is None or arg == '':
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in class_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                obj = storage.all().get(args[0], None)
                if obj is None:
                    print("** no instance found **")
                else:
                    if len(args) < 3:
                        print("** attribute name missing **")
                    else:
                        value = obj.__dict__.get(args[2], None)
                        if value is None:
                            print("** value missing **")
                        else:
                            new_value = args[3].split("\"")
                            if len(new_value) == 3 and new_value[2] != "":
                                obj.__dict__[args[2]] = new_value[1]
                                obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
