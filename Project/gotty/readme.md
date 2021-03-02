# GoTTY

## Overview

Using the [GoTTY](https://github.com/yudai/gotty) library, a Python script is ran on a "terminal" that can be accessed from a web browser.

## GoTTY

Every time the page is loaded, it re-runs the script. Students must use the username gathered from the FTP section and the un-Vigenere'd password to login.

Every successful username or password entry are logged to help gives teams credit (in log.txt).

Once students successfully login, they must navigate through the "Metal Gear Control System" to self-destruct Metal Gear REX and complete the final objective.

Once a team initiates the self-destruct sequence, the script waits 5 seconds and runs a command to kill the tmux session, therefore ending the challenge. The team that does this is recorded in the guilty.txt file before exit.

## image2ascii

A program used to convert images to ASCII art to be displayed on the GoTTY webpage. It automatically sizes the art to fit the web terminal.

There is an amd64 binary included in this repo which has been pre-compiled, but an arm binary may have to be compiled if this project needs to run on a Raspberry Pi. Compile the project for the desired architecture from this repo [image2ascii](https://github.com/qeesung/image2ascii).