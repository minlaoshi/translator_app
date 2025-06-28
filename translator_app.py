import streamlit as st
from deep_translator import GoogleTranslator
import pandas as pd

st.set_page_config(
    page_title="다국어 번역기",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 다국어 번역기")
st.markdown("""
이 앱은 Google 번역 API를 사용하여 다양한 언어 간의 번역을 제공합니다. 텍스트를 입력하고 원하는 언어를 선택하여 번역해보세요. """)

LANGUAGES = {
    '한국어' :'ko',
    '영어':'en',
    '일본어':'ja',
    '중국어':'zh-CN',
    '스페인어':'es',
    '프랑스어':'fr',
    '독일어':'de',
    '러시아어':'ru',
}

st.sidebar.header("번역 설정")
source_lang = st.sidebar.selectbox(
    "원본 언어",
    list(LANGUAGES.keys())
)
target_lang = st.sidebar.selectbox(
    "번역 언어",
    list(LANGUAGES.keys())
)

st.sidebar.write("made by ✍️KMS™️")

col1, col2 = st.columns(2)

with col1:
    st.subheader("번역할 텍스트")
    source_text = st.text_area(
        "텍스트를 입력하세요.",
        height=200,
        placeholder="번역할 텍스트를 입력하세요."
    )

with col2:
    st.subheader("번역 결과")
    if source_text:
        try:
            translator = GoogleTranslator(
               source=LANGUAGES[source_lang],
               target=LANGUAGES[target_lang]
            )
            translated_text = translator.translate(source_text)

            st.text_area(
                "번역된 텍스트",
                translated_text,
                height = 200,
                disabled = True
            )

            if st.button("번역 결과 복사"):
                st.write("'''")
                st.code(translated_text)
                st.write("'''")
        except Exception as e:
            st.error(f"번역 중 오류가 발생했습니다: {str(e)}")

    else:
        st.info("왼쪽에 번역할 텍스트를 입력하세요.")

# st.markdown("---")
# st.subheader("여러 문장 번역")
# st.markdown("어러 문장을 한 번에 번역하려면 아래 형식으로 입력하세요 (한 줄에 하나의 문장)")

# batch_text = st.text_area(
#     "여러 문장 입력",
#     height=150,
#     placeholder = "안녕하세요\n반갑습니다\n좋은 하루 되세요"
# )

# if st.button("배치 번역 실행"):
#     try:
#         texts = [text.strip() for text in batch_text.split("\n") if text.strip()]
#         translator = GoogleTranslator(
#             source=LANGUAGES[source_lang],
#             target=LANGUAGES[target_lang]
#         )
#         translated_texts = translator.translate_batch(texts)

#         df = pd.DataFrame({
#             '원본': texts,
#             '번역': translated_texts
#         })
#         st.dataframe(df, use_container_width=True)

#     except Exception as e:
#         st.error(f"배치 번역 중 오류가 발생했습니다: {str(e)}")

st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Powered by Google Translate API | Created with Streamlit</p>
</div>
""", unsafe_allow_html=True)
