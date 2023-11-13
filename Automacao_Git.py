import os
import subprocess
from datetime import datetime

# Lista dos diretórios dos seus projetos
diretorios = ["C:/Dev/React/dashboard-cia", "C:/Dev/Python/projetos_de_api"]

# Loop através dos diretórios
for diretorio in diretorios:
    # Navegue até o diretório do projeto
    os.chdir(diretorio)

    subprocess.run(["git", "pull"])
    # Adicione todas as alterações ao índice
    subprocess.run(["git", "add", "."])

    # Faça commit das alterações com a data e hora atual
    commit_message = f"Atualização: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_message])

    # Suba as alterações para o repositório remoto
    subprocess.run(["git", "push"])
