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


class HBNBCommand(cmd.Cmd):
    prompt = "(hbtn) "

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        """
        Exit the console (EOF).
        Syntax: EOF
        """
        print()
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def onecmd(self, line):
        command_map = {
            'quit': self.do_quit,
            'eof': self.do_EOF,
            'help': self.do_help
        }

        if line:
            frag = line.split()
            command_name = frag[0].lower()
            command_args = ' '.join(frag[1:])
            if command_name in command_map:
                return command_map[command_name](command_args)
            else:
                print(f"Command not found: {command_name}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
