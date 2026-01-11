import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.markdown("""
<style>
html, body, [class*="css"]  {color-scheme: light !important; background: white !important;}
.header-section {text-align: center; padding: 1.5rem; margin: 1rem 0; border-bottom: 2px solid #e0e0e0; border-radius: 6px;}
.result-high {border-left: 4px solid #d32f2f; padding: 1.2rem; margin: 1rem 0; border-radius: 6px; }
.result-low {border-left: 4px solid #388e3c; padding: 1.2rem; margin: 1rem 0; border-radius: 6px; }
.metric-container {padding: 0.8rem !important; margin: 0.3rem !important;}
h1 {color: #fff !important; font-size: 1.8rem !important;}
h2 {color: #fff !important; font-size: 1.3rem !important;}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load('diabetes_model.pkl')

model = load_model()

st.set_page_config(page_title="Silent Disease Detector", layout="wide", initial_sidebar_state="expanded")

# Compact clean header
st.markdown("""
<div class='header-section'>
    <h1>🩺 Silent Disease Detector</h1>
    <p style=' font-size: 1rem; margin: 0;'>Diabetes Risk | PIMA Dataset | 77% Accuracy</p>
</div>
""", unsafe_allow_html=True)

# Compact sidebar - Single column inputs
with st.sidebar:
    st.header("📊 Lab Values")
    st.caption("Normal ranges shown")
    
    pregnancies = st.number_input("Pregnancies", 0, 17, 3, 1, help="0-17")
    glucose = st.number_input("Glucose mg/dL", 0, 200, 90, 5, help="70-140 normal")
    bp = st.number_input("BP mmHg", 0, 130, 72, 2, help="50-90 normal")
    skin = st.number_input("Skin mm", 0, 100, 20, 1, help="7-50 normal")
    insulin = st.number_input("Insulin", 0, 850, 50, 10, help="2-25 normal")
    bmi = st.number_input("BMI", 0.0, 70.0, 22.0, 0.1, help="18.5-24.9 normal")
    pedigree = st.number_input("Pedigree", 0.0, 3.0, 0.5, 0.05, help="0-1 normal")
    age = st.number_input("Age", 20, 80, 30, 1, help="20-60 normal")

# PERFECT CENTER BUTTON - Fixed width
col1, col2, col3 = st.columns([1, 10, 1])
with col2:
    if st.button("Analyze Risk", type="primary", help="Predict diabetes probability"):
        input_data = pd.DataFrame({
            'Pregnancies': [pregnancies], 'Glucose': [glucose], 
            'BloodPressure': [bp], 'SkinThickness': [skin],
            'Insulin': [insulin], 'BMI': [bmi],
            'DiabetesPedigreeFunction': [pedigree], 'Age': [age]
        })
        
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] * 100
        
        # Results 
        st.markdown("### Results")
        if prediction == 1:
            st.markdown(f"""
            <div class='result-high'>
                <h1 style='margin: 0;'>HIGH RISK</h1>
                <h2 style='margin: 0.2rem 0;'>{probability:.1f}%</h2>
                <p style='margin: 0.5rem 0;'>Consult doctor immediately</p>
            </div>
            """, unsafe_allow_html=True)
            st.error("🚨 Multiple risk factors detected")
        else:
            st.markdown(f"""
            <div class='result-low'>
                <h1 style='margin: 0;'>LOW RISK</h1>
                <h2 style='margin: 0.2rem 0;'>{probability:.1f}%</h2>
                <p style='margin: 0.5rem 0;'>Continue monitoring</p>
            </div>
            """, unsafe_allow_html=True)
            st.success("✅ No immediate concerns")
        
        # Metrics 
        col_met1, col_met2, col_met3 = st.columns(3)
        with col_met1:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric("Risk", "HIGH" if prediction else "LOW")
            st.markdown('</div>', unsafe_allow_html=True)
        with col_met2:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric("Probability", f"{probability:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)
        with col_met3:
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric("Model", "77%")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Compact risk table
        st.markdown("### Risk Factors")
        risk_table = pd.DataFrame({
            'Parameter': ['Glucose>140', 'BMI>30', 'Age>45', 'Insulin>150', 'BP>90'],
            'Status': ['High' if glucose>140 else 'Safe', 'High' if bmi>30 else 'Safe',
                      'High' if age>45 else 'Safe', 'High' if insulin>150 else 'Safe',
                      'High' if bp>90 else 'Safe']
        })
        st.table(risk_table)
        
       # PERFECT CENTERED HORIZONTAL SQUARE CHART
        col_center1, col_center2, col_center3 = st.columns([1, 10, 1])  
        with col_center2:
            # FIXED Horizontal bar chart
            chart_data = input_data.T.reset_index()
            chart_data.columns = ['Feature', 'Value']
            fig = px.bar(chart_data, 
                        x='Value',           
                        y='Feature',        
                        orientation='h',     
                        title="🩺 Your Lab Results",
                        color='Value',
                        color_continuous_scale='RdYlGn_r')
            
            fig.update_layout(
                width=800,           
                height=500,            
                margin=dict(l=120, r=20, t=50, b=20),  
                xaxis_title="Value", yaxis_title="Features",
                showlegend=False,
                font={'family': 'Arial', 'size': 12}
            )
            fig.update_traces(marker_line_width=0)
            
            st.plotly_chart(fig, use_container_width=False)  


# Clean footer
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns([1,2,1])
with col_f2:
    st.markdown("<p style='text-align: center; color: #757575; font-size: 0.85rem;'>GFGBQ-Team-GKV-P | PIMA Indians Diabetes Dataset | Clinical AI Tool</p>", unsafe_allow_html=True)
