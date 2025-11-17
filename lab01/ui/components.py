import streamlit as st
from typing import List, Dict, Any, Optional


def model_selector(models: List[str]) -> str:
    choice: str = st.pills(
        "Choose model",
        options=models,
        selection_mode='single',
        default=models[0]
    )
    return choice


def text_input_box() -> str:
    text: str = st.text_input(
        "Text to analyze",
        placeholder="Enter your sentence here..."
    )
    return text


def show_result(result: Dict[str, Any]) -> None:
    error: Optional[bool] = result.get('error')
    if error:
        message: str = result.get('message', 'Unknown error')
        st.error(f"API error: {message}")
        return

    raw: List[Dict[str, Any]] = result.get('raw', [])

    for item in raw:
        label: str = item.get('label', 'unknown')
        score_value: Any = item.get('score', 0)

        score: float = float(score_value)

        st.markdown(f"### {label.lower()}")
        st.progress(score)
        st.write(f"Score: **{score:.4f}**")
