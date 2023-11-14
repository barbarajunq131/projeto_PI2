import streamlit as st
import sqlite3

# Aplicação Streamlit
# Função para cadastrar ONGs
def cadastrar_ong(nome, endereco, cep, area_atuacao):
    conn = sqlite3.connect('ongs.db')
    c = conn.cursor()
    c.execute("INSERT INTO ongs (nome, endereco, CEP, area_atuacao) VALUES (?, ?, ?, ?)", (nome, endereco, cep, area_atuacao))
    conn.commit()
    conn.close()
    st.success('ONG cadastrada com sucesso!')

st.title('Seja voluntário! Encontre uma ONG perto de você')

# Cadastro de ONGs na barra lateral (sidebar)
st.sidebar.header('Cadastrar nova ONG')
nome = st.sidebar.text_input('Nome da ONG')
endereco = st.sidebar.text_input('Endereço')
cep = st.sidebar.text_input('CEP')
area_atuacao = st.sidebar.text_input('Área de atuação')

if st.sidebar.button('Cadastrar ONG'):
    cadastrar_ong(nome, endereco, cep, area_atuacao)

 # Busca de ONGs por CEP ou Área de Atuação
filtro = st.radio('Filtrar por:', ('CEP', 'Área de Atuação'))

if filtro == 'CEP':
    cep_input = st.text_input('Digite o CEP para encontrar ONGs próximas')
    if st.button('Buscar por CEP'):
        conn = sqlite3.connect('ongs.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ongs WHERE CEP=?", (cep_input,))
        ongs_encontradas = c.fetchall()
        conn.close()

        if ongs_encontradas:
            st.header('ONGs encontradas pelo CEP:')
            for ong in ongs_encontradas:
                st.write(f"Nome: {ong[1]}, Endereço: {ong[2]}, CEP: {ong[3]}, Área de Atuação: {ong[4]}")
        else:
            st.warning('Nenhuma ONG encontrada para este CEP.')

else:  # Busca por Área de Atuação
    area_input = st.text_input('Digite a Área de Atuação para encontrar ONGs')
    if st.button('Buscar por Área de Atuação'):
        conn = sqlite3.connect('ongs.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ongs WHERE area_atuacao=?", (area_input,))
        ongs_por_area = c.fetchall()
        conn.close()

        if ongs_por_area:
            st.header(f'ONGs encontradas na Área de Atuação: {area_input}')
            for ong in ongs_por_area:
                st.write(f"Nome: {ong[1]}, Endereço: {ong[2]}, CEP: {ong[3]}, Área de Atuação: {ong[4]}")
        else:
            st.warning(f'Nenhuma ONG encontrada para a Área de Atuação: {area_input}.')
