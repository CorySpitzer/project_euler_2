from pe2_library import FibonacciSequence, find_sum

def main():
    print('Functionally - ' + str(find_sum()))
    print('Objectively  - ' + str(FibonacciSequence().even_sum()) )

# only execute main() if the script is being run directly, but not imported;
# __name__ is set to '__main__' only if we run 'python pe1.py',
# but not with 'import pe1'
# (see stackoverflow.com/questions/419163/what-does-if-name-main-do for details)
if __name__ == "__main__":
    main()
