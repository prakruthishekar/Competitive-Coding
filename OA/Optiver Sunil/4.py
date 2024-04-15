# A friend asks you to tune into a local numbers station, a radio station that is 
# publishing a coded message. They say they've had a tip on how to decipher the messages 
# the station is publishing, but want your help in writing a program that will do the 
# deciphering. You start listening to the station and notice that in each voice sample
# the person reads out a number follow by letter or a hyphen -.
# The numbers don't seem to be in any particular order..

# You decide that you're going to help write the program, so your friend shares what the tip was
# • Every sample will contain a number which can be used to put the messages in order 
# (sequence ID).
# • Every message only contains the letters a-z.
# • A complete message is a continuous set of characters surrounded by two - characters.
# • Sometimes a message is never completed (missing sequence IDs)
# • Once you've completed a full message, I messages
# completed later with a lower sequence ID are no longer useful and shouldn't be output 
# (you should only output the latest message).
# • If two full messages are completed at the same time, then you should output only 
# the message containing higher sequence IDs.
# • A full broadcast can contain multiple complete messages and you will need to output 
# each of them.

# Function Description
# You are to implement the function ProcessSample that takes:
# • a sequence number for the sample,
# • the character for the sample.
# Whenever a full message is completed you should call the OnMessageComplete function 
# with the completed message.
# Constraints
# • 0 < sequence id < 264 _ 1
# • number of messages >= 1
# Input Format
# For each line, the first string is the sequence number associated with the sample, 
# the second cliaracter is the character related to the sequence number.

# sample Input
# 1 -
# 2 h
# 3 е
# 4 l
# 5 l
# 6 o
# 7 -
# 8 b
# Sample Output
# hello
# Explanation
# When the samples are placed in order according to their sequence IDs we get the 
# following, -hell-b. There is one complete message here (between the so it is output.




class Printer:
    def on_message_complete(self, message):
        print(message)


class Decoder:
    def __init__(self, printer):
        self.printer = printer
        self.message = ""
        self.seq = -1
        self._found = False

    def process_sample(self, sequence, character):
        if character == '-':
            if self.message:
                self.printer.on_message_complete(self.message)
                self.message = ""
            self._found = True
        else:
            if self._found:
                self.message += character
            else:
                self.printer.on_message_complete(character)

    


if __name__ == "__main__":
    printer = Printer()
    decoder = Decoder(printer)

    samples = [
        (1, '-'),
        (2, 'h'),
        (3, 'e'),
        (4, 'l'),
        (5, 'l'),
        (6, 'o'),
        (7, '-'),
        (8, 'b'),
        (9, 'y'),
        (10, 'e'),
        (11, '-')
    ]

    for sample in samples:
        decoder.process_sample(*sample)
