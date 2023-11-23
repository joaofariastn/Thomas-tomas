import os

class FileExplorer:
    def __init__(self):
        self.current_path = os.getcwd()

    def pwd(self):
        return self.current_path

    def ls(self):
        files = os.listdir(self.current_path)
        return files

    def cd(self, new_path):
        new_dir = os.path.join(self.current_path, new_path)
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_path = new_dir
            return f"Directory changed to {new_path}"
        else:
            return f"Directory '{new_path}' not found"

    def mkdir(self, folder_name):
        new_folder_path = os.path.join(self.current_path, folder_name)
        try:
            os.mkdir(new_folder_path)
            return f"Folder '{folder_name}' created"
        except FileExistsError:
            return f"Folder '{folder_name}' already exists"

    def rm(self, folder_name):
        folder_path = os.path.join(self.current_path, folder_name)
        if os.path.exists(folder_path):
            try:
                os.rmdir(folder_path)
                return f"Folder '{folder_name}' removed"
            except OSError:
                return f"Failed to remove folder '{folder_name}'"
        else:
            return f"Folder '{folder_name}' not found"

# Exemplo de uso:
file_explorer = FileExplorer()
print(file_explorer.pwd())  # Mostra o caminho atual

print(file_explorer.ls())  # Mostra os arquivos e pastas no diretório atual

print(file_explorer.mkdir("Nova_Pasta"))  # Cria uma nova pasta

print(file_explorer.cd("Nova_Pasta"))  # Muda para a nova pasta criada

print(file_explorer.pwd())  # Mostra o novo caminho atual

print(file_explorer.ls())  # Mostra os arquivos e pastas no diretório atual

print(file_explorer.rm("Nova_Pasta"))  # Remove a pasta criada anteriormente