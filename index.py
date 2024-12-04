def main():
    # Prompt user for filename
    input_file = input("Enter the filename to read: ")

    try:
        # Try reading the file
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        output_file = f"modified_{input_file}"
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content successfully written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()




   