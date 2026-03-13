import pandas as pd
import plotly.express as px
import streamlit as st

def rd1_question_9(df):
    df_grouped = df[['id', 'seller_type']].groupby('seller_type')

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={'id': 'count'})

    df_grouped
    
    fig = px.bar(
        df_grouped,
        x="seller_type",
        y="count",
        labels={"sellers_type": "Seller Type", "count":"Quantity"}
    )
    
    fig.update_traces(textposition="outside")
    
    st.plotly_chart(fig, use_container_width=True)
    
    return None

def rd1_question13(df):
    df_grouped = (
        df.groupby("owner")
        .agg(qty =pd.NamedAgg("id","count"))
        .sort_values("qty")
        .reset_index()
    )
    
    fig = px.bar (
        df_grouped,
        x="owner",
        y="qty",
        labels={"owner": "Owner Types", "qty": "Quantuty"},
        color = "owner",
        text = "qty"
    )
    
    fig.update_traces(textposition="outside")
    
    st.plotly_chart(fig, use_container_width = True)
    
    return None

def rd1_question14(df):
    st.text("As we can see, bikes with high kilometer have cheapier prices")
    
    fig = px.scatter(
        df,
        x="km_driven",
        y="selling_price",
        labels = {"km_driven": "Kilometers", "selling_price": "Selling Price"},
    )
    
    st.plotly_chart(fig, use_container_width = True)
    
    return None

