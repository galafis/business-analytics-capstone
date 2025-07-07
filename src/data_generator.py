"""
Business Analytics Capstone Project - Data Generator
University of Pennsylvania (Wharton) Business Analytics Specialization

This module generates comprehensive business data for analytics including:
- Customer data with demographics and behavior
- Sales transactions and revenue data
- Employee performance and HR metrics
- Financial statements and accounting data
- Operations and supply chain metrics
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker
import json

fake = Faker()
np.random.seed(42)
random.seed(42)

class BusinessDataGenerator:
    def __init__(self):
        self.start_date = datetime(2022, 1, 1)
        self.end_date = datetime(2025, 6, 30)
        
    def generate_customer_data(self, n_customers=10000):
        """Generate customer analytics data"""
        customers = []
        
        for i in range(n_customers):
            customer = {
                'customer_id': f'CUST_{i+1:06d}',
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.email(),
                'age': np.random.randint(18, 80),
                'gender': np.random.choice(['M', 'F', 'Other'], p=[0.48, 0.48, 0.04]),
                'income': np.random.lognormal(10.5, 0.8),
                'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 
                                            p=[0.3, 0.4, 0.25, 0.05]),
                'city': fake.city(),
                'state': fake.state(),
                'country': fake.country(),
                'registration_date': fake.date_between(self.start_date, self.end_date),
                'customer_segment': np.random.choice(['Premium', 'Standard', 'Basic'], 
                                                   p=[0.2, 0.5, 0.3]),
                'lifetime_value': np.random.lognormal(7, 1),
                'churn_probability': np.random.beta(2, 8),
                'satisfaction_score': np.random.normal(7.5, 1.5),
                'acquisition_channel': np.random.choice(['Online', 'Referral', 'Social Media', 'Direct'], 
                                                      p=[0.4, 0.3, 0.2, 0.1])
            }
            customers.append(customer)
        
        return pd.DataFrame(customers)
    
    def generate_sales_data(self, n_transactions=50000):
        """Generate sales and revenue data"""
        transactions = []
        
        products = ['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E']
        categories = ['Electronics', 'Clothing', 'Home', 'Sports', 'Books']
        
        for i in range(n_transactions):
            transaction = {
                'transaction_id': f'TXN_{i+1:08d}',
                'customer_id': f'CUST_{np.random.randint(1, 10001):06d}',
                'product_id': np.random.choice(products),
                'category': np.random.choice(categories),
                'quantity': np.random.randint(1, 10),
                'unit_price': np.random.lognormal(3, 0.5),
                'discount': np.random.beta(1, 9) * 0.3,
                'transaction_date': fake.date_time_between(self.start_date, self.end_date),
                'sales_rep': fake.name(),
                'region': np.random.choice(['North', 'South', 'East', 'West']),
                'channel': np.random.choice(['Online', 'Store', 'Phone'], p=[0.6, 0.3, 0.1]),
                'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'Cash', 'PayPal'], 
                                                 p=[0.5, 0.3, 0.1, 0.1])
            }
            
            # Calculate derived fields
            transaction['gross_revenue'] = transaction['quantity'] * transaction['unit_price']
            transaction['net_revenue'] = transaction['gross_revenue'] * (1 - transaction['discount'])
            transaction['profit_margin'] = np.random.normal(0.25, 0.1)
            transaction['profit'] = transaction['net_revenue'] * transaction['profit_margin']
            
            transactions.append(transaction)
        
        return pd.DataFrame(transactions)
    
    def generate_employee_data(self, n_employees=1000):
        """Generate people analytics data"""
        employees = []
        
        departments = ['Sales', 'Marketing', 'Engineering', 'HR', 'Finance', 'Operations']
        positions = ['Manager', 'Senior', 'Junior', 'Intern', 'Director', 'VP']
        
        for i in range(n_employees):
            hire_date = fake.date_between(datetime(2020, 1, 1), datetime(2025, 1, 1))
            
            employee = {
                'employee_id': f'EMP_{i+1:05d}',
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.email(),
                'department': np.random.choice(departments),
                'position': np.random.choice(positions),
                'hire_date': hire_date,
                'salary': np.random.lognormal(10.8, 0.4),
                'performance_score': np.random.normal(3.5, 0.8),
                'satisfaction_score': np.random.normal(7, 1.5),
                'training_hours': np.random.poisson(40),
                'projects_completed': np.random.poisson(8),
                'absenteeism_days': np.random.poisson(5),
                'overtime_hours': np.random.exponential(10),
                'manager_id': f'EMP_{np.random.randint(1, min(100, i+1)):05d}' if i > 0 else None,
                'tenure_years': (datetime.now().date() - hire_date).days / 365.25,
                'promotion_eligible': np.random.choice([True, False], p=[0.3, 0.7]),
                'flight_risk': np.random.beta(2, 8)
            }
            employees.append(employee)
        
        return pd.DataFrame(employees)
    
    def generate_financial_data(self, n_periods=36):
        """Generate accounting analytics data"""
        financial_data = []
        
        base_date = datetime(2022, 1, 1)
        
        for i in range(n_periods):
            period_date = base_date + timedelta(days=30*i)
            
            # Generate monthly financial metrics
            revenue = np.random.lognormal(15, 0.2)
            cogs = revenue * np.random.uniform(0.4, 0.6)
            operating_expenses = revenue * np.random.uniform(0.2, 0.4)
            
            financial = {
                'period': period_date.strftime('%Y-%m'),
                'date': period_date,
                'revenue': revenue,
                'cost_of_goods_sold': cogs,
                'gross_profit': revenue - cogs,
                'operating_expenses': operating_expenses,
                'ebitda': revenue - cogs - operating_expenses,
                'depreciation': revenue * np.random.uniform(0.02, 0.05),
                'interest_expense': revenue * np.random.uniform(0.01, 0.03),
                'tax_rate': np.random.uniform(0.2, 0.3),
                'cash_flow': np.random.normal(revenue * 0.15, revenue * 0.05),
                'accounts_receivable': revenue * np.random.uniform(0.1, 0.2),
                'inventory': cogs * np.random.uniform(0.15, 0.25),
                'accounts_payable': cogs * np.random.uniform(0.08, 0.15),
                'working_capital': np.random.normal(revenue * 0.1, revenue * 0.03)
            }
            
            # Calculate derived metrics
            financial['gross_margin'] = financial['gross_profit'] / financial['revenue']
            financial['operating_margin'] = financial['ebitda'] / financial['revenue']
            financial['net_income'] = (financial['ebitda'] - financial['depreciation'] - 
                                     financial['interest_expense']) * (1 - financial['tax_rate'])
            financial['net_margin'] = financial['net_income'] / financial['revenue']
            financial['roa'] = financial['net_income'] / (revenue * 2)  # Simplified ROA
            financial['current_ratio'] = (financial['cash_flow'] + financial['accounts_receivable']) / financial['accounts_payable']
            
            financial_data.append(financial)
        
        return pd.DataFrame(financial_data)
    
    def generate_operations_data(self, n_records=5000):
        """Generate operations analytics data"""
        operations = []
        
        suppliers = ['Supplier_A', 'Supplier_B', 'Supplier_C', 'Supplier_D']
        warehouses = ['Warehouse_North', 'Warehouse_South', 'Warehouse_East', 'Warehouse_West']
        
        for i in range(n_records):
            operation = {
                'operation_id': f'OPS_{i+1:06d}',
                'date': fake.date_between(self.start_date, self.end_date),
                'supplier': np.random.choice(suppliers),
                'warehouse': np.random.choice(warehouses),
                'product_id': f'Product_{np.random.choice(["A", "B", "C", "D", "E"])}',
                'order_quantity': np.random.poisson(100),
                'received_quantity': lambda q: q - np.random.poisson(2),
                'lead_time_days': np.random.gamma(2, 3),
                'unit_cost': np.random.lognormal(2, 0.3),
                'quality_score': np.random.beta(8, 2) * 10,
                'delivery_performance': np.random.beta(7, 2),
                'inventory_turnover': np.random.gamma(3, 2),
                'stockout_incidents': np.random.poisson(0.5),
                'carrying_cost_rate': np.random.uniform(0.15, 0.25),
                'demand_forecast': np.random.lognormal(4, 0.5),
                'actual_demand': lambda f: f * np.random.normal(1, 0.2)
            }
            
            # Calculate derived fields
            operation['received_quantity'] = max(0, operation['order_quantity'] - np.random.poisson(2))
            operation['actual_demand'] = max(0, operation['demand_forecast'] * np.random.normal(1, 0.2))
            operation['forecast_accuracy'] = 1 - abs(operation['actual_demand'] - operation['demand_forecast']) / operation['demand_forecast']
            operation['total_cost'] = operation['received_quantity'] * operation['unit_cost']
            operation['carrying_cost'] = operation['total_cost'] * operation['carrying_cost_rate']
            
            operations.append(operation)
        
        return pd.DataFrame(operations)
    
    def generate_all_data(self):
        """Generate all business analytics datasets"""
        print("Generating comprehensive business analytics data...")
        
        # Generate all datasets
        customers_df = self.generate_customer_data()
        sales_df = self.generate_sales_data()
        employees_df = self.generate_employee_data()
        financial_df = self.generate_financial_data()
        operations_df = self.generate_operations_data()
        
        # Save to CSV files
        data_dir = '../data'
        customers_df.to_csv(f'{data_dir}/customers.csv', index=False)
        sales_df.to_csv(f'{data_dir}/sales_transactions.csv', index=False)
        employees_df.to_csv(f'{data_dir}/employees.csv', index=False)
        financial_df.to_csv(f'{data_dir}/financial_statements.csv', index=False)
        operations_df.to_csv(f'{data_dir}/operations.csv', index=False)
        
        # Generate summary statistics
        summary = {
            'generation_date': datetime.now().isoformat(),
            'datasets': {
                'customers': {
                    'records': len(customers_df),
                    'columns': list(customers_df.columns),
                    'date_range': f"{customers_df['registration_date'].min()} to {customers_df['registration_date'].max()}"
                },
                'sales': {
                    'records': len(sales_df),
                    'columns': list(sales_df.columns),
                    'total_revenue': float(sales_df['net_revenue'].sum()),
                    'date_range': f"{sales_df['transaction_date'].min()} to {sales_df['transaction_date'].max()}"
                },
                'employees': {
                    'records': len(employees_df),
                    'columns': list(employees_df.columns),
                    'departments': list(employees_df['department'].unique())
                },
                'financial': {
                    'records': len(financial_df),
                    'columns': list(financial_df.columns),
                    'period_range': f"{financial_df['period'].min()} to {financial_df['period'].max()}"
                },
                'operations': {
                    'records': len(operations_df),
                    'columns': list(operations_df.columns),
                    'suppliers': list(operations_df['supplier'].unique())
                }
            }
        }
        
        with open(f'{data_dir}/data_summary.json', 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        
        print(f"✅ Generated {len(customers_df):,} customer records")
        print(f"✅ Generated {len(sales_df):,} sales transactions")
        print(f"✅ Generated {len(employees_df):,} employee records")
        print(f"✅ Generated {len(financial_df):,} financial periods")
        print(f"✅ Generated {len(operations_df):,} operations records")
        print(f"✅ Total revenue: ${sales_df['net_revenue'].sum():,.2f}")
        print("✅ All data saved to ../data/ directory")
        
        return {
            'customers': customers_df,
            'sales': sales_df,
            'employees': employees_df,
            'financial': financial_df,
            'operations': operations_df
        }

if __name__ == "__main__":
    generator = BusinessDataGenerator()
    data = generator.generate_all_data()

