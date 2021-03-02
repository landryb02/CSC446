# FTP Permsissions

First step of challenge. Teams must traverse through the ftp servers to listen in on conversations encoded in the permissions of the files.

## FTP Servers 1 and 2

Each server houses several folders corresponding to a different conversation. The numbers on each server match up, so conversation 1 is happening in folder on on both servers.

Server 1 is hosted in the folder "public1" and Server 2 is hosted in the folder "public2".

If the folders do not already exist, the program will make them.

## Conversation Engine

Creates files with encoded permissions based on the information from the conversations folder for FTP servers.

Pre-computes the file permissions for every message in each conversation. The script iterates in a while loop through each conversation moving the dialogue forward and updating the files and permissions as it does so.

The filenames chosen come from a list of 5-letter words that start with 'S'.

## Information for challenge

There isn't any configuration to do here besides changing the ports and conversation update interval (SERVER_UPDATE_WAIT), which determines how many seconds should pass (roughly. ignores encoding time taken) between the dialogue updates of a single conversations (applies to each of them).