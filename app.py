import streamlit as st
from nlp_utils import split_with_delimiters, get_longest_common_word_sequences 

def hide_made_by_streamlit():
    hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def load_data():
    """Load questions, context and output dict by reading from csv
        with:
        - questions being a list of string
        - context a list of string
        - output_dict a dict of list of string
    """

    questions = [
        "How representative are iPSC kidney models for human kidney?",
        "How does stress affect immune system response in humans?",
        "What surface proteins internalize?"
    ]

    context = ["full context"] * 3

    output_dict = {
        "LLM 1": ["llm1_output_1 full context"*10,"llm1_output_2","llm1_output_3"],
        "LLM 2": ["llm2_output_1","llm2_output_2","llm2_output_3"],
        "LLM 3": ["llm3_output_1","llm3_output_2","llm3_output_3"]
    }

    return questions, context, output_dict


def app():

    questions, context, output_dict = load_data()

    st.title("LLM Output Comparison")

    selected_models = st.multiselect("Select models to display", list(output_dict.keys()), default=list(output_dict.keys()))

    selected_question = st.selectbox("Select input to compare", questions)
    selected_input_index = questions.index(selected_question)

    st.write("Relative context:\n\n", context[selected_input_index])

    for key in output_dict.keys():
        if key in selected_models:
            with st.expander(key):
                st.write("Output:\n", output_dict[key][selected_input_index])

    hide_made_by_streamlit()

if __name__ == '__main__':
    app()