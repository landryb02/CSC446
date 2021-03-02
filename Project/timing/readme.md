# Timing Channel

## Overview

Second step of the challenge. Teams must decrypt a secret message based on the timing of the characters being sent by the chat server.

## Chat Server

Sends an over message per character using four different timings. Each timing corresponds to one of four two-bit combination (00, 01, 10, 11), and every 4 two-bit combinations combinations correspond to an 8 bit ASCII character.

## Information for Challenge

The overt message can be anything as long as it is at least 2*(x + 1) characters long where x is the length of the covert message.

The covert message is the key used to un-Vigenere the encrypted password for the GoTTY login.