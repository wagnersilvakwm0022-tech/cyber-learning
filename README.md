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












































































