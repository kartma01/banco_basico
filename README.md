# banco_basico
Este código é uma simulação simplificada de um sistema bancário que permite aos usuários realizar operações básicas, como depósitos, saques e visualização de extrato. A ideia por trás desse código é fornecer uma interface de linha de comando para interagir com a conta bancária.

O programa apresenta um menu com as seguintes opções:

[d] Depositar: Permite ao usuário fazer um depósito em sua conta. O valor do depósito é adicionado ao saldo da conta e registrado no extrato.
[s] Sacar: Permite ao usuário fazer um saque da conta. O valor do saque é subtraído do saldo, desde que o saldo seja suficiente e o valor do saque não exceda o limite diário e o limite por transação. As informações do saque são registradas no extrato.
[e] Extrato: Permite ao usuário visualizar o extrato da conta, que exibe as transações realizadas, incluindo depósitos e saques, bem como o saldo atual da conta.
[q] Sair: Encerra o programa.
O código utiliza variáveis para armazenar informações sobre a conta, como saldo, limite de saque diário, número de saques realizados e extrato. Um loop while infinito é usado para que o menu seja exibido continuamente até que o usuário decida sair.

O código verifica a opção escolhida pelo usuário e executa a ação correspondente. Se uma opção inválida for escolhida, uma mensagem de erro é exibida. O código também realiza algumas validações, como verificar se o valor do depósito é válido e se o usuário possui saldo suficiente para fazer um saque.

Ao final do programa, o usuário pode sair do menu selecionando a opção "q". É importante ressaltar que este código é apenas uma simulação e não se trata de um sistema bancário real, pois não considera muitas das complexidades e requisitos de segurança envolvidos em operações bancárias.
