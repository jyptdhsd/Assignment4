import streamlit as st


def main():
    st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")

    st.title("Zhou Yunyi")

    st.markdown(
        """
        Welcome to the KFC Sales Performance Dashboard.

        Explore key sales insights and performance trends in a clean, professional view.
        """
    )

    if st.button("View Dashboard"):
        st.switch_page("pages/app.py")


if __name__ == "__main__":
    main()
