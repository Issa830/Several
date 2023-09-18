import os

def delete_hidden_directories(path):
    try:
        for root, dirs, files in os.walk(path, topdown=False):
            for dir_name in dirs:
                if dir_name.startswith('.'):
                    hidden_dir_path = os.path.join(root, dir_name)
                    print(f"Deleting hidden directory: {hidden_dir_path}")
                    os.rmdir(hidden_dir_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_path = "/path/to/your/target/directory"
    delete_hidden_directories(target_path)
