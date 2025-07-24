print('this is a newly added python file - Also changed this line as its old')
print('added this new feature')

def custom_print(*args):
    for arg in args:
        print("* ", arg)


custom_print("hello", "second")