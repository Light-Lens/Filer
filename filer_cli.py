from src.Filer import Filer

if __name__ == "__main__":
    txt = """
'#' means Comment (to be ignored)
'.' means DONE
'x' means NOT TO BE DONE (REMOVED FEATURE)
'\\\' means Continue the current line in a newline

........................................................................................................................
........................................................Non-Commands....................................................
........................................................................................................................
. Further clean the code, specially Obsidian and EntryPoint.
. If any .aos or any other .exe, .msi, .bat, .cmd, etc file executable exists in the 'PowerToys' folder make it a global command for AOs.
Fix the bug in Filer where it sometimes tries decrypt "099" for some reason. Debug it and fix it.

/* Not sure to do or not */
Make AOs launch with windows terminal using 'wt.exe AOs.exe'
Add a setup system on first startup of AOs [if aos.user file doesn't exist in 'Files.x72\\root' folder then only open the setup page, also don't ask for password].

........................................................................................................................
...........................................................Commands.....................................................
........................................................................................................................
/* AOs 2.6 features */
let -> Store data to a variable:
	To use the variable type '$[the-name-of-the-variable]'.
	'let' command can store any value to variables. Even store values from other commands like the 'datetime' command.

Direct/Indirect implementation of pastel in AOs. \\\
'include', 'import' command will import a '.pastel' and load all it's functions into AOs as make them work like in-built commands. \\\
Meaning if you have a pastel file having a function 'test' and comment on top of the defination of the function then you import that file using the 'include' command then the function test will work like any other AOs command. \\\
Meaning when you will type 'help test' you will get all the details including a help message from the comment on top of the defination of the very same function in the '.pastel' file. \\\
In the 'help' command the function will be listed, but only for that instance of AOs because include is not a permanent include.

If the input is 'powertoys::<file-name>', run the file from the 'PowerToys' folder without checking for similar executable files in the current folder.
If the input is 'startup::.startlist', run the '.startlist' from the 'Startup' folder.
If the input is 'startup::<file-name>', run the file from the 'Startup' folder without checking for similar executable files in the current folder.

/* Experimental commands */
@               -> Experimental commands

/* Flagged commands */
. clear           -> Clear the screen
. version         -> Display the AOs version
. about           -> About AOs
. shutdown        -> Shutdown the system
. restart         -> Restart the system
. exit            -> Exit AOs
. reload          -> Restart AOs
. credits         -> Credit for AOs
. time            -> Show time
. date            -> Show date
. datetime        -> Show both date and time
. generate        -> Generate a random number between 0 and 1
. ran             -> Display operating system configuration information
. tree            -> Graphically display the directory structure of a drive or path
. diagxt          -> Display AOs specific properties and configuration
. scan            -> Scan the integrity of all protected system files
. update          -> Check for AOs updates

/* Unflagged commands */
. shout           -> Display messages
. history         -> Display the history of Commands:
	-c, --clear:
		Clear the history

. console         -> Start a new instance of the terminal
. run             -> Start a specified program or command, given the full or sysenv path
. title           -> Change the title for AOs window
. color           -> Change the default AOs foreground and background colors
. time            -> Display current time and date
. wait            -> Suspend processing of a command for the given number of seconds
. pause           -> Suspend processing of a command and displays the message
. cat             -> Start an installed program from the system
x allinstapps     -> List all installed apps on your machine               [NOTE: it is now a part of cat. If no command is passed in cat then this command will automatically be called]
. prompt          -> Change the command prompt:
	-h, --help:
		Display all supported arguments

	-r, --reset, --restore, --default:
		$ (dollar sign, reset the prompt)

	-u, --username:
		%username%

	-s, --space:
		(space)

	-b, --backspace:
		(backspace)

	-v, --version:
		Current AOs version

	-t, --time:
		Current time

	-d, --date:
		Current date

	-p, --path:
		Current path

	-n, --drive:
		Current drive

x backup          -> Create a restore point of AOs                         [NOTE: Discontinued feature]
. ls              -> Display a list of files and subdirectories in a directory
. cd              -> Change the current directory                          [NOTE: cd.. is an independent/separate command which change the current directory to previous directory]
. touch           -> Create a file or folder
. del             -> Delete one or more files or folders
. ren             -> Rename a file or files
. copy            -> Advanced utility to copy files and directory trees
. move            -> Move one or more files from one directory to another directory
. pixelate        -> Start a website in a web browser:
	-e, --engine:
		Search for a query on a specific search engine (google, bing, duckduckgo, youtube, wikipedia)

	-w, --weather:
		Display today's weather in a city

	-t, --temp, --temperature:
		Display today's temperature in a city

. read            -> Display the contents of a text file
	-l, --line:
		Shows information about a specific line

. commit          -> Edit the contents of a text file:
	-l, --line:
		Edit specific line in a text file

. zip             -> Compresse or Decompresses files or folders (-u flag to unzip):
	-u, --uncompress, --decompress:
		Decompress zip files

x lock            -> Lock the System at Start-up                              [NOTE: Discontinued feature]
x restore         -> Restore system files and folders                         [NOTE: Discontinued feature]
x reset           -> Reset AOs                                                [NOTE: Discontinued feature]
x srh             -> Search for a specific query on the internet              [NOTE: Implemented in pixelate]
x wiki            -> Search for information on wikipedia                      [NOTE: Implemented in pixelate]
x ply             -> Search for a video on youtube based on a query           [NOTE: Implemented in pixelate]
x weather         -> Display today's weather in a city                        [NOTE: Implemented in pixelate]
x temperature     -> Display today's temperature in a city                    [NOTE: Implemented in pixelate]
x settings        -> Start the Windows settings page                          [NOTE: Included in 'cat' command]
.terminate       -> Terminate current running process
. filer           -> Encrypt any text

/* Developer features */
dev, developer	-> Developer tools:
	[
		NOTE: dev command will also maintain some build number for projects and will have more stuff in it,
		it will compile projects based on their file extentions.
	]

	-h, --help, ??, /?, -?:
		show info about any programming language, or a developer command

	cloc:
		Count the lines of code in a directory

	server:
		Start a local web-server

	clean:
		Delete temp/unnecessary files created by the programming language in the project

	git:
		Use git to maintain version control

	ver, version:
		Show the build no of the current project

	new (args_to_be_passed -> dotnet, python, g++, gcc, java, kotlin, go, rust, swift, node):
		Create a new project,
		setup build version control,
		configure it with the programming language,
		`git init` and ask for the github repo link,

	new (args_to_be_passed -> dirpath):
		code [dirpath]						[NOTE: default_value for dirpath is '.']

	[
		NOTE: you don't need to type `dev pastel test.pastel` to run the program,
		just do `dev test.pastel` or `dev my_progam.py` or `dev k.c++` and
		developer command will automatically identify the programming language.
		Create a 'aos.dev' file in 'aos.dev' folder in the root directory.
		'aos.dev' file will contain all the build and running related commands,
		it will provide a proper and customizable environment for the build system.
	]
#	[when no argument is passed]:
#		AOs				-> Run a AOs file
#		pastel			-> Run a Pastel project
#		dotnet			-> Build or run a .NET project
#		python			-> Run a Python project
#		g++				-> Build a C++ project
#		gcc				-> Build a C project
#		java			-> Run a Java project
#		kotlin			-> Run a Kotlin project
#		go				-> Build a Go project
#		cargo			-> Run a Rust project
#		swift			-> Run a Swift project
#		node			-> Run a JavaScript project
#		batch			-> Run a batch project

#	[
#		NOTE: you don't need to type `dev -c pastel test.pastel` to compile the program,
#		just do `dev -c test.pastel` or `dev -c my_progam.py` or `dev -c k.c++` and
#		developer command will automatically identify the programming language.
#	]
#	-b, -c, --build, --compile:
#		pastel			-> Run a Pastel project
#		dotnet			-> Build a .NET project
#		g++				-> Build a C++ project
#		gcc				-> Build a C project
#		java			-> Build a Java project
#		kotlin			-> Build a Kotlin project
#		go				-> Build a Go project
#		rust			-> Build a Rust project
#		swift			-> Build a Swift project

#	-e, --execute:
#		execute without build.
"""

    f = Filer(0.123)
    e = f.encrypt(txt)
    d = f.decrypt(e)

    print(d)

# from pprint import pprint
# import argparse, sys, os

# # Initialize command-line arguments.
# parser = argparse.ArgumentParser(description="A powerful text encryption and decryption program.")
# encrypt_or_decrypt_group = parser.add_mutually_exclusive_group(required=True)
# text_or_file_input_group = parser.add_mutually_exclusive_group(required=True)

# parser.add_argument("-s", help="A random seed in the range (0, 1) that acts like a password", type=float, required=True)
# parser.add_argument("-o", help="Place the output into <file>.")
# parser.add_argument("-m", help="The maximum length of a string in each chunk.", type=int, default=4)
# parser.add_argument("-c", help="The common exponent used with the random encryption key to encrypt or decrypt text", type=int, default=8)

# encrypt_or_decrypt_group.add_argument("-e", help="Encrypt", action="store_true")
# encrypt_or_decrypt_group.add_argument("-d", help="Decrypt", action="store_true")

# text_or_file_input_group.add_argument("-t", help="Text input from the command line.")
# text_or_file_input_group.add_argument("-f", help="Takes a text file as an input.")

# args = parser.parse_args()

# # Check for the input source and append all the input texts to the inputs list.
# inputs = []
# if args.t:
#     inputs.append(args.t)

# elif args.f:
#     if os.path.isfile(args.f) == False:
#         print(f"{args.f}: No such file or directory")
#         sys.exit()

#     file = open(args.f, "r")
#     for i in file.readlines():
#         inputs.append(i[:-1])
#     file.close()

# # Initialize Filer and start encrypting or decrypting.
# list_of_outputs = []
# filer = Filer(args.s)
# filer.max_len = args.m
# filer.common_exponent = args.c

# if args.e:
#     for encrypted_text in inputs:
#         output = [str(i) for i in filer.encrypt(encrypted_text)]
#         list_of_outputs.append(output)

# elif args.d:
#     for encrypted_text in inputs:
#         new_encrypted_text = [float(i) for i in encrypted_text.split()]
#         list_of_outputs.append(filer.decrypt(new_encrypted_text))

# # Print or save the output
# if args.o:
#     file = open(args.o, "w")

#     if args.e:
#         for output in list_of_outputs:
#             file.write(" ".join(output) + "\n")

#     elif args.d:
#         for output in list_of_outputs:
#             file.write(output + "\n")

#     file.close()

# else:
#     pprint(list_of_outputs)
