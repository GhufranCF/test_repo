print('this is a newly added python file - Also changed this line as its old')
print('added this new feature')

def custom_print(*args):

    for i, arg in enumerate(args, start=1):
        print(f"{i}) {arg} ")


custom_print("hello", "second")