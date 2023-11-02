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
import sys
import json
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()


class HBNBCommand(cmd.Cmd):
    prompt = "(hbtn) "

    def do_quit(self, args):
        """
        Quit command to exit the program

        """
        return True

    def do_EOF(self, args):
        """
        Exit the console (EOF).
        Syntax: EOF
        """
        print()
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


    def do_show(self, args):
        """
        Display the details of an instance.
        Syntax: show ClassName ID
        """
        if not args:
            print("** class name missing **")
            return

        frag = args.split()

        if len(frag) != 2:
            print("** instance id missing **")
            return

        if frag[0] not in globals():
            print("** class doesn't exist **")
            return

        instance = f"{frag[0]}.{frag[1]}"

        if instance not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[instance])

    def onecmd(self, line):
        commands = {
            'quit': self.do_quit,
            'eof': self.do_EOF,
            'help': self.do_help,
            'create': self.do_create,
            'show': self.do_show
        }

        if line:
            frag = line.split()
            command_name = frag[0]
            command_args = ' '.join(frag[1:])
            if command_name in commands:
                return commands[command_name](command_args)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
