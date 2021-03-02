# METAL GEAR COVERT

CSC446/CYEN402 Final Project for team Big Covert.

Group Members:  Landry Baudouin, Jeremy Choyce, Jacob Mathews, Brandon Vessel

## Readme(s)

Documentation for each component is provided in its respective folder.

## Installation

To install necessary libraries and setup the user environment:

```bash
./install.sh
```

Allow the following ports IN through the firewall:

- ftp1 9611
- ftp2 9612
- timing 56540
- web interface 38941

## Usage

Launch the server in a tmux session using:

```bash
./start.sh
```

This allows the operator to see every script running and maintains its running status even if the terminal is closed.

The session will automatically terminate and clean up if the GoTTY session reaches the self-destruct stage.

To end the session prematurely:

```bash
stop
```
