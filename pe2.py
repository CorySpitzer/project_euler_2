from pe2_library import FibonacciSequence

def main():
    # print('main called')
    # print('Functionally we get: ' + str(find_sum()))
    print('Objectively we get: ' + str(FibonacciSequence().even_sum()) )

# only execute main() if the script is being run directly, but not imported;
# __name__ is set to '__main__' only if we run 'python pe1.py',
# but not with 'import pe1'
# (see stackoverflow.com/questions/419163/what-does-if-name-main-do for details)
if __name__ == "__main__":
    main()
