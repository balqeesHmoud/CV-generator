TEMPLATE_PATH = 'assets/cv_template.txt'
OUTPUT_PATH = 'cv_output.txt'

def read_template(template_path):
    template_path = 'assets/cv_template.txt'
    try:
        with open(template_path, 'r') as file:
            template_content = file.read()
        return template_content.strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Template file not found at: {template_path}")

def parse_template(template):
    import re
    pattern = r'\{([^\{\}]+)\}'
    language_parts = re.findall(pattern, template)
    stripped_template = re.sub(pattern, '{}', template)
    return stripped_template, tuple(language_parts)

def merge(template, language_parts):
    filled_cv = template.format(*language_parts)
    return filled_cv

def main():
    # Read template file
    template = read_template(TEMPLATE_PATH)
    
    # Parse template to extract language parts
    stripped_template, language_parts = parse_template(template)
    
    # Prompt user for input
    print("Welcome to the CV Generator!")
    print("Please provide the following information:")
    
    user_inputs = []
    for part in language_parts:
        user_input = input(f"Enter {part.replace('_', ' ').title()}: ")
        user_inputs.append(user_input)
    
    # Merge user inputs into the template
    filled_cv = merge(stripped_template, user_inputs)
    
    # Display completed CV
    print("\nCompleted CV:")
    print(filled_cv)
    
    # Write completed CV to output file
    with open(OUTPUT_PATH, 'w') as output_file:
        output_file.write(filled_cv)
        print(f"\nCV successfully saved to: {OUTPUT_PATH}")

# Run the main function
if __name__ == "__main__":
    main()
