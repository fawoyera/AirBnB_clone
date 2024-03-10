#!/usr/bin/python3

"""
Entry Point for Command Interpreter

This module defines the `HBNBCommand` class, which subclasses `cmd.Cmd`.
It provides a command-line interface for interacting with a storage system
(FileStorage / DB). These abstractions enable easy manipulation of data models
and objects without extensive codebase updates.

Features:
- Interactively and non-interactively manage data models and objects.
- Supports operations like creation, updating, and deletion.
- Persists objects to a file in JSON format.

Usage Example:
    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit
"""

import cmd
import sys
import re
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command Interpreter

    This class represents the command interpreter, serving as the control
    center of the project. It defines handlers for all commands inputted
    in the console and calls the appropriate storage engine APIs to manipulate
    application data/models.
    """
    classes = {
        "BaseModel": BaseModel, "User": User, "State": State, "City": City,
        "Amenity": Amenity, "Place": Place, "Review": Review
    }
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    # Set the prompt message
    prompt = '(hbnb) '

    # Handl the empty line behavior
    def emptyline(self):
        """Do nothing on empty line"""
        pass

    # Quit
    def do_quit(self, line):
        """Quit the program.
        """
        return True

    # EOF
    def do_EOF(self, line):
        """Exit the program in case of EOF.
        """
        print('')
        return True

    # Help
    def do_help(self, arg):
        """To get help, tape help <topic>.
        """
        return super().do_help(arg)

    # Create
    def do_create(self, className):
        """Create a new instance of any class
        [Usage]: create <class name>

        The available classes are:
        - BaseModel
        """
        if not className:
            print("** class name missing **")
            return

        if className not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[className]()
        storage.save()
        print(new_instance.id)

    # Show
    def do_show(self, line):
        """Print the string representation of an instance
        based on the class name and id
        [Usage]: show <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return
        else:
            args = line.split()

        className = args[0]
        if className not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instanceId = args[1]
        try:
            print(storage._FileStorage__objects[className + '.' + instanceId])
        except KeyError:
            print("** no instance found **")

    # Destroy
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        [Usage]: destroy <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return
        else:
            args = line.split()

        cName = args[0]
        if cName not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instanceId = args[1]
        try:
            storage._FileStorage__objects.__delitem__(cName + '.' + instanceId)
            storage.save()
        except KeyError:
            print("** no instance found **")

    # All
    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        Usage: all <class name (optional>
        """
        objects_list = []

        if not line:
            for key, value in storage._FileStorage__objects.items():
                objects_list.append(str(value))
        else:
            className = line.split(' ')[0]
            if className not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage._FileStorage__objects.items():
                    if key.split('.')[0] == className:
                        objects_list.append(str(value))

        print(objects_list)

    # Update
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute

        Usage: update <class name> <id> <attribute name> <attribute value>
        [!Important] Only one attribute can be updated at the time
        """
        if not line:
            print("** class name missing **")
            return

        if line.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        args = line.split()

        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_key = args[2].strip('"')

        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3].strip('"')

        # Casting the attribute value if neccessary
        if attr_key in self.types:
            attr_value = self.types[attr_key](attr_value)

        instance = storage.all()[key]
        setattr(instance, attr_key, attr_value)
        storage.save()

    # Count
    def do_count(self, line):
        """Count the number of class instances
        [Usage]: count <class name>
        """
        if not line:
            print("** class name missing **")
            return

        className = line.split()[0]
        if className not in self.classes:
            print("** class doesn't exist **")
            return

        instancesNumber = 0
        for key, value in storage._FileStorage__objects.items():
            if key.split('.')[0] == className:
                instancesNumber += 1
        print(instancesNumber)

    # Modify the precmd to handl special calls
    def precmd(self, line):
        # Handel <class name>.all()
        if ".all()" in line:
            className = line.split('.')[0]
            return f"all {className}"

        # Handel <class name>.count()
        if ".count()" in line:
            className = line.split('.')[0]
            return f"count {className}"

        # Handel <class name>.show(<id>)
        if ".show(" in line and ')' in line:
            className = line.split('.')[0]
            instanceId = line.split('(')[1].split(')')[0]
            return f"show {className} {instanceId}"

        # In case no special command found
        else:
            return line


# Call The cmd loop to start the program
if __name__ == '__main__':
    HBNBCommand().cmdloop()
