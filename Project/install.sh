# python dependency for ftp server
python -m pip install pyftpdlib
python3 -m pip install pyftpdlib
py -m pip install pyftpdlib

# python library that creates lists with curses
python -m pip install pick
python3 -m pip install pick
py -m pip install pick

# apt-update
sudo apt-get update
# linux dependency for running all the consoles
sudo apt-get install tmux -y
# this is a python library for automating tmux
sudo apt-get install tmuxp -y
# install go
sudo apt-get install golang -y

# install gotty for the web page
go get github.com/yudai/gotty

# setup non-sudoer and non-ssh-able user for security
sudo useradd csc446 -m
echo "Created user \"csc446\""

# print password status
sudo passwd csc446 --status

# disable practical ssh for that user by setting a random password that is very long (20 random numbers 0-9)
RANDOM_PASSWORD=$(cat /dev/urandom | tr -dc '0-9' | fold -w 256 | head -n 1 | sed -e 's/^0*//' | head --bytes 20)
yes $RANDOM_PASSWORD | passwd csc446

echo "csc446 has been given a random password"

# make sure all files have accessible permissions
sudo chmod 777 -R *