#  Teste Técnico BYNE
## Requisitos
- [x] Servidor deve implementar dois serviços: Um que retorne números pares, e outro números ímpares;
- [x] Cada cliente ao se conectar ao servidor deve iniciar um processo que incrementa o valor recebido do servidor em 1 a cada 500ms, enviando o novo valor ao servidor;
- [x] Cada cliente deve, em um intervalo aleatório entre 3 e 5 segundos, requisitar ao servidor um número par ou ímpar, escolhido de forma aleatória, que será utilizado como novo valor de incremento, ao invés de 1;
- [x] Os números devem estar sempre no range 0-99;
- [x] Servidor deve enviar um valor ao aceitar conexão do cliente;
- [X] Servidor deve manter o último valor enviado para cada cliente. Caso um mesmo cliente se conecte, enviar esse valor para o mesmo. Caso não haja valor registrado, enviar 0;
- [X] Servidor deve manter um log de todas as mensagens trocadas;
- [X] Você pode utilizar qualquer linguagem/framework que se sentir mais confortável.
- [X] A entrega deve ser feita através de um repositório git público de sua escolha;
- [X] A data limite é até 28/02/22 às 23:59:59.