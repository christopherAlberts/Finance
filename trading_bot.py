
def config_handler(start_text, end_text, config_file):

    # The following code is designed to import text from a config file.
    # It's designed to do this line by line.
    # start_text: The program will start importing after this point.
    # end_text: The program will stop importing when it reaches this point.
    # config_file: location where config file is stored.

    fr = open(config_file, 'r')
    text = fr.read()
    start = text.find(start_text) + len(start_text + "\n")
    end = text.find("\n" + end_text)
    substring = text[start:end]
    fr.close()

    return substring

def luno_bot(sell_or_buy, amount):

    pass