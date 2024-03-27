class SearchTool:
    def __init__(self):
        print()

    def build(self):
        pass

    def load(self):
        pass

    def print(self):
        pass

    def find(self):
        pass


def main():
    # Create new SearchTool instance
    searchTool = SearchTool()

    # Print welcome message
    print("\n\033[1;34mWelcome to the quotes search tool!\033[0m")
    print("Type 'help' for a list of commands or 'exit' to close the search tool.")

    # Loop infinitely to accept user input & run commands until exit command is given
    while True:
        # Wait for user to input command & arguments
        input_parts = input("> ").split(" ")
        command = input_parts[0]
        args = input_parts[1:]

        # Run appropriate search tool method based on command
        if command == "exit":
            break
        elif command == "build":
            searchTool.build()
        elif command == "load":
            searchTool.load()
        elif command == "print":
            searchTool.print()
        elif command == "find":
            searchTool.find()
        elif command == "help":
            print("\n\033[1;34mAvailable commands:\033[0m\n"
                  "build - Crawls the quotes website, builds the index, and saves it to the local filesystem.\n"
                  "load - Loads the index from the local filesystem (requires that the index has already been built).\n"
                  "print <target_word> - Prints the inverted index for the target word.\n"
                  "find <target_word>... - Finds the target word(s) in the inverted index and returns a list of all "
                  "pages containing the phrase these words form.\n"
                  "exit - Exits the search tool\n")
        else:
            print("\033[1;31mError: Invalid command - type 'help' for available commandsd\033[0m")


if __name__ == '__main__':
    main()