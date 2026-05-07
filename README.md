# 🛡️ Jornada Cibersegurança - Dia 1

## 🎯 Objetivo: Atuar na área até os 21 anos.

### 🛠️ O que aprendi hoje:
- **Fundamentos de Redes:** O que é um endereço IP, Octetos e a diferença entre Network ID e Host ID.
- **Linux:** Como ativar o ambiente Linux no Chromebook e comandos básicos de terminal.
- **Ferramentas:** Instalação e primeiro uso do `nmap` para escaneamento de rede.


### 💻 Comandos Praticados:
- `sudo apt update` (Atualização do sistema)
- `ping -c 4 8.8.8.8` (Teste de conectividade)
- `nmap scanme.nmap.org` (Primeiro scan ético)
- `sudo nmap -O`(Concluí o reconhecimento de Sistema Operacional (OS Detection) usando privilégios de superusuário (Sudo). Identifiquei que o alvo scanme.nmap.org utiliza o sistema Linux.)
- ![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/foto%202.png).
- `ping -c 4 127.0.0.1(Localhost)
- ![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/capture.png)
*Foco: 5 horas diárias de estudo intenso.*


# 🛡️ Jornada Cibersegurança - Dia 2

## 🎯 Objetivo: Atuar na área até os 21 anos.

### 🛠️ O que aprendi hoje:
**Escaneamento de Serviços Avançado:**
Uso do comando nmap -sV para identificar não apenas portas abertas, mas as versões exatas dos serviços (ex: Apache, OpenSSH).
Uso da flag -Pn para escanear alvos que bloqueiam pacotes de Ping (ICMP).
Entendimento da importância de descobrir versões de software para a busca de vulnerabilidades específicas (Exploits).

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/scan-nmap-dia2.png)

**Hierarquia de Segurança (Blue Team & Red Team):**
SOC L1 Analyst: Responsável pela triagem inicial (triage) de alertas.
SOC L2 Analyst: Responsável pela análise profunda (deep analysis) de incidentes.
Penetration Tester (Pentester): O "Hacker Ético" que busca vulnerabilidades de forma proativa.
Security Engineer: Responsável pela manutenção e configuração das ferramentas de defesa (SIEM, Firewalls).
CERT Lead: Liderança em casos de incidentes críticos e resposta a crises (Ransomware).
Threat Intel Analyst: Analista que estuda as táticas e comportamentos de grupos cibercriminosos específicos.

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/download.jpeg)

**Inglês Técnico:**
Expansão de vocabulário específico da área para resolução de desafios em plataformas internacionais (TryHackMe).

💻 **Comandos Praticados:**
nmap -sV -Pn scanme.nmap.org
ping 127.0.0.1 (Teste de Localhost/Loopback)

Foco mantido: 5 horas de estudo concluídas. Amanhã: Protocolos de Transporte (TCP/UDP) e o Three-way Handshake."


## Dia 3: Protocolos de Transporte e Handshake

### 🧠 Teoria de Redes
- **TCP (Transmission Control Protocol):** Focado em confiabilidade. Realiza o "Three-Way Handshake" (SYN, SYN-ACK, ACK). Ideal para transferências de dados sensíveis como HTTPS e SSH.
- **UDP (User Datagram Protocol):** Focado em velocidade. Não orientado à conexão. Utilizado para ataques de volume e serviços em tempo real (Streaming/VOIP).

### 💻 Prática no Terminal
- Realizei um **Ping Sweep** na rede local utilizando `nmap -sn`.
- Identifiquei `X` dispositivos ativos na rede.
- Pratiquei o comando `nmap -sT` para forçar a conclusão do Handshake TCP.

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/Screenshot%202026-04-21%2011.32.42.png)

### 🇺🇸 Inglês Técnico do Dia
- **Handshake:** Conexão/Aperto de mão.
- **Reliable:** Confiável.
- **Connectionless:** Sem conexão (UDP).
- **Latency:** Latência (atraso na resposta).


## pra fechar com chave de ouro
- **porta aberta:** usei a porta 80.
- **porta fechada:** usei a porta 1234.

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/foto%203.png)

*Foco: meu desejo por aprender mais não para,quero passar o dia todo aprendendo mais sobre o meu terminal.*

# 🛡️ Jornada Cibersegurança - Dia 4: O Sistema Nervoso da Internet

## 🎯 Objetivo: Especialista em Segurança (SOC/Pentest)

Neste quarto dia, foquei em como a internet gerencia nomes e endereços, e como investigar a identidade de um domínio.

### 🌐 DNS (Domain Name System) & DHCP
- **DNS:** Entendi que o DNS é o "tradutor" que converte nomes de domínio (google.com) em endereços IP.
- **NXDOMAIN:** Aprendi que este erro (Non-Existent Domain) indica que o domínio pesquisado não existe nos registros mundiais.
- **DHCP:** Compreendi como o roteador entrega endereços IP de forma dinâmica para os dispositivos da rede local.

### 🛠️ Comandos Praticados (Terminal)
- `nslookup google.com`: Consulta simples de resolução de nome.
- `dig google.com`: Ferramenta avançada para verificar registros de DNS e tempos de resposta (**Query Time**).
![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/Screenshot%202026-04-22%2023.11.00.png)
- `whois google.com`: Investigação de propriedade de domínio, data de criação e expiração.
![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/Screenshot%202026-04-22%2023.17.42.png)
### 📊 Descobertas Técnicas
- **Data de Criação do Google:** Identificada via `whois` como 15/09/1997.
- **Status da Rede:** Pratiquei a identificação de domínios derrubados ou inexistentes através do status **NXDOMAIN**.

### 🇺🇸 Inglês Técnico (Tech Vocabulary)
- **Query:** Consulta / Pergunta ao servidor.
- **Resolution:** Resolução (processo de transformar nome em IP).
- **Registrar:** Empresa responsável pelo registro do domínio.
- **Expiry Date:** Data de validade/expiração do contrato do domínio.
- **Lease:** Tempo de "aluguel" de um IP entregue pelo DHCP.

---
*Status: 5 horas de estudo concluídas. Amanhã: Camada 7 - Protocolos Web (HTTP/HTTPS).*


# 🛡️ Jornada Cibersegurança - Dia 5: Camada de Aplicação (Web)

## 🎯 Objetivo: Especialista em Segurança (SOC/Pentest)

Neste quinto dia, subi para a Camada 7 do Modelo OSI para entender como os dados trafegam na Web e como os servidores se comunicam com os navegadores.

### 🌐 Protocolos Web (HTTP vs HTTPS)
- **HTTP (Porta 80):** Protocolo de transferência de texto puro. Inseguro, pois os dados viajam sem criptografia.
- **HTTPS (Porta 443):** Versão segura do HTTP que utiliza SSL/TLS para criptografar a comunicação, protegendo dados sensíveis.

### 📑 Verbos e Status Codes HTTP
Aprendi a interpretar as respostas dos servidores através dos códigos de status:
- **200 OK:** A requisição foi bem-sucedida.
- **301 Moved Permanently:** O recurso mudou de endereço (Redirecionamento).
- **403 Forbidden:** O servidor entendeu o pedido, mas se recusa a autorizar o acesso (Falta de permissão).
- **404 Not Found:** O recurso solicitado não foi encontrado no servidor.

### 🛠️ Comandos Praticados (Terminal)
- `curl -I https://google.com`: Utilizado para ler apenas o cabeçalho (Header) da resposta do servidor.
![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/Screenshot%202026-04-23%2008.46.49.png)
- `curl -I -L https://google.com`: Segue automaticamente os redirecionamentos (como o erro 301) até chegar ao destino final (200).
![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/pdf.png)

### 🇺🇸 Inglês Técnico (Tech Vocabulary)
- **Request:** Requisição (o pedido feito pelo cliente).
- **Response:** Resposta (o retorno enviado pelo servidor).
- **Header:** Cabeçalho (metadados da conexão).
- **Redirect:** Redirecionamento.
- **Forbidden:** Proibido/Negado.

#### Hoje também aprendi a analisar o arquivo robots.txt, técnica utilizada no reconhecimento de aplicações web para identificar diretórios ocultos ou sensíveis.
![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/Screenshot%202026-04-23%2009.16.05.png)

---
*Status: 5 horas de estudo concluídas. Amanhã: Dia 6 - Finalizando os fundamentos de Rede (Portas e Protocolos).*


# 🛡️ Jornada Cibersegurança - Dia 6: Portas e Hardening

## 🎯 Objetivo: Especialista em Segurança (SOC/Pentest)

Neste sexto dia, foquei em entender o "Dicionário de Portas" e como a configuração correta de um servidor (Hardening) pode prevenir invasões.

### 🚪 Portas de Gerenciamento e Riscos
- **Porta 21 (FTP) & 23 (Telnet):** Protocolos inseguros que trafegam dados em **Plaintext**. Identifiquei que são alvos fáceis para interceptação.
- **Porta 22 (SSH):** O padrão ouro para acesso remoto. Utiliza criptografia para proteger comandos e transferências de arquivos (SFTP).
- **Porta 445 (SMB):** Frequentemente explorada por Ransomwares para movimentação lateral em redes Windows.

- # Entendi a vulnerabilidade crítica da Porta 23 (Telnet). Por não utilizar criptografia, todas as credenciais trafegam em Plaintext, permitindo ataques de interceptação. Em contraste, a Porta 22 (SSH) é o padrão de mercado por garantir a confidencialidade dos dados."

### 🛠️ Comandos Praticados (Terminal)
- `sudo nmap -p 21,22,23,445 scanme.nmap.org`: Scan focado em portas de gerenciamento.
- `sudo nmap -sV -p 22 scanme.nmap.org`: Técnica de **Banner Grabbing** para identificar a versão do serviço SSH.
- `sudo apt install netcat-openbsd -y`: (Instalação da ferramenta de conexão direta).

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/Screenshot%202026-04-24%2013.12.17.png)

### 📊 Conclusões Técnicas
- Servidores bem configurados, como o `scanme.nmap.org`, mantêm portas inseguras (21, 23) **fechadas**.
- A segurança proativa exige a desativação de serviços desnecessários para reduzir a superfície de ataque.

### 🇺🇸 Inglês Técnico (Tech Vocabulary)
- **Banner Grabbing:** Coleta de informações sobre a versão de um serviço.
- **Hardening:** Processo de reforçar a segurança de um sistema.
- **Plaintext:** Texto puro, sem criptografia.
- **Inbound/Outbound:** Tráfego de entrada e saída.

---
*Status: 5 horas de estudo concluídas. Próxima meta: Dia 7 - Introdução ao Windows Security e Active Directory.*

# 🛡️ Jornada Cibersegurança - Dia 7: Active Directory e Infraestrutura Windows

### 🏛️ O Coração da Rede Corporativa
- **Active Directory (AD):** Serviço de diretório da Microsoft utilizado para gerenciar identidades e acessos em redes empresariais.
- **Domain Controller (DC):** Servidor responsável por autenticar usuários e aplicar políticas de segurança (GPOs).

### 🔑 Gestão de Privilégios
- Entendi a diferença entre um usuário comum e um **Domain Admin**.
- Estudei o conceito de **Privilege Escalation** (objetivo principal de um ataque em redes AD).
  
### 🛠️ Ferramentas de Enumeração
- **Enum4linux:** Utilizada para extrair informações de sistemas Windows/Samba.
- **SMBClient:** Ferramenta para interagir com compartilhamentos de rede (Porta 445).
![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/PP..png)
![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/PeP.png)
### 🇺🇸 Vocabulário Corporativo
- **Lateral Movement:** Técnica de saltar entre máquinas na rede.
- **Policy:** Regra de segurança aplicada centralizadamente.
- **Share:** Pasta compartilhada na rede.

# 🛡️ Jornada Cibersegurança - Dia 8: Hashes e Quebra de Senhas (Cracking)

## 🎯 Objetivo: Especialista em Segurança (SOC/Pentest)

Neste oitavo dia, mergulhei na ciência da criptografia de senhas, entendendo como os sistemas protegem credenciais e como hackers tentam revertê-las.

### 🧠 O que são Hashes?
- **Definição:** Um hash é um "resumo matemático" de uma senha. Sistemas modernos não guardam senhas em texto puro (plaintext), mas sim em códigos únicos (MD5, SHA-256, NTLM).
- **Via de Mão Única:** Aprendi que é impossível transformar um hash de volta em senha original sem usar métodos de comparação (Cracking).

### 🛠️ Desafios Técnicos e Ferramentas
- **John the Ripper:** Instalei e configurei esta ferramenta lendária para quebra de hashes.
- **Resolução de Erros:** Superei limitações do ambiente Linux do Chromebook (erros de montagem do `snapd`) instalando a ferramenta via repositórios nativos e compilando dependências.
- **Benchmark:** Realizei o comando `john --test` para medir a capacidade de processamento do sistema em diferentes algoritmos.
  ![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/ka1.51%20PM.png)

### ⚔️ Métodos de Ataque
- **Brute Force:** Tentativa de todas as combinações possíveis (lento).
- **Dictionary Attack:** Uso de **Wordlists** (listas de senhas reais vazadas) para acelerar a descoberta de credenciais.

### 🇺🇸 Inglês Técnico (Tech Vocabulary)
- **Hash Cracking:** O ato de quebrar um hash.
- **Wordlist:** Dicionário de senhas.
- **Plaintext:** Senha em texto puro, sem proteção.
- **Benchmark:** Teste de performance da ferramenta.
- **Salt:** Código aleatório adicionado ao hash para aumentar a segurança.

---
*Status: 5 horas de estudo concluídas sob cansaço, mas com sucesso. Amanhã: Dia 9 - Praticando ataques de dicionário com Wordlists reais.*


# 🛡️ Jornada Cibersegurança - Dia 9: Wordlists e Início em Python

## 🎯 Objetivo: Automação e Quebra de Senhas

Neste nono dia, comecei a explorar como as ferramentas de ataque utilizam "munição" (Wordlists) e como a programação pode acelerar o trabalho de um analista.

### 📚 Wordlists (Dicionários de Senhas)
- **O que são:** Listas contendo milhões de senhas reais que vazaram em ataques históricos.
- **Localização Técnica:** Identifiquei a wordlist padrão do John em `/usr/share/john/password.lst` (26 KB).
- **RockYou.txt:** Aprendi sobre a wordlist mais famosa do mundo (130 MB / 14 milhões de senhas), essencial para ataques de dicionário eficazes.

### 🐍 Primeiro contato com Python
- Iniciei o aprendizado da linguagem Python, focando em automação para segurança.
- **Prática:** Criei meu primeiro script básico para manipulação de variáveis e cálculos simples no interpretador `python3`.
- **Lógica:** Entendi que o Python é a ferramenta que me permitirá analisar grandes volumes de dados (como as wordlists de 130 MB) em segundos.

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/ay8%20PM.png)

### 🇺🇸 Inglês Técnico (Vocabulary)
- **Script:** Conjunto de instruções para o computador.
- **Wordlist:** Lista de palavras/senhas.
- **Run / Execute:** Rodar ou executar um programa.
- **Dictionary Attack:** Ataque que utiliza listas pré-definidas.

---
*Status: 5 horas de estudo concluídas. Amanhã: Dia 10 - Entendendo Criptografia e Diferença entre Encode e Encrypt.*


# 🛡️ Jornada Cibersegurança - DIA 10: Encoding vs Encryption

### 🧠 O Grande Diferencial
Hoje aprendi a não confundir **Codificação** com **Criptografia**. 
- **Encoding (Base64):** Usado para compatibilidade de dados. Não protege a informação (não exige senha).
- **Encryption:** Usado para confidencialidade. Exige uma chave para ser lido.

### 💻 Prática no Terminal e Python
- Usei o comando `base64` e `base64 -d` para codificar e decodificar mensagens.
- Desenvolvi um script simples em **Python** utilizando a biblioteca `base64` para automatizar o processo.

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/7%20PM.png)

### 🇺🇸 Inglês Técnico
- **Encoding / Decoding:** Codificar / Decodificar.
- **Ciphertext:** O texto secreto gerado por criptografia.
- **Plaintext:** O texto original, legível.


# 🛡️ Jornada Cibersegurança - Dia 11: Firewalls e Defesa de Perímetro

## 🎯 Objetivo: Entender a Barreira entre o Atacante e o Alvo

Neste décimo primeiro dia, foquei em como as organizações protegem seus recursos internos através de Firewalls e como identificar essas proteções durante um reconhecimento.

### 🧱 O que é um Firewall?
- **Definição:** Uma barreira de segurança que monitora e controla o tráfego de rede de entrada (**Inbound**) e saída (**Outbound**) com base em regras de segurança predefinidas.
- **Estado "Filtered" no Nmap:** Aprendi que quando uma porta aparece como filtrada, significa que um Firewall está descartando os pacotes e impedindo que o Nmap saiba se a porta está aberta ou fechada.

### 🛠️ Técnicas de Reconhecimento e Evasão
- **ACK Scan (`nmap -sA`):** Utilizado para mapear regras de firewall e determinar se as portas estão sendo filtradas ou não.
- **Fragmentação (`nmap -f`):** Estudei o conceito de quebrar pacotes em pedaços menores para tentar burlar a inspeção de firewalls mais simples.
- **Bypass:** O ato de contornar ou encontrar uma brecha em uma regra de segurança.

### 🐍 Lógica de Defesa com Python
- Desenvolvi um script simples de **Blacklist** (Lista Negra) para entender a lógica de decisão de um firewall ao permitir ou negar um endereço IP.

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/Screenshot%202026-04-29%2012.51.40%20PM.png)

### 🇺🇸 Inglês Técnico (Tech Vocabulary)
- **Rule:** Regra (A instrução que permite ou bloqueia o tráfego).
- **Inbound / Outbound:** Tráfego de entrada e de saída.
- **Filtered:** Quando a porta está protegida por um firewall.
- **Bypass:** Contornar/Burlar uma proteção.
- **Blacklist / Whitelist:** Lista de bloqueio e lista de permissão.

---
*Status: 5 horas de estudo concluídas. Amanhã: Dia 12 - Introdução ao Wireshark e Análise de Tráfego de Rede.*

# 🛡️ Jornada Cibersegurança - Dia 12: Análise de Tráfego e Sniffing

## 🎯 Objetivo: Aprender a interceptar e analisar dados na rede

Neste décimo segundo dia, deixei de apenas enviar comandos e passei a "ouvir" a comunicação da rede. Aprendi a utilizar ferramentas de captura de pacotes para perícia e análise de segurança.

### 🕵️ O que é Packet Sniffing?
- **Definição:** É a técnica de interceptar pacotes de dados que viajam pela rede. 
- **Utilidade:** Essencial para analistas de SOC identificarem invasões, vazamentos de dados ou diagnósticos de rede.
- **Protocolos Inseguros:** Ficou claro como protocolos como HTTP e FTP são perigosos, pois permitem que um "sniffer" leia os dados em texto puro.

### 🛠️ Comandos Praticados (Terminal)
- `sudo apt install tcpdump -y`: Instalação do analisador de tráfego via linha de comando.
- `sudo tcpdump -i any -c 20`: Captura global de 20 pacotes para análise inicial.
- `sudo tcpdump -i any tcp -c 10`: Filtro específico para capturar apenas tráfego TCP.
- `sudo tcpdump -A`: Visualização dos pacotes em formato ASCII (texto legível).

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/pod12%20PM.png)

### 📊 Observações Técnicas
- Durante os testes, identifiquei uma alta predominância de pacotes **UDP**. 
- **Conclusão:** Isso reflete o tráfego de serviços de streaming e consultas de DNS que ocorrem em segundo plano no sistema.

### 🇺🇸 Inglês Técnico (Tech Vocabulary)
- **Capture:** Capturar.
- **Traffic:** Tráfego de rede.
- **Sniffer:** Farejador/Interceptador de pacotes.
- **Payload:** A carga útil (dados reais) dentro de um pacote.
- **Interface:** A placa de rede por onde os dados passam.

---
*Status: 5 horas de estudo concluídas. Amanhã: Dia 13 - Vulnerabilidades de Software e o conceito de Exploit.*

# 🛡️ Jornada Cibersegurança - Dia 13: Análise de Protocolos e Vulnerabilidades Web

## 🎯 Objetivo: Mergulho Profundo (Deep Dive) em Tráfego e Falhas Lógicas

Neste décimo terceiro dia, dediquei um tempo estendido para entender como os pacotes se comportam na rede e como falhas simples de lógica podem comprometer sistemas inteiros.

### 🔍 Análise de Tráfego Avançada (TCPDump)
- **Filtros de Captura:** Aprendi a filtrar tráfego específico no terminal para evitar o "ruído" de dados desnecessários.
- **Protocolos ICMP e ARP:** Estudei como o protocolo de mensagens (Ping) e o protocolo de resolução de endereços (ARP) operam. 
- **ARP Spoofing:** Compreendi o conceito de "envenenamento" de ARP, onde um atacante intercepta o tráfego entre o computador e o roteador.

### 🌐 Vulnerabilidades Web (OWASP Top 10)
- **IDOR (Insecure Direct Object Reference):** Estudei esta falha de controle de acesso onde a alteração de um parâmetro (como um ID na URL) permite acessar dados de outros usuários. 
- **Impacto:** Entendi que falhas lógicas são tão perigosas quanto falhas técnicas, pois muitas vezes não são detectadas por firewalls automáticos.

### 🐍 Automação com Python
- **Socket Programming:** Desenvolvi a lógica inicial de um **Port Scanner** em Python, utilizando a biblioteca `socket` para testar conexões em portas específicas.
- **Diferencial:** Entendi que criar minhas próprias ferramentas me dá mais flexibilidade do que apenas usar softwares prontos.

### 🇺🇸 Inglês Técnico e Teoria
- **Query / Response:** O fluxo de pergunta e resposta dos protocolos.
- **IDOR:** Referência direta a objeto insegura.
- **Spoofing:** Falsificação de identidade/endereço.
- **Linear Algebra:** Iniciei estudos em álgebra linear, fundamental para o entendimento de algoritmos de segurança.

---
*Status: 10 horas de imersão concluídas. Amanhã: Dia 14 - Explorando Metasploit e Frameworks de Exploração.*

# 🛡️ Jornada Cibersegurança - Dia 14: Frameworks de Exploração (Metasploit)

## 🎯 Objetivo: Entender a Lógica de Exploração e Pós-Invasão

Neste décimo quarto dia, foquei na anatomia de um ataque cibernético e nas ferramentas utilizadas por Pentesters profissionais para ganhar acesso a sistemas.

### 🧠 Vulnerabilidade vs Exploit vs Payload
- **Vulnerabilidade:** A falha técnica no sistema alvo.
- **Exploit:** O meio/código utilizado para aproveitar a falha.
- **Payload:** O software malicioso que executa ações após a invasão. Ex: **Meterpreter**.

### ⚡ O Poder do Meterpreter
- Entendi que o Meterpreter é um payload avançado que reside na memória RAM, permitindo ações como:
  - Captura de tela (`screenshot`).
  - Extração de hashes de senhas (`hashdump`).
  - Pivotagem (usar o PC invadido para atacar outros na mesma rede).

### 🛠️ Troubleshooting de Rede
- Enfrentei problemas de resolução de DNS no ambiente Linux do Chromebook ao tentar baixar o framework.
- "Durante a instalação do Metasploit, enfrentei um erro de DNS Resolution (Could not resolve host). Utilizei técnicas de troubleshooting de rede para verificar a conectividade e entendi que, no Pentest, a infraestrutura do atacante deve estar tão sólida quanto o conhecimento técnico.
- Pratiquei comandos de diagnóstico como `ping` e edição do arquivo `/etc/resolv.conf`. No Pentest, saber lidar com falhas na própria infraestrutura é vital.

### 🇺🇸 Vocabulário de Exploração
- **Reverse Shell:** Quando o alvo se conecta ao atacante para burlar o firewall.
- **LHOST / RHOST:** Local Host (Atacante) e Remote Host (Alvo).
- **PoC (Proof of Concept):** Demonstração de que uma vulnerabilidade é real.

---
*Status: 5 horas de estudo concluídas. Amanhã: Dia 15 - Consolidando as duas primeiras semanas.*

# 🛡️ DIA 15: Marco da Primeira Quinzena - Consolidação de Elite

Duas semanas atrás, eu era um iniciante. Hoje, sou um estudante de cibersegurança com base técnica real.

### 🧠 Resumo do Conhecimento Blindado:
- **Redes:** Domínio de TCP/IP, portas críticas e diagnóstico de DNS.
- **Sistemas:** Administração Linux (Crostini) e manipulação de arquivos.
- **Segurança Corporativa:** Noções de Active Directory e Privilégios Windows.
- **Exploração:** Lógica de Reverse Shell, Metasploit e Netcat.
- **Programação:** Scripts básicos em Python para automação de segurança.

### 🚀 O Plano de Guerra:
- Faltam poucos dias para o investimento no TryHackMe Premium.
- O foco continua sendo o mercado americano aos 21 anos.

### 🧠 Resumo:
- **Three-Way Handshake"** do TCP: É o processo de aperto de mão que um servidor tem
antes de estabelecer os dados para que qualquer dado seja enviado.

- **Diferença entre os códigos 200, 301, 403 e 404**: As diferenças são (código de status 200) - acesso
autorizado sem nenhuma restrição ou permissão para acessar.(código de status 301) - O acesso 
mudou de posição para sempre, ele direciona uma nova URL mandando o navegador ir para lá.(código de status 403) - O servidor entendeu o que você quer mais ele se recusa dar, é um sinal que tem algo valioso aqui e se eu acessar terei uma recompensa, dá para acessar usando técnicas de 403 bypass para tentar pular a proteção.(código de status 404) - O servidor não conseguiu localizar nada no endereço solicitado, as veses é usado para despistar hackers que tentam invadir e no lugar de 403 põe 404.

- **O que é o Domain Controller**: é onde todo hacker quer chegar para poder ter o acesso de Enterprise Admin.

- **Lateral Movement**: não dá para chegar e pegar direto o chefão,precisa começar de onde menos as pessoas esperam um exemplo disso é começar pelo acesso de alguém da administração até chegar no (DC).


---
*Status: 15/1000 dias concluídos. A BMW e a casa da minha mãe são o combustível.*

**Ontem dia 15 tive bastante dificuldade para estuadar,a IA do google que estava me auxiliando ficou bastante pesado
com a primeira quinzena,estou tentando dar um jeito,o dia 16 será realizado e também todos os demais 984 dias.Espero consertar isso até o dia de amanhã.**

# 🛡️ Dia 16: Google Dorking e Reconhecimento Passivo

Hoje aprendi que o Google indexa muito mais do que sites públicos; ele pode expor falhas críticas se soubermos "perguntar" corretamente.

### 🔍 Operadores de Busca Avançada:
- **site:** Limita a busca a um domínio específico.
- **filetype:** Busca extensões específicas que podem conter dados sensíveis (LOG, ENV, SQL).
- **intitle / inurl:** Localiza termos em títulos de páginas e endereços de sites, como painéis de login.

### 🧠 Conceitos de Segurança:
- **Passive Reconnaissance:** Coleta de informações sem interagir diretamente com o servidor do alvo.
- **Google Hacking Database (GHDB):** Estudei como utilizar queries prontas para identificar vulnerabilidades expostas globalmente.

### 🇺🇸 Inglês Técnico:
- **Dork:** Uma busca avançada customizada.
- **Data Leakage:** Vazamento de informações.

_Pratiquei buscas avançadas no navegador para entender como o Google indexa dados sensíveis_
---

*Status: 5 horas de estudos consluidas.Amanhã dia 17 ó foco será **Active Reconnaissance** (Reconhecimento Ativo). Vou aprender a usar ferramentas para "chutar" nomes de pastas e arquivos escondidos que o Google não conseguiu indexar.*

# 🛡️ Dia 17: Web Fuzzing e Enumeração de Diretórios

Hoje avancei do reconhecimento passivo para o **Active Reconnaissance** (Reconhecimento Ativo), utilizando ferramentas para descobrir arquivos e pastas ocultas em servidores web.

### 🔍 O que é Web Fuzzing?
- **Conceito:** Técnica de "força bruta" aplicada a URLs. Consiste em testar milhares de palavras de uma **Wordlist** contra um servidor para identificar diretórios que não estão linkados publicamente.
- **Ferramentas de Elite:** Instalei e explorei o **ffuf** (Fuzz Faster U Fool) e o **dirb**, ferramentas essenciais para descoberta de conteúdo.

### 🚧 Enfrentando Defesas (Status Codes)
- **200 OK:** Diretório encontrado e acessível.
- **404 Not Found:** O diretório não existe.
- **429 Too Many Requests:** Identifiquei que este código indica a presença de **Rate Limiting**. O servidor percebeu o excesso de requisições e bloqueou o acesso temporariamente.
- **Estratégia de Evasão:** Aprendi que para contornar o erro 429 e sistemas de **WAF**, é necessário ajustar o *delay* (atraso) entre as requisições para parecer um tráfego legítimo.

### 🐍 Lógica de Automação
- Pratiquei a lógica de decisão em Python para tratar diferentes respostas HTTP, reforçando o entendimento de como automatizar a análise de resultados de um scan.

![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/pyt.24.30%20PM.png)

### 🇺🇸 Inglês Técnico:
- **Rate Limiting:** Limite de taxa de requisições.
- **Hidden Directories:** Diretórios escondidos/ocultos.
- **Active Recon:** Reconhecimento que interage diretamente com o alvo.

---
*Status: 17/1000 dias. A base está ficando sólida, o foco agora é a prática intensa.*

# 🛡️ Dia 18: Burp Suite e Interceptação de Tráfego

Neste décimo oitavo dia, dei um passo crucial ao instalar e configurar o **Burp Suite Community Edition**, a ferramenta padrão da indústria para testes de segurança em aplicações web.

### 🔌 O Coração do Pentest Web: Proxy de Interceptação
- **Conceito:** Aprendi a posicionar o Burp Suite entre o meu navegador e o servidor alvo, permitindo "parar o tempo" nas requisições HTTP.
- **Troubleshooting de Ambiente:** Enfrentei limitações de armazenamento no Chromebook (Crostini). Realizei a manutenção do sistema via terminal (`apt clean` / `autoremove`) e redimensionei a partição do Linux para permitir a instalação dos certificados CA do Burp.
- **HTTPS/SSL:** Entendi a necessidade de instalar o certificado do Burp no navegador para descriptografar e analisar tráfego seguro (HTTPS).

### 🛠️ Módulos Explorados
- **Proxy:** Interceptação e modificação de tráfego em tempo real (Request/Response).
- **Repeater:** Aprendi a reenviar requisições modificadas para testar vulnerabilidades de forma rápida, sem recarregar o navegador.
- **Lógica de Ataque:** Estudei como a manipulação de parâmetros (como preços ou funções de usuário) pode expor falhas de lógica de negócio e **Privilege Escalation** (Escalação de Privilégios).

![](https://github.com/wagnersilvakwm0022-tech/meus-dowloads/blob/main/Screenshot%202026-05-06%208.59.09%20PM.png)

### 🇺🇸 Inglês Técnico (Tech Vocabulary)
- **Intercept:** Interceptar a comunicação.
- **Forward / Drop:** Enviar ou descartar uma requisição.
- **Raw Data:** Dados brutos, sem formatação.
- **Request / Response:** O fluxo de pergunta (cliente) e resposta (servidor).

---
*Status: 18/1000 dias. Superando barreiras de hardware e dominando as ferramentas de elite.*







































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































