#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_quit(self, command):
        """Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """Handles EOF to exit program"""
        print()
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF"""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the emptyline method of CMD"""
        pass

    def do_create(self, args):
        """Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        class_name = arg_list[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.classes[class_name]()

        for arg in arg_list[1:]:
            param = arg.split('=')
            key = param[0]
            val = param[1]

            if val[0] == '\"':
                val = val.replace('\"', '').replace('_', ' ')
            elif '.' in val:
                val = float(val)
            else:
                val = int(val)

            setattr(new_instance, key, val)

        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """Help information for the create method"""
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Method to show an individual object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        obj = storage.all().get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def help_show(self):
        """Help information for the show command"""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroys a specified object"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        objs = storage.all()

        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for the destroy command"""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Shows all objects, or all objects of a class"""
        print_list = []
        objs = storage.all()

        if args:
            class_name = args.split(' ')[0]
            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, obj in objs.items():
                if key.split('.')[0] == class_name:
                    print_list.append(str(obj))
        else:
            for obj in objs.values():
                print_list.append(str(obj))

        print(print_list)

    def help_all(self):
        """Help information for the all command"""
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """Count current number of class instances"""
        count = 0
        objs = storage.all()
        for key in objs:
            if args == key.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """Help information for the count command"""
        print("Usage: count <class_name>")

    def do_update(self, args):
        """Updates a certain object with new info"""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        objs = storage.all()

        if key not in objs:
            print("** no instance found **")
            return

        obj = objs[key]
        args = new[2]

        if not args:
            print("** attribute name missing **")
            return

        args = args.split(' ')

        if args[0] == '{' and args[-1] == '}' and type(eval(' '.join(args))) is dict:
            kwargs = eval(' '.join(args))
            for k, v in kwargs.items():
                setattr(obj, k, v)
        else:
            if len(args) < 2:
                print("** value missing **")
                return
            setattr(obj, args[0], args[1])

        storage.save()

    def help_update(self):
        """Help information for the update command"""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
