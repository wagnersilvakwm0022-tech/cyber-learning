#!/bin/bash

# Script automatizado de varredura com Nmap
# Uso: ./scanner.sh <IP_ALVO>

# Verifica se o alvo foi passado como argumento
if [ -z "$1" ]; then
    echo "[-] Erro: Você precisa especificar um IP ou domínio alvo."
    echo "Exemplo: ./scanner.sh 192.168.1.1"
    exit 1
fi

ALVO=$1
ARQUIVO_SAIDA="resultado_nmap_$(date +%Y%m%d_%H%M%S).txt"

echo "[+] Iniciando varredura automatizada no alvo: $ALVO"
echo "[+] Os resultados serão salvos em: $ARQUIVO_SAIDA"
echo "--------------------------------------------------"

# Executa o Nmap:
# -sV: Detecta versões de serviços
# -sC: Executa scripts padrão de vulnerabilidade
# -oN: Salva a saída em formato de texto normal
nmap -sV -sC "$ALVO" -oN "$ARQUIVO_SAIDA"

echo "--------------------------------------------------"
echo "[+] Varredura concluída com sucesso!"
