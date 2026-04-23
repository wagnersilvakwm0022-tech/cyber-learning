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
![](
- `curl -I -L https://google.com`: Segue automaticamente os redirecionamentos (como o erro 301) até chegar ao destino final (200 OK).
![](https://github.com/wagnersilvakwm0022-tech/cyber-learning/blob/main/pdf.png)
### 🇺🇸 Inglês Técnico (Tech Vocabulary)
- **Request:** Requisição (o pedido feito pelo cliente).
- **Response:** Resposta (o retorno enviado pelo servidor).
- **Header:** Cabeçalho (metadados da conexão).
- **Redirect:** Redirecionamento.
- **Forbidden:** Proibido/Negado.

---
*Status: 5 horas de estudo concluídas. Amanhã: Dia 6 - Finalizando os fundamentos de Rede (Portas e Protocolos).*

































































