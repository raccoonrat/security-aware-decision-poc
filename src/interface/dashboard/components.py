import plotly.express as px
import streamlit as st

def show_realtime_threat(threat_data):
    fig = px.density_heatmap(
        threat_data,
        x='timestamp',
        y='threat_type',
        z='severity',
        histfunc="avg",
        nbinsx=20,
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig, use_container_width=True)

def display_decision_tree(reasoning_steps):
    nodes = []
    edges = []
    for i, step in enumerate(reasoning_steps):
        nodes.append({
            "id": i,
            "label": f"Step {i+1}\n{step['action']}",
            "color": "#FF6B6B" if "Block" in step else "#6BFF6B"
        })
        if i > 0:
            edges.append({"from": i-1, "to": i, "label": step['reason']})

    st_cyto(
        elements=nodes + edges,
        style={"height": "500px"},
        layout={"name": "cose"},
        key="decision-path"
    )
