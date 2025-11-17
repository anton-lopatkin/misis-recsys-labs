from core.config import get_hf_token
from core.models import MODELS
from core.api import query_model
from ui.components import model_selector, text_input_box, show_result

import streamlit as st
from typing import Optional, Any, Dict

st.set_page_config(
    page_title="Text Sentiment Analysis",
    page_icon="📝"
)


def main() -> None:
    st.title("📝 Text Sentiment Analysis")

    try:
        hf_token: str = get_hf_token()
    except RuntimeError as e:
        st.error(str(e))
        return

    model_id: str = model_selector(MODELS)
    text: Optional[str] = text_input_box()

    if text:
        with st.spinner("Analyzing..."):
            result: Dict[str, Any] = query_model(model_id, text, hf_token)

        show_result(result) 
        

if __name__ == "__main__":
    main()
