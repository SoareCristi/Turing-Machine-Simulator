# Turing-Machine-Simulator

Implemented a Python simulator for a Turing Machine with two heads and one
tape that loads and validates a configuration file

Created two configuration files for adding numbers and checking for the prefix of
a given word to test the simulator

If adding_numers config file is selected, the tape alphabet is 1 and +:
  Input example: 111+1
  Output: 1111______
 
If check_prefix config file is selected, the tape alphabet is 0, 1 and #
  Input example: 0100#01
  If 01 is a prefix of 0100 (True in this case), it will output Tape Iput Accepted
