# Caixa_Eletronico
Este projeto consiste em um programa Python que simula um caixa eletrônico para realizar saques de valores pré-definidos. O objetivo principal é proporcionar uma experiência simples e rápida para o usuário, garantindo que o saque seja efetuado de forma segura e eficiente.





Funcionamento do Código:


Interface de Usuário Intuitiva:
O programa inicia apresentando uma mensagem de boas-vindas e instruções para o usuário.
Utiliza a função limpar_console() para limpar a tela do console, proporcionando uma experiência mais organizada e limpa para o usuário.

Validação de Entrada de Dados:
O código utiliza um loop while em conjunto com a estrutura try-except para garantir que apenas valores inteiros positivos sejam aceitos como entrada do usuário.
Em caso de entrada inválida, são exibidas mensagens de erro específicas, orientando o usuário a inserir valores válidos.
Geração Aleatória de Notas:

A lista valoresDisponiveis armazena os valores das notas disponíveis para o saque (R$1, R$10, R$20 e R$50).
O programa utiliza a função random.choice() para selecionar de forma aleatória as notas disponíveis, garantindo uma distribuição aleatória dos valores sacados.

Contagem de Notas Utilizadas:
Após o saque ser realizado com sucesso, o programa utiliza a classe Counter da biblioteca collections para contar a quantidade de cada nota utilizada.
As informações sobre as notas utilizadas são então exibidas ao usuário de forma clara e organizada.

Registro de Transações:
Todas as transações de saque são registradas em um arquivo de log (caixa.log) utilizando o módulo logging do Python.
O registro inclui informações como a data e hora do saque, valores sacados e notas utilizadas, proporcionando uma trilha de auditoria para análises futuras.

Encerramento Controlado do Caixa:
Após cada saque, o programa oferece ao usuário a opção de realizar outro saque ou encerrar o serviço.
Ao encerrar o caixa, uma mensagem de agradecimento é exibida, junto com uma mensagem de fechamento no arquivo de log.





Por que foram utilizados tais métodos:


limpar_console(): Utilizado para proporcionar uma experiência de usuário mais limpa e organizada, removendo informações desnecessárias da tela do console.

try-except para validação de entrada de dados: Garante que o programa lide de forma adequada com entradas inválidas do usuário, evitando falhas inesperadas.

random.choice(): Utilizado para garantir que as notas selecionadas para o saque sejam escolhidas de forma aleatória, proporcionando uma experiência mais dinâmica.

Counter da biblioteca collections: Facilita a contagem e a organização das notas utilizadas durante o saque, fornecendo ao usuário um resumo claro e conciso das transações.

logging para registro de transações: Permite registrar todas as transações de saque em um arquivo de log, garantindo uma trilha de auditoria para análises futuras e proporcionando maior segurança e confiabilidade ao sistema.
