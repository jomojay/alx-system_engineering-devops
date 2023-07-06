# Shell Permissions

This project took through the file/directory permissions, as well as ownership manipulation among many other concepts.

## task 0
    This script switches the current user to the user betty. Assuming that user betty is created already.

## task 1
    `1-who_am_i` script that prints the effective username of the current user.

## task 2
    `2-groups` is a script that prints all the groups the current user is part of.

## task 3
    `3-new_owner` a script that changes the owner of the file hello to the user betty.

## task 4
    `4-empty` is a script that creates an empty file called hello.

## task 5
    `5-execute` is a script that adds execute permission to the owner of the file hello. Assuming that the file hello is already in the the working directory.

## task 6
    `6-multiple_permissions` is a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello. Assuming that the file hello is already in the the working directory.

## task 7
    `7-everybody` is a script that adds execution permission to the owner, the group owner and the other users, to the file hello. No comma should used and it is assumed that the file hello is already in the the current working directory.

## task 8
    8-james_bond is a script that sets the permission to the file hello as follows:
        Owner: no permission at all
        Group: no permission at all
        others: all the permissions
    No comma should used and it is assumed that the file hello is already in the the current working directory.

## task 9
    `9-John_Doe` is a script that sets the mode of the file hello to this:
        `-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`

## task 10
    `10-mirror_permissions` a script that sets the mode of the file hello the same as olleh’s mode.
        The files olleh & hello are assumed to be in the working directory. The script works for any file mode.

## task 11
    `11-directories_permissions` is a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be affected.

## task 12
    `12-directories_permissions` is a script that creates a directory called my_dir with permissions 751 in the working directory.

## task 13
    `13-change_group` is a script that changes the group owner to school for the file hello. Hello is assumed to be in the working directory.

## task 14
    `100-change_owner_and_group` is a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

## task 15
    a script that changes the owner and group owner of _hello to vincent and staff respectively. _hello is a symlink and its assumed to be in the working directory.

## task 16
    `102-if_only` is a script that changes the owner of the file hello to betty only if it is owned by the user guillaume. hello is assumed to be in the working directory.

## task 17
    `103-star_wars` is a script that will play the StarWars IV episode in the terminal.
