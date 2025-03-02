import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Função para pegar os dados do Yahoo Finance \ Function to collect data from Yahoo Finance
def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    if 'Adj Close' not in data.columns:
        data['Adj Close'] = data['Close']
    return data

# Função para calcular o retorno simples \ Function to calculate simple return
def simple_return(data):
    data['simple_return'] = (data['Adj Close'] / data['Adj Close'].shift(1)) - 1
    return data['simple_return']

# Função para calcular o retorno logarítmico \ Function to calculate logarithmic return
def log_return(data):
    data['log_return'] = np.log(data['Adj Close'] / data['Adj Close'].shift(1))
    return data['log_return']

# Função para plotar o gráfico de linha \ Function to plot line graph
def plot_line(data, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Adj Close'], mode='lines', name='Adj Close'))
    fig.update_layout(title_text=title, xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)

# Função para plotar o gráfico de candlestick \ Function to plot the candlestick chart
def plot_candlestick(data, title):
    fig = go.Figure(data=[go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])])
    fig.update_layout(title_text=title, xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)

# Função para plotar o gráfico de retorno simples \ Function to plot simple return graph
def plot_simple_return(data, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['simple_return'], mode='lines', name='Simple Return'))
    fig.update_layout(title_text=title, xaxis_title='Date', yaxis_title='Return')
    st.plotly_chart(fig)

# Função para plotar o gráfico de retorno logarítmico \ Function to plot the logarithmic return graph
def plot_log_return(data, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['log_return'], mode='lines', name='Log Return'))
    fig.update_layout(title_text=title, xaxis_title='Date', yaxis_title='Return')
    st.plotly_chart(fig)

# Função para plotar o gráfico de retorno simples acumulado \ Function to plot the cumulative simple return graph
def plot_cumulative_simple_return(data, title):
    data['cumulative_simple_return'] = (1 + data['simple_return']).cumprod()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['cumulative_simple_return'], mode='lines', name='Cumulative Simple Return'))
    fig.update_layout(title_text=title, xaxis_title='Date', yaxis_title='Return')
    st.plotly_chart(fig)

# Função para plotar o gráfico de retorno logarítmico acumulado \ Function to plot the cumulative logarithmic return graph
def plot_cumulative_log_return(data, title):
    data['cumulative_log_return'] = data['log_return'].cumsum()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['cumulative_log_return'], mode='lines', name='Cumulative Log Return'))
    fig.update_layout(title_text=title, xaxis_title='Date', yaxis_title='Return')
    st.plotly_chart(fig)

# Função para plotar o gráfico de densidade de retorno simples \ Function to plot simple return density plot
def plot_density_simple_return(data, title):
    fig = px.histogram(data, x='simple_return', nbins=50, title=title)
    st.plotly_chart(fig)

# Função para plotar o gráfico de densidade de retorno logarítmico \ Function to plot logarithmic return density graph
def plot_density_log_return(data, title):
    fig = px.histogram(data, x='log_return', nbins=50, title=title)
    st.plotly_chart(fig)

# Função para plotar o gráfico de retorno simples vs retorno logarítmico \ Function to plot simple return vs logarithmic return graph
def plot_simple_vs_log_return(data, title):
    fig = make_subplots(rows=1, cols=2, subplot_titles=('Simple Return', 'Log Return'))
    fig.add_trace(go.Scatter(x=data.index, y=data['simple_return'], mode='lines', name='Simple Return'), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['log_return'], mode='lines', name='Log Return'), row=1, col=2)
    fig.update_layout(title_text=title)
    st.plotly_chart(fig)

# Título do painel \ title
st.title('Painel Financeiro')

# Sidebar
st.sidebar.title('Configurações')
ticker = st.sidebar.text_input('Ticker', 'AAPL')
start_date = st.sidebar.date_input('Data Inicial', datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input('Data Final', datetime.date(2021, 12, 31))

# Pegar os dados \ get the data
data = get_data(ticker, start_date, end_date)

# Verificar se os dados foram baixados corretamente \ Verify that the data was downloaded correctly
if data.empty:
    st.write("Não foram encontrados dados para o ticker e período especificados.")
else:
    # Verificar se a coluna 'Adj Close' está presente no DataFrame \ Check if column 'Adj Close' is present in DataFrame
    if 'Adj Close' not in data.columns:
        st.write("A coluna 'Adj Close' não está presente nos dados.")
    else:
        # Exibir os dados \ display the data
        st.write('**Dados**')
        st.write(data)

        # Gráfico de Linha - line graph
        st.write('**Gráfico de Linha**')
        plot_line(data, 'Gráfico de Linha')

        # Gráfico de Candlestick - Candlestick Chart
        st.write('**Gráfico de Candlestick**')
        plot_candlestick(data, 'Gráfico de Candlestick')

        # Retorno Simples - Simple Return
        st.write('**Retorno Simples**')
        data['simple_return'] = simple_return(data)
        st.write(data['simple_return'])

        # Gráfico de Retorno Simples
        st.write('**Gráfico de Retorno Simples**')
        plot_simple_return(data, 'Gráfico de Retorno Simples')

        # Gráfico de Retorno Simples Acumulado
        st.write('**Gráfico de Retorno Simples Acumulado**')
        plot_cumulative_simple_return(data, 'Gráfico de Retorno Simples Acumulado')

        # Gráfico de Densidade de Retorno Simples
        st.write('**Gráfico de Densidade de Retorno Simples**')
        plot_density_simple_return(data, 'Gráfico de Densidade de Retorno Simples')

        # Retorno Logarítmico
        st.write('**Retorno Logarítmico**')
        data['log_return'] = log_return(data)
        st.write(data['log_return'])

        # Gráfico de Retorno Logarítmico
        st.write('**Gráfico de Retorno Logarítmico**')
        plot_log_return(data, 'Gráfico de Retorno Logarítmico')

        # Gráfico de Retorno Logarítmico Acumulado
        st.write('**Gráfico de Retorno Logarítmico Acumulado**')
        plot_cumulative_log_return(data, 'Gráfico de Retorno Logarítmico Acumulado')

        # Gráfico de Densidade de Retorno Logarítmico
        st.write('**Gráfico de Densidade de Retorno Logarítmico**')
        plot_density_log_return(data, 'Gráfico de Densidade de Retorno Logarítmico')

        # Gráfico de Retorno Simples vs Retorno Logarítmico
        st.write('**Gráfico de Retorno Simples vs Retorno Logarítmico**')
        plot_simple_vs_log_return(data, 'Gráfico de Retorno Simples vs Retorno Logarítmico')
