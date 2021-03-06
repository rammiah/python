file_name = 'alice.txt'

try:
    with open(file_name, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("THe file " + file_name + " has about " + str(num_words) + " words.")
    print(str(len(set(words))) + " different words.")
    words = contents.lower().split()
    print(str(len(set(words))) + " different words.")
    