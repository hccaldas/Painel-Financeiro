# Painel Financeiro em Python

Este repositório contém um script em Python que cria um painel financeiro interativo usando Streamlit. O painel permite visualizar dados financeiros de ações, calcular retornos simples e logarítmicos, e plotar vários tipos de gráficos.

## Funcionalidades

- Obtenção de dados financeiros do Yahoo Finance.
- Cálculo de retornos simples e logarítmicos.
- Plotagem de gráficos de linha, candlestick, retornos simples e logarítmicos, e densidade de retornos.
- Interface interativa usando Streamlit.

## Pré-requisitos

- Python 3.x
- Bibliotecas `yfinance`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `streamlit`, `plotly`

Você pode instalar todas as bibliotecas necessárias usando o `pip`:

```bash
pip install yfinance pandas numpy matplotlib seaborn streamlit plotly

## Como usar

1.Clone este repositório ou copie o código para o seu ambiente local.
2.Certifique-se de ter o Python 3.x instalado no seu sistema.
3.Instale as bibliotecas necessárias usando os comandos acima.
4.Execute o script usando o comando: streamlit run painel_finance.py
5.O painel será aberto em uma nova aba do navegado

Exemplo de Uso

Funções
get_data(ticker, start_date, end_date)
Obtém os dados financeiros do Yahoo Finance para o ticker especificado e o intervalo de datas.

simple_return(data)
Calcula o retorno simples dos dados financeiros.

log_return(data)
Calcula o retorno logarítmico dos dados financeiros.

plot_line(data, title)
Plota um gráfico de linha dos preços ajustados de fechamento.

plot_candlestick(data, title)
Plota um gráfico de candlestick dos dados financeiros.

plot_simple_return(data, title)
Plota um gráfico de linha dos retornos simples.

plot_log_return(data, title)
Plota um gráfico de linha dos retornos logarítmicos.

plot_cumulative_simple_return(data, title)
Plota um gráfico de linha dos retornos simples acumulados.

plot_cumulative_log_return(data, title)
Plota um gráfico de linha dos retornos logarítmicos acumulados.

plot_density_simple_return(data, title)
Plota um gráfico de densidade dos retornos simples.

plot_density_log_return(data, title)
Plota um gráfico de densidade dos retornos logarítmicos.

plot_simple_vs_log_return(data, title)
Plota gráficos comparativos dos retornos simples e logarítmicos.

Alterando para Receber Outros Resultados
Para alterar o ticker ou o intervalo de datas, você pode usar a barra lateral do Streamlit:

Ticker: Insira o símbolo do ticker da ação que deseja analisar.

Data Inicial: Selecione a data inicial do intervalo de análise.

Data Final: Selecione a data final do intervalo de análise.

Contribuição
Sinta-se à vontade para contribuir com melhorias para este projeto. Você pode fazer isso abrindo uma issue ou enviando um pull request.

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
