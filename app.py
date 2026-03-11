import streamlit as st
from src.extraction import load_data

st.set_page_config(layout="wide")

def load_data():
    return pd.read_csv('data/processed/bikes_completed.csv')

def main():
    df = load_data()
    
    st.dataframe()

if __name__ == '__main__':
    main()