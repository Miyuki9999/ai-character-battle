import streamlit as st
from supabase import create_client
import uuid

st.set_page_config(
    page_title="AI最強キャラクターバトル",
    page_icon="🔥",
    layout="centered"
)

supabase = create_client(
    st.secrets["https://dxnqazilkqxbxoxwccwe.supabase.co/rest/v1/"],
    st.secrets["sb_publishable_mF_dxOWXuIuofLvREq7J0Q_oYn6q3gt"],
)

TOURNAMENT_ID = 1

st.titile("🔥AI最強キャラクター大会🔥")
st.write(
    "AIで作った自分だけの最強キャラを登録しよう"
)
st.info(
    "⚠️AIで作ったキャラクター画像を登録してください"
    "本人や友達の写真はアップロード禁止です"
) 
st.header("①キャラクター登録")
name = st.text_input(
    "キャラクター名",
    placeholder="例：炎竜ゼウス"
)

image = st.file_uploader(
    "キャラクター説明"
    placehoder="どんなキャラクターなのか説明してください"
)

speacil_move = st.text_input(
"弱点"
) 
