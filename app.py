%%writefile app.py

import streamlit as st
import random
import itertools


# -------------------------
# ふりがな表示用
# -------------------------

def ruby(word, reading):
    return f"<ruby>{word}<rt>{reading}</rt></ruby>"



# -------------------------
# 設定
# -------------------------

st.set_page_config(
    page_title="AI最強キャラクター大会"
)


if "characters" not in st.session_state:
    st.session_state.characters = []



# -------------------------
# AI審判
# -------------------------

def judge(char1,char2):

    score1 = (
        char1["attack"]
        + char1["defense"]
        + char1["skill"]
        + random.randint(0,30)
    )


    score2 = (
        char2["attack"]
        + char2["defense"]
        + char2["skill"]
        + random.randint(0,30)
    )


    if score1 >= score2:
        return char1,char2

    else:
        return char2,char1



# -------------------------
# 実況
# -------------------------

def commentary(win,lose):

    texts=[

    f"{win['name']}の必殺技（ひっさつわざ）が炸裂（さくれつ）！",

    f"激闘（げきとう）の末（すえ）、{win['name']}が勝利（しょうり）！",

    f"{lose['name']}も強敵（きょうてき）だったが、{win['name']}が上回（うわまわ）った！",

    f"会場（かいじょう）が大盛（おおも）り上（あ）がり！{win['name']}の勝利！"

    ]

    return random.choice(texts)



# -------------------------
# タイトル
# -------------------------

st.markdown(
    f"""
    <h1>
    🔥 {ruby('AI最強','AIさいきょう')}
    {ruby('キャラクター','キャラクター')}
    {ruby('大会','たいかい')}
    🔥
    </h1>
    """,
    unsafe_allow_html=True
)


st.write(
    "自分（じぶん）だけの最強（さいきょう）キャラクターを作（つく）って戦（たたか）わせよう！"
)



# -------------------------
# 登録
# -------------------------

st.header(
    "① キャラクター登録（とうろく）"
)


name=st.text_input(
    "名前（なまえ）"
)


image=st.file_uploader(
    "画像（がぞう）",
    type=["png","jpg","jpeg"]
)


description=st.text_area(
    "能力（のうりょく）説明（せつめい）"
)



if st.button("登録（とうろく）"):


    if name:

        char={

            "name":name,

            "image":image,

            "description":description,


            "attack":random.randint(50,100),

            "defense":random.randint(50,100),

            "skill":random.randint(50,100)

        }


        st.session_state.characters.append(char)


        st.success(
            f"{name} が参加（さんか）しました！"
        )



# -------------------------
# 一覧
# -------------------------

st.header(
    "参加（さんか）キャラクター"
)


for c in st.session_state.characters:

    st.write(
        "⚔️",
        c["name"],
        "攻撃（こうげき）",
        c["attack"],
        "防御（ぼうぎょ）",
        c["defense"],
        "必殺（ひっさつ）",
        c["skill"]
    )



# -------------------------
# 大会
# -------------------------

if len(st.session_state.characters)>=2:


    st.header(
        "② 総当（そうあ）たりバトル"
    )


    if st.button(
        "大会開始（たいかいかいし）"
    ):


        wins={}


        for c in st.session_state.characters:
            wins[c["name"]]=0



        matches=list(
            itertools.combinations(
                st.session_state.characters,
                2
            )
        )



        for a,b in matches:


            winner,loser=judge(a,b)


            wins[winner["name"]]+=1



            st.subheader(
                f"{a['name']} VS {b['name']}"
            )


            st.write(
                "🏆 勝者（しょうしゃ）：",
                winner["name"]
            )


            st.write(
                commentary(
                    winner,
                    loser
                )
            )



        st.header(
            "🏆 最終（さいしゅう）ランキング"
        )


        ranking=sorted(
            wins.items(),
            key=lambda x:x[1],
            reverse=True
        )


        for i,item in enumerate(ranking):

            st.write(
                i+1,
                "位（い）",
                item[0],
                item[1],
                "勝（しょう）"
            )
