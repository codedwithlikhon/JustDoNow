import os

def read_and_print(file_path):
    """Reads and prints the content of a file if it exists."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            print(f"--- Content of {file_path} ---")
            print(content)
            print("-" * (len(file_path) + 16))
    else:
        print(f"--- File not found: {file_path} ---")

def main():
    """Main function for the chatbot runner."""
    print(">>> Chatbot model runner started!")
    print(">>> Reading context files...")

    read_and_print("/app/agent.md")
    read_and_print("/app/instructions.md")
    read_and_print("/app/structure.md")

    print(">>> All context files processed.")
    print(">>> Chatbot model runner finished.")

if __name__ == "__main__":
    main()
