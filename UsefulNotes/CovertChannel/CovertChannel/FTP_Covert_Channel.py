#########################################################
#   CSC - 442 Spring 2019
#   Github: ***PRIVATE*** marcusjr98/CSC442
#   Phoenicians' FTP Covert Channel Decoder
#   This program was written and tested using Python 2.7,
#   but it seems to work in Python 3.7 as well
#########################################################

from ftplib import FTP

# Define variables for what FTP server to connect to and what directory and bit encoding
FTP_SERVER_NAME = 'jeangourd.com'
METHOD = 7
DIRECTORY = ''


def create_file_permissions_list(raw_files):
    file_permissions = []
    for raw_file in raw_files:
        # Strip off only the file permissions
        file_permission = str(raw_file)[0:10]
        # Check if the file permissions are valid if using encoding less than 10
        if METHOD < 10 and check_for_dashes(file_permission):
            file_permissions.append(file_permission[(10 - METHOD):10])
        elif METHOD == 10:
            file_permissions.append(file_permission)
    return file_permissions


def check_for_dashes(given_file_permission):
    for i in range(10-METHOD):
        if given_file_permission[i] != '-':
            return False
    return True


def convert_file_to_bit_string(file_perms):
    message = ''
    for fileP in file_perms:
        binary_string = ''
        # Generate the binary string with '-' being a 0 and anything else being a 1
        for letter in fileP:
            if letter != '-':
                binary_string = binary_string + '1'
            else:
                binary_string = binary_string + '0'
        message = message + binary_string
    return message


# The Binary decoder to convert the bit string into letters
def binary_decoder(number, n):
    split_binary = [number[i:i + n] for i in range(0, len(number), n)]
    letters = []
    for i in range(len(split_binary)):
        letters.append(int(split_binary[i], 2))
    final_message = ''
    for letter in letters:
        final_message = final_message + chr(letter)
    return final_message


def main():
    files = []
    # Connect to FTP server
    ftp = FTP(FTP_SERVER_NAME)
    ftp.login()
    ftp.cwd(DIRECTORY)
    ftp.retrlines('LIST', files.append)
    files_to_decode = create_file_permissions_list(files)
    decoded_binary_string = convert_file_to_bit_string(files_to_decode)
    print(binary_decoder(decoded_binary_string, 7))


main()
