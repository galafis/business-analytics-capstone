#!/usr/bin/env python3
"""
Business Analytics Dashboard - Wharton Capstone Project
Comprehensive Business Intelligence Platform
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import sqlite3
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BusinessAnalyticsDashboard:
    """Comprehensive Business Analytics Dashboard"""
    
    def __init__(self):
        self.db_path = "business_analytics.db"
        self.init_database()
        logger.info("Business Analytics Dashboard initialized")
    
    def init_database(self):
        """Initialize business analytics database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Customer analytics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer_analytics (
                customer_id TEXT PRIMARY KEY,
                acquisition_cost DECIMAL(10,2),
                lifetime_value DECIMAL(10,2),
                churn_probability DECIMAL(3,2),
                segment TEXT,
                satisfaction_score DECIMAL(3,2)
            )
        """)
        
        # Operations analytics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS operations_analytics (
                operation_id TEXT PRIMARY KEY,
                process_name TEXT,
                efficiency_score DECIMAL(3,2),
                cost DECIMAL(10,2),
                duration_hours DECIMAL(5,2),
                quality_score DECIMAL(3,2)
            )
        """)
        
        # People analytics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS people_analytics (
                employee_id TEXT PRIMARY KEY,
                department TEXT,
                performance_score DECIMAL(3,2),
                engagement_score DECIMAL(3,2),
                retention_risk DECIMAL(3,2),
                training_hours INTEGER
            )
        """)
        
        # Accounting analytics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounting_analytics (
                account_id TEXT PRIMARY KEY,
                account_type TEXT,
                balance DECIMAL(15,2),
                variance_percent DECIMAL(5,2),
                risk_level TEXT,
                last_audit_date DATE
            )
        """)
        
        conn.commit()
        conn.close()
        logger.info("Business analytics database initialized")
    
    def generate_comprehensive_data(self):
        """Generate comprehensive business analytics data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Clear existing data
        cursor.execute("DELETE FROM customer_analytics")
        cursor.execute("DELETE FROM operations_analytics")
        cursor.execute("DELETE FROM people_analytics")
        cursor.execute("DELETE FROM accounting_analytics")
        
        # Customer Analytics Data
        customers = []
        segments = ['Premium', 'Standard', 'Basic']
        for i in range(2000):
            customer_id = f"CUST_{i+1:05d}"
            acquisition_cost = np.random.uniform(50, 500)
            lifetime_value = np.random.uniform(500, 5000)
            churn_probability = np.random.uniform(0.05, 0.30)
            segment = np.random.choice(segments, p=[0.2, 0.5, 0.3])
            satisfaction_score = np.random.uniform(3.0, 5.0)
            
            customers.append((customer_id, acquisition_cost, lifetime_value, 
                            churn_probability, segment, satisfaction_score))
        
        cursor.executemany("""
            INSERT INTO customer_analytics 
            (customer_id, acquisition_cost, lifetime_value, churn_probability, segment, satisfaction_score)
            VALUES (?, ?, ?, ?, ?, ?)
        """, customers)
        
        # Operations Analytics Data
        operations = []
        processes = ['Manufacturing', 'Logistics', 'Quality Control', 'Procurement', 'Distribution']
        for i in range(500):
            operation_id = f"OP_{i+1:04d}"
            process_name = np.random.choice(processes)
            efficiency_score = np.random.uniform(0.6, 1.0)
            cost = np.random.uniform(1000, 50000)
            duration_hours = np.random.uniform(1, 48)
            quality_score = np.random.uniform(0.7, 1.0)
            
            operations.append((operation_id, process_name, efficiency_score, 
                             cost, duration_hours, quality_score))
        
        cursor.executemany("""
            INSERT INTO operations_analytics 
            (operation_id, process_name, efficiency_score, cost, duration_hours, quality_score)
            VALUES (?, ?, ?, ?, ?, ?)
        """, operations)
        
        # People Analytics Data
        employees = []
        departments = ['Sales', 'Marketing', 'Engineering', 'HR', 'Finance', 'Operations']
        for i in range(300):
            employee_id = f"EMP_{i+1:04d}"
            department = np.random.choice(departments)
            performance_score = np.random.uniform(0.6, 1.0)
            engagement_score = np.random.uniform(0.5, 1.0)
            retention_risk = np.random.uniform(0.1, 0.4)
            training_hours = np.random.randint(10, 100)
            
            employees.append((employee_id, department, performance_score, 
                            engagement_score, retention_risk, training_hours))
        
        cursor.executemany("""
            INSERT INTO people_analytics 
            (employee_id, department, performance_score, engagement_score, retention_risk, training_hours)
            VALUES (?, ?, ?, ?, ?, ?)
        """, employees)
        
        # Accounting Analytics Data
        accounts = []
        account_types = ['Assets', 'Liabilities', 'Equity', 'Revenue', 'Expenses']
        risk_levels = ['Low', 'Medium', 'High']
        for i in range(100):
            account_id = f"ACC_{i+1:04d}"
            account_type = np.random.choice(account_types)
            balance = np.random.uniform(-100000, 1000000)
            variance_percent = np.random.uniform(-15, 15)
            risk_level = np.random.choice(risk_levels, p=[0.6, 0.3, 0.1])
            last_audit_date = datetime.now() - timedelta(days=np.random.randint(1, 365))
            
            accounts.append((account_id, account_type, balance, variance_percent, 
                           risk_level, last_audit_date.date()))
        
        cursor.executemany("""
            INSERT INTO accounting_analytics 
            (account_id, account_type, balance, variance_percent, risk_level, last_audit_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, accounts)
        
        conn.commit()
        conn.close()
        logger.info("Generated comprehensive business analytics data")

def create_dashboard():
    """Create comprehensive business analytics dashboard"""
    st.set_page_config(
        page_title="Business Analytics Dashboard",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 Business Analytics Dashboard")
    st.markdown("*Wharton Business Analytics Capstone Project*")
    st.markdown("---")
    
    # Initialize dashboard
    dashboard = BusinessAnalyticsDashboard()
    
    # Sidebar
    st.sidebar.title("🔧 Dashboard Controls")
    
    if st.sidebar.button("🔄 Generate Sample Data"):
        with st.spinner("Generating business analytics data..."):
            dashboard.generate_comprehensive_data()
        st.sidebar.success("Data generated successfully!")
        st.experimental_rerun()
    
    # Analytics modules
    analytics_module = st.sidebar.selectbox(
        "Select Analytics Module",
        ["Overview", "Customer Analytics", "Operations Analytics", "People Analytics", "Accounting Analytics"]
    )
    
    if analytics_module == "Overview":
        show_overview_dashboard(dashboard)
    elif analytics_module == "Customer Analytics":
        show_customer_analytics(dashboard)
    elif analytics_module == "Operations Analytics":
        show_operations_analytics(dashboard)
    elif analytics_module == "People Analytics":
        show_people_analytics(dashboard)
    elif analytics_module == "Accounting Analytics":
        show_accounting_analytics(dashboard)

def show_overview_dashboard(dashboard):
    """Show overview dashboard"""
    st.subheader("📈 Business Overview Dashboard")
    
    # Load all data
    conn = sqlite3.connect(dashboard.db_path)
    
    try:
        customer_df = pd.read_sql_query("SELECT * FROM customer_analytics", conn)
        operations_df = pd.read_sql_query("SELECT * FROM operations_analytics", conn)
        people_df = pd.read_sql_query("SELECT * FROM people_analytics", conn)
        accounting_df = pd.read_sql_query("SELECT * FROM accounting_analytics", conn)
    except:
        st.warning("No data available. Please generate sample data.")
        return
    finally:
        conn.close()
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_customers = len(customer_df)
        avg_clv = customer_df['lifetime_value'].mean() if not customer_df.empty else 0
        st.metric("Total Customers", f"{total_customers:,}")
        st.metric("Avg Customer LTV", f"${avg_clv:,.2f}")
    
    with col2:
        total_operations = len(operations_df)
        avg_efficiency = operations_df['efficiency_score'].mean() if not operations_df.empty else 0
        st.metric("Active Operations", f"{total_operations:,}")
        st.metric("Avg Efficiency", f"{avg_efficiency:.1%}")
    
    with col3:
        total_employees = len(people_df)
        avg_performance = people_df['performance_score'].mean() if not people_df.empty else 0
        st.metric("Total Employees", f"{total_employees:,}")
        st.metric("Avg Performance", f"{avg_performance:.1%}")
    
    with col4:
        total_balance = accounting_df['balance'].sum() if not accounting_df.empty else 0
        st.metric("Total Balance", f"${total_balance:,.2f}")

def show_customer_analytics(dashboard):
    """Show customer analytics"""
    st.subheader("👥 Customer Analytics")
    
    conn = sqlite3.connect(dashboard.db_path)
    try:
        df = pd.read_sql_query("SELECT * FROM customer_analytics", conn)
    except:
        st.warning("No customer data available.")
        return
    finally:
        conn.close()
    
    if df.empty:
        st.warning("No customer data available.")
        return
    
    # Customer metrics
    col1, col2 = st.columns(2)
    
    with col1:
        # CLV by segment
        clv_by_segment = df.groupby('segment')['lifetime_value'].mean()
        fig_clv = px.bar(
            x=clv_by_segment.index,
            y=clv_by_segment.values,
            title="Average Customer Lifetime Value by Segment"
        )
        st.plotly_chart(fig_clv, use_container_width=True)
    
    with col2:
        # Churn risk distribution
        fig_churn = px.histogram(
            df,
            x='churn_probability',
            title="Churn Probability Distribution",
            nbins=20
        )
        st.plotly_chart(fig_churn, use_container_width=True)

def show_operations_analytics(dashboard):
    """Show operations analytics"""
    st.subheader("⚙️ Operations Analytics")
    
    conn = sqlite3.connect(dashboard.db_path)
    try:
        df = pd.read_sql_query("SELECT * FROM operations_analytics", conn)
    except:
        st.warning("No operations data available.")
        return
    finally:
        conn.close()
    
    if df.empty:
        st.warning("No operations data available.")
        return
    
    # Operations metrics
    col1, col2 = st.columns(2)
    
    with col1:
        # Efficiency by process
        efficiency_by_process = df.groupby('process_name')['efficiency_score'].mean()
        fig_efficiency = px.bar(
            x=efficiency_by_process.index,
            y=efficiency_by_process.values,
            title="Average Efficiency by Process"
        )
        st.plotly_chart(fig_efficiency, use_container_width=True)
    
    with col2:
        # Cost vs Quality
        fig_cost_quality = px.scatter(
            df,
            x='cost',
            y='quality_score',
            color='process_name',
            title="Cost vs Quality Score"
        )
        st.plotly_chart(fig_cost_quality, use_container_width=True)

def show_people_analytics(dashboard):
    """Show people analytics"""
    st.subheader("👨‍💼 People Analytics")
    
    conn = sqlite3.connect(dashboard.db_path)
    try:
        df = pd.read_sql_query("SELECT * FROM people_analytics", conn)
    except:
        st.warning("No people data available.")
        return
    finally:
        conn.close()
    
    if df.empty:
        st.warning("No people data available.")
        return
    
    # People metrics
    col1, col2 = st.columns(2)
    
    with col1:
        # Performance by department
        perf_by_dept = df.groupby('department')['performance_score'].mean()
        fig_perf = px.bar(
            x=perf_by_dept.index,
            y=perf_by_dept.values,
            title="Average Performance by Department"
        )
        st.plotly_chart(fig_perf, use_container_width=True)
    
    with col2:
        # Engagement vs Retention Risk
        fig_engagement = px.scatter(
            df,
            x='engagement_score',
            y='retention_risk',
            color='department',
            title="Engagement vs Retention Risk"
        )
        st.plotly_chart(fig_engagement, use_container_width=True)

def show_accounting_analytics(dashboard):
    """Show accounting analytics"""
    st.subheader("💰 Accounting Analytics")
    
    conn = sqlite3.connect(dashboard.db_path)
    try:
        df = pd.read_sql_query("SELECT * FROM accounting_analytics", conn)
    except:
        st.warning("No accounting data available.")
        return
    finally:
        conn.close()
    
    if df.empty:
        st.warning("No accounting data available.")
        return
    
    # Accounting metrics
    col1, col2 = st.columns(2)
    
    with col1:
        # Balance by account type
        balance_by_type = df.groupby('account_type')['balance'].sum()
        fig_balance = px.bar(
            x=balance_by_type.index,
            y=balance_by_type.values,
            title="Total Balance by Account Type"
        )
        st.plotly_chart(fig_balance, use_container_width=True)
    
    with col2:
        # Risk level distribution
        risk_counts = df['risk_level'].value_counts()
        fig_risk = px.pie(
            values=risk_counts.values,
            names=risk_counts.index,
            title="Risk Level Distribution"
        )
        st.plotly_chart(fig_risk, use_container_width=True)

def main():
    """Main application entry point"""
    create_dashboard()

if __name__ == "__main__":
    main()
