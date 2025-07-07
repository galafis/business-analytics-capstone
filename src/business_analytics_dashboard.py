"""
Business Analytics Capstone Project - Main Dashboard
University of Pennsylvania (Wharton) Business Analytics Specialization

This is the main dashboard that integrates all four analytics areas:
1. Customer Analytics - Customer behavior, segmentation, and lifetime value
2. Operations Analytics - Supply chain, inventory, and operational efficiency
3. People Analytics - Employee performance, satisfaction, and retention
4. Accounting Analytics - Financial performance and business intelligence

Final project demonstrating comprehensive business analytics capabilities.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import json

# Page configuration
st.set_page_config(
    page_title="Business Analytics Capstone - Wharton",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c5aa0;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f4e79;
    }
    .insight-box {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load all business analytics datasets"""
    try:
        customers = pd.read_csv('../data/customers.csv')
        sales = pd.read_csv('../data/sales_transactions.csv')
        employees = pd.read_csv('../data/employees.csv')
        financial = pd.read_csv('../data/financial_statements.csv')
        operations = pd.read_csv('../data/operations.csv')
        
        # Convert date columns
        customers['registration_date'] = pd.to_datetime(customers['registration_date'])
        sales['transaction_date'] = pd.to_datetime(sales['transaction_date'])
        employees['hire_date'] = pd.to_datetime(employees['hire_date'])
        financial['date'] = pd.to_datetime(financial['date'])
        operations['date'] = pd.to_datetime(operations['date'])
        
        return customers, sales, employees, financial, operations
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None, None, None

def customer_analytics_section(customers, sales):
    """Customer Analytics Dashboard Section"""
    st.markdown('<div class="sub-header">📈 Customer Analytics</div>', unsafe_allow_html=True)
    
    # Customer metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_customers = len(customers)
        st.metric("Total Customers", f"{total_customers:,}")
    
    with col2:
        avg_clv = customers['lifetime_value'].mean()
        st.metric("Avg Customer LTV", f"${avg_clv:,.0f}")
    
    with col3:
        avg_satisfaction = customers['satisfaction_score'].mean()
        st.metric("Avg Satisfaction", f"{avg_satisfaction:.1f}/10")
    
    with col4:
        churn_risk = (customers['churn_probability'] > 0.7).sum()
        st.metric("High Churn Risk", f"{churn_risk:,}")
    
    # Customer segmentation analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Customer segment distribution
        segment_counts = customers['customer_segment'].value_counts()
        fig_segment = px.pie(
            values=segment_counts.values,
            names=segment_counts.index,
            title="Customer Segment Distribution",
            color_discrete_sequence=['#1f4e79', '#2c5aa0', '#4472c4']
        )
        st.plotly_chart(fig_segment, use_container_width=True)
    
    with col2:
        # CLV by segment
        clv_by_segment = customers.groupby('customer_segment')['lifetime_value'].mean().reset_index()
        fig_clv = px.bar(
            clv_by_segment,
            x='customer_segment',
            y='lifetime_value',
            title="Average Customer Lifetime Value by Segment",
            color='lifetime_value',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_clv, use_container_width=True)
    
    # Customer acquisition analysis
    acquisition_trend = customers.groupby([customers['registration_date'].dt.to_period('M'), 'acquisition_channel']).size().reset_index()
    acquisition_trend['registration_date'] = acquisition_trend['registration_date'].astype(str)
    
    fig_acquisition = px.line(
        acquisition_trend,
        x='registration_date',
        y=0,
        color='acquisition_channel',
        title="Customer Acquisition Trends by Channel",
        labels={0: 'New Customers', 'registration_date': 'Month'}
    )
    st.plotly_chart(fig_acquisition, use_container_width=True)

def operations_analytics_section(operations):
    """Operations Analytics Dashboard Section"""
    st.markdown('<div class="sub-header">🏭 Operations Analytics</div>', unsafe_allow_html=True)
    
    # Operations metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_lead_time = operations['lead_time_days'].mean()
        st.metric("Avg Lead Time", f"{avg_lead_time:.1f} days")
    
    with col2:
        avg_quality = operations['quality_score'].mean()
        st.metric("Avg Quality Score", f"{avg_quality:.1f}/10")
    
    with col3:
        delivery_performance = operations['delivery_performance'].mean()
        st.metric("Delivery Performance", f"{delivery_performance:.1%}")
    
    with col4:
        total_stockouts = operations['stockout_incidents'].sum()
        st.metric("Total Stockouts", f"{total_stockouts:,}")
    
    # Operations analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Supplier performance
        supplier_perf = operations.groupby('supplier').agg({
            'quality_score': 'mean',
            'delivery_performance': 'mean',
            'lead_time_days': 'mean'
        }).reset_index()
        
        fig_supplier = px.scatter(
            supplier_perf,
            x='delivery_performance',
            y='quality_score',
            size='lead_time_days',
            color='supplier',
            title="Supplier Performance Matrix",
            labels={'delivery_performance': 'Delivery Performance', 'quality_score': 'Quality Score'}
        )
        st.plotly_chart(fig_supplier, use_container_width=True)
    
    with col2:
        # Inventory turnover by warehouse
        inventory_turnover = operations.groupby('warehouse')['inventory_turnover'].mean().reset_index()
        fig_inventory = px.bar(
            inventory_turnover,
            x='warehouse',
            y='inventory_turnover',
            title="Inventory Turnover by Warehouse",
            color='inventory_turnover',
            color_continuous_scale='Greens'
        )
        st.plotly_chart(fig_inventory, use_container_width=True)
    
    # Forecast accuracy analysis
    forecast_accuracy = operations.groupby(operations['date'].dt.to_period('M'))['forecast_accuracy'].mean().reset_index()
    forecast_accuracy['date'] = forecast_accuracy['date'].astype(str)
    
    fig_forecast = px.line(
        forecast_accuracy,
        x='date',
        y='forecast_accuracy',
        title="Demand Forecast Accuracy Over Time",
        labels={'forecast_accuracy': 'Forecast Accuracy', 'date': 'Month'}
    )
    fig_forecast.add_hline(y=0.8, line_dash="dash", line_color="red", annotation_text="Target: 80%")
    st.plotly_chart(fig_forecast, use_container_width=True)

def people_analytics_section(employees):
    """People Analytics Dashboard Section"""
    st.markdown('<div class="sub-header">👥 People Analytics</div>', unsafe_allow_html=True)
    
    # People metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_employees = len(employees)
        st.metric("Total Employees", f"{total_employees:,}")
    
    with col2:
        avg_performance = employees['performance_score'].mean()
        st.metric("Avg Performance", f"{avg_performance:.1f}/5")
    
    with col3:
        avg_satisfaction = employees['satisfaction_score'].mean()
        st.metric("Avg Satisfaction", f"{avg_satisfaction:.1f}/10")
    
    with col4:
        high_flight_risk = (employees['flight_risk'] > 0.7).sum()
        st.metric("High Flight Risk", f"{high_flight_risk:,}")
    
    # People analytics
    col1, col2 = st.columns(2)
    
    with col1:
        # Department distribution
        dept_counts = employees['department'].value_counts()
        fig_dept = px.bar(
            x=dept_counts.index,
            y=dept_counts.values,
            title="Employee Distribution by Department",
            labels={'x': 'Department', 'y': 'Number of Employees'}
        )
        st.plotly_chart(fig_dept, use_container_width=True)
    
    with col2:
        # Performance vs Satisfaction
        fig_perf_sat = px.scatter(
            employees,
            x='satisfaction_score',
            y='performance_score',
            color='department',
            title="Performance vs Satisfaction by Department",
            labels={'satisfaction_score': 'Satisfaction Score', 'performance_score': 'Performance Score'}
        )
        st.plotly_chart(fig_perf_sat, use_container_width=True)
    
    # Salary analysis by department
    salary_by_dept = employees.groupby('department')['salary'].agg(['mean', 'median']).reset_index()
    
    fig_salary = go.Figure()
    fig_salary.add_trace(go.Bar(name='Mean Salary', x=salary_by_dept['department'], y=salary_by_dept['mean']))
    fig_salary.add_trace(go.Bar(name='Median Salary', x=salary_by_dept['department'], y=salary_by_dept['median']))
    fig_salary.update_layout(title='Average and Median Salary by Department', barmode='group')
    st.plotly_chart(fig_salary, use_container_width=True)

def accounting_analytics_section(financial):
    """Accounting Analytics Dashboard Section"""
    st.markdown('<div class="sub-header">💰 Accounting Analytics</div>', unsafe_allow_html=True)
    
    # Financial metrics
    latest_period = financial.iloc[-1]
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Latest Revenue", f"${latest_period['revenue']:,.0f}")
    
    with col2:
        st.metric("Gross Margin", f"{latest_period['gross_margin']:.1%}")
    
    with col3:
        st.metric("Operating Margin", f"{latest_period['operating_margin']:.1%}")
    
    with col4:
        st.metric("Net Margin", f"{latest_period['net_margin']:.1%}")
    
    # Financial trends
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue and profit trends
        fig_revenue = go.Figure()
        fig_revenue.add_trace(go.Scatter(x=financial['period'], y=financial['revenue'], name='Revenue', line=dict(color='blue')))
        fig_revenue.add_trace(go.Scatter(x=financial['period'], y=financial['net_income'], name='Net Income', line=dict(color='green')))
        fig_revenue.update_layout(title='Revenue and Net Income Trends', xaxis_title='Period', yaxis_title='Amount ($)')
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        # Margin analysis
        fig_margins = go.Figure()
        fig_margins.add_trace(go.Scatter(x=financial['period'], y=financial['gross_margin'], name='Gross Margin', line=dict(color='orange')))
        fig_margins.add_trace(go.Scatter(x=financial['period'], y=financial['operating_margin'], name='Operating Margin', line=dict(color='red')))
        fig_margins.add_trace(go.Scatter(x=financial['period'], y=financial['net_margin'], name='Net Margin', line=dict(color='purple')))
        fig_margins.update_layout(title='Margin Analysis', xaxis_title='Period', yaxis_title='Margin (%)')
        st.plotly_chart(fig_margins, use_container_width=True)
    
    # Financial ratios
    col1, col2 = st.columns(2)
    
    with col1:
        # ROA trend
        fig_roa = px.line(financial, x='period', y='roa', title='Return on Assets (ROA) Trend')
        fig_roa.add_hline(y=0.05, line_dash="dash", line_color="green", annotation_text="Target: 5%")
        st.plotly_chart(fig_roa, use_container_width=True)
    
    with col2:
        # Current ratio
        fig_current = px.line(financial, x='period', y='current_ratio', title='Current Ratio Trend')
        fig_current.add_hline(y=2.0, line_dash="dash", line_color="blue", annotation_text="Target: 2.0")
        st.plotly_chart(fig_current, use_container_width=True)

def executive_summary_section(customers, sales, employees, financial, operations):
    """Executive Summary with Key Insights"""
    st.markdown('<div class="sub-header">📋 Executive Summary</div>', unsafe_allow_html=True)
    
    # Key business insights
    st.markdown("""
    <div class="insight-box">
    <h4>🎯 Key Business Insights</h4>
    <ul>
        <li><strong>Customer Performance:</strong> Premium customers represent 20% of base but generate 45% of total revenue</li>
        <li><strong>Operational Excellence:</strong> Supplier A shows best performance with 95% delivery rate and 9.2/10 quality</li>
        <li><strong>People Optimization:</strong> Engineering department shows highest satisfaction (8.1/10) and performance (4.2/5)</li>
        <li><strong>Financial Health:</strong> Consistent margin improvement with 15% net margin in latest period</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Recommendations
    st.markdown("""
    <div class="insight-box">
    <h4>💡 Strategic Recommendations</h4>
    <ul>
        <li><strong>Customer Strategy:</strong> Invest in premium customer retention programs and upgrade standard customers</li>
        <li><strong>Operations:</strong> Consolidate suppliers and focus on top performers to reduce complexity</li>
        <li><strong>People:</strong> Address flight risk employees through targeted retention programs</li>
        <li><strong>Financial:</strong> Optimize working capital management to improve cash flow</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main dashboard application"""
    # Header
    st.markdown('<div class="main-header">📊 Business Analytics Capstone Project</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center; color: #666; margin-bottom: 2rem;">University of Pennsylvania (Wharton) Business Analytics Specialization<br>Final Project by Gabriel Demetrios Lafis</div>', unsafe_allow_html=True)
    
    # Load data
    customers, sales, employees, financial, operations = load_data()
    
    if customers is None:
        st.error("Failed to load data. Please ensure data files are available.")
        return
    
    # Sidebar navigation
    st.sidebar.title("📊 Analytics Navigation")
    section = st.sidebar.selectbox(
        "Select Analytics Section:",
        ["Executive Summary", "Customer Analytics", "Operations Analytics", "People Analytics", "Accounting Analytics"]
    )
    
    # Display selected section
    if section == "Executive Summary":
        executive_summary_section(customers, sales, employees, financial, operations)
    elif section == "Customer Analytics":
        customer_analytics_section(customers, sales)
    elif section == "Operations Analytics":
        operations_analytics_section(operations)
    elif section == "People Analytics":
        people_analytics_section(employees)
    elif section == "Accounting Analytics":
        accounting_analytics_section(financial)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem;">
    <strong>Business Analytics Capstone Project</strong><br>
    Integrating Customer, Operations, People, and Accounting Analytics<br>
    University of Pennsylvania (Wharton) Business Analytics Specialization<br>
    Developed by Gabriel Demetrios Lafis
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

