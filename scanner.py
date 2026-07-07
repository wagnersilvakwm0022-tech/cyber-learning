import sys
import subprocess
from datetime import datetime

def executar_varredura():
    # Verifica se o argumento do IP alvo foi fornecido
    if len(sys.argv) < 2:
        print("[-] Erro: Você precisa especificar um IP ou domínio alvo.")
        print("Exemplo: python scanner.py 192.168.1.1")
        sys.exit(1)

    alvo = sys.argv[1]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    arquivo_saida = f"resultado_nmap_{timestamp}.txt"

    print(f"[+] Iniciando varredura em: {alvo}")
    print(f"[+] Salvando relatório em: {arquivo_saida}")
    print("-" * 50)

    # Comando Nmap simplificado para rodar direto pelo Python
    comando = ["nmap", "-sV", "-F", alvo]

    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        
        with open(arquivo_saida, "w") as arquivo:
            arquivo.write(resultado.stdout)
            
        print("[+] Varredura concluída com sucesso!")
        
    except subprocess.CalledProcessError as e:
        print(f"[-] Erro ao executar o Nmap: {e}")
    except FileNotFoundError:
        print("[-] Erro: Nmap não está instalado ou não foi encontrado no sistema.")

if __name__ == "__main__":
    executar_varredura()
