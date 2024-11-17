import os 


def load_repo_names(input_file):
    """
    load names of repository from a file.
    
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file '{input_file}' not exist.")
    
    with open(input_file, 'r') as file:
        return [line.strip() for line in file if line.strip()]  



    