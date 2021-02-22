# start the tmux window
tmuxp load tmux_config.yaml

# kill everything the csc446 user has running
skill -KILL -u csc446

# print a message for the operator
echo "The system has self-destructed on `date`"
echo "The team that did it was `cat ./gotty/guilty.txt`"