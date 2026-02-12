# BioSemma
BioSemma - é uma plataforma digital projetada para modernizar, desburocratizar e dar transparência ao processo de licenciamento ambiental. O sistema automatiza desde a triagem do potencial poluidor até a fiscalização de vencimentos em tempo real com notificações via WhatsApp.

## 1. Requisitos Funcionais (RF)

Estes descrevem o que o sistema deve fazer (as funcionalidades diretas).

* **RF01 - Portal do Requerente:** Interface para que o consultor ou empreendedor faça o upload de documentos (PDF, DWG, SHP) e preencha o formulário de caracterização do empreendimento.
* **RF02 - Triagem Automática:** O sistema deve classificar automaticamente o potencial poluidor e o porte da atividade com base na legislação vigente, definindo se é Licença Prévia (LP), de Instalação (LI), de Operação (LO) ou Simplificada (LAS).
* **RF03 - Módulo de Geoprocessamento (GIS):** Integração com mapas para verificar automaticamente se o polígono do projeto sobrepõe Áreas de Preservação Permanente (APP), Unidades de Conservação ou Terras Indígenas.
* **RF04 - Workflow de Análise (Tramitação):** Fluxo de trabalho digital onde o processo passa pelo setor de protocolo, análise técnica, vistoria e parecer jurídico.
* **RF05 - Gestão de Condicionantes:** Sistema de alertas para o órgão ambiental e para o empreendedor sobre prazos de validade de licenças e cumprimento de condicionantes.
* **RF06 - Emissão de Taxas (DAM):** Geração automática de boletos de taxas ambientais integrados ao sistema tributário municipal.
* **RF07 - Assinatura Digital:** Gov.br para assinatura de pareceres e licenças.
* **RF08 - Monitoramento de Validade:** O sistema deve varrer diariamente a base de dados de licenças emitidas para identificar as que expiram em 5 dias ou menos.
* **RF09 - Integração com API de WhatsApp:** Conexão com uma API (como Twilio, MessageBird ou Evolution API) para envio automático de mensagens.
* **RF10 - Gestão de Alertas:** Painel para o administrador visualizar quais avisos foram enviados e se foram entregues com sucesso.

## 2. Requisitos Não Funcionais (RNF)

Estes descrevem os critérios de operação e qualidade do sistema.

* **RNF01 - Segurança e Auditoria:** Registro de logs de todas as alterações (quem alterou o quê e quando), fundamental para processos de fiscalização.
* **RNF02 - Disponibilidade:** O sistema deve estar disponível 24/7 via web, considerando que consultores costumam trabalhar fora do horário comercial.
* **RNF03 - Escalabilidade:** Capacidade de suportar o aumento do volume de dados geográficos (arquivos pesados de shapefiles e imagens de satélite).
* **RNF04 - Interoperabilidade:** Capacidade de se comunicar com outros sistemas (Sinaflor, Cadastro Ambiental Rural - CAR e sistemas da Secretaria de Fazenda).
* **RNF05 - Usabilidade:** Interface intuitiva para que técnicos com pouca afinidade com TI consigam emitir pareceres sem dificuldades.
* **RNF06 - Confiabilidade da Notificação:** O sistema deve tratar erros de API (ex: se o celular do empresário estiver sem internet) e tentar reenviar em um intervalo de 1 hora, limitado a 3 tentativas.

## 3. Estrutura de Níveis de Acesso

Considerando uma hierarquia eficiente para o controle de dados:

| Perfil | Permissões |
| --- | --- |
| **Superusuário** | Acesso total, configuração de tabelas de taxas, gestão de usuários e logs de auditoria. |
| **Técnico Analista** | Análise de processos, upload de pareceres e relatórios de vistoria. Não apaga processos. |
| **Usuário Visualizador** | Consulta de processos e emissão de relatórios estatísticos (Ex: Ministério Público ou Secretário). |

## 4. Fluxo do Processo Digital

### Próximos Passos Sugeridos

Para tornar esse sistema "custo zero" ou altamente eficiente, você pode utilizar tecnologias como:

* **PostgreSQL com PostGIS:** Para o banco de dados geográfico.
* **Python (Django/FastAPI):** Para a lógica do sistema (aproveitando seu interesse na linguagem).
* **Leaflet ou OpenLayers:** Para a visualização dos mapas no navegador.
