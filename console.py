#!/usr/bin/python3
"""
This script creates a simple interactive console (REPL) for the HBNB application.
Users can enter commands to interact with the application.
Available commands include 'quit' to exit, 'help' to display help,
and 'EOF' to exit (typically triggered by Ctrl-D).

To use the console, run the script, and then enter commands at the '(hbtn)' prompt.

Available commands:
- quit: Exit the console
- EOF: Exit the console (Ctrl-D)
- help: Display help for other commands
"""
import cmd

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


storage = FileStorage()


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class defining the commands and functionalities of
    the custom command interpreter.
    Use "help" to get a list of the commands.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """A method to handle an empty command (which is ignored)"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Recognizes EOF"""
        return True

    def do_create(self, arg):
        """
        create a new_instance
        syntax: create ClassName
        """
        if not arg:
            print("** class name missing **")
            return

        if arg not in globals():
            print("** class doesn't exist **")
            return

        classe = globals()[arg]
        add_instance = classe()

        storage.save()

        print(add_instance.id)


    def do_show(self, arg):
        """
        Display the details of an instance.
        Syntax: show ClassName ID
        """
        if not arg:
            print("** class name missing **")
            return

        frag = arg.split()

        if frag[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(frag) != 2:
            print("** instance id missing **")
            return


        instance = f"{frag[0]}.{frag[1]}"

        if instance not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[instance])

    def do_destroy(self, arg):
        """
        Delete an instance and save the json file
        syntax: destroy ClassName ID
        """
        if not arg:
            print("** class name missing **")
            return

        frag = arg.split()

        if frag[0] not in globals():
            print("** class doesn't exist **")
            return

        if len(frag) != 2:
            print("** instance id missing ** ")
            return

        instance = f"{frag[0]}.{frag[1]}"
        if instance not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[instance]
        storage.save()

    def do_all(self, arg):
        """
        print all instance in string representation

        all BaseModel
        all
        """
        if not arg:
            print([str(storage.all()[id]) for id in storage.all()])
            return

        if arg not in globals():
            print("** class doesn't exist **")
            return

        instances = []

        for instance in storage.all():
            if arg in instance:
                instances.append(str(storage.all()[instance]))

        print(instances)

    def do_update(self, arg):
        """
        update a instance attribute by ID and ClassName
        update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        if len(arg) < 3:
            print("** attribute name missing **")
            return

        if len(arg) < 4:
            print("** value missing **")
            return

        frag = arg.split()

        instance = f"{frag[0]}.{frag[1]}"

        if not instance in storage.all():
            print("** no instance found **")
            return

        setattr(storage.all()[instance], frag[2], frag[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
