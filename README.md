# ComparadorTabelasSimples

## O que é isto?

Um simples programa que fiz para ajudar a empresa em que meu pai trabalhava; um funcionário precisava frequentemente conferir se havia algum boleto que ainda precisava ser pago (tabela do SIEG), verificando na tabela de contas pagas fornecida pelo sistema da empresa (tabela do FOCCO); como era uma tarefa diária, isso fazia com que o dito funcionário gastasse cerca de 10 minutos por dia fazendo esta conferência, e com este programa, não chegava a gastar 30 segundos.

## Como funciona?

O programa abre uma interface (que programei usando o Tkinter) com campos para preencher o local de ambas as tabelas (e botões que abrem uma janela do Explorador de Arquivos, para facilitar a tarefa), e caso ambos os campos estejam preenchidos com arquivos válidos, pode ser feita a comparação.
Para comparar, o programa utiliza a biblioteca Pandas, guardando ambas as tabelas (Csv e Excel) em variáveis; depois, por meio do método Map da Lista e de uma compreensão de lista, é criada uma nova coluna chamada "Verificado" em uma das tabelas, que indica se aquele boleto está ou não na lista de já pagos; após a conferência, é criada uma nova variável, para guardar uma versão da tabela com as células da nova coluna coloridas e centralizadas.
Por fim, a tabela final é salva em um arquivo Excel chamado "Final" na mesma pasta.

## O que aprendi com isto?

A tarefa de comparar as tabelas em si foi um tanto fácil, levei poucas horas para concluir; mas como na época que escrevi eu não tinha experiência em criar interfaces, demorou um pouco para aprender a lidar com o Tkinter (quase uma semana). Ainda assim, foi um projeto que me deu uma satisfação imensa ao ser concluído, por poder ajudar outras pessoas através da tecnologia (ainda mais por indiretamente auxiliar meu pai), além de poder aprender a usar novas ferramentas (o Pandas, por exemplo).

## Como posso testar?

Basta executar o arquivo "main.py", selecionar os dois arquivos de teste (no primeiro campo o arquivo .csv, no segundo o arquivo .xlsx) e clicar em "Converter"; uma tabela chamada "Final" será criada, com a comparação feita entre os dois arquivos.
