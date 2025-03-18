import streamlit as st
from ..components import ThreatMap, DecisionTree

def main():
    st.title("安全决策仪表板")

    with st.sidebar:
        st.header("控制面板")
        threat_filter = st.slider("威胁阈值", 0.0, 1.0, 0.7)

    tab1, tab2 = st.tabs(["实时监控", "决策分析"])

    with tab1:
        ThreatMap().render()

    with tab2:
        DecisionTree().render()

if __name__ == "__main__":
    main()
