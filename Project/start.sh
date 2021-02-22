echo "The program will now launch a tmux session to display all the scripts at once"
echo "Exit the session prematurely by typing \"tmux kill-session\" on the terminal"
echo "Press enter to continue"
read dummyvar
tmuxp load tmux_config.yaml
echo "The system has self-destructed on `date`"
echo "The team that did it was `cat ./gotty/guilty.txt`"