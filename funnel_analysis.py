import pandas as pd
import plotly.express as px

# 1. Create Mock Data (Simulating Company X)
data = {
    'Stage': ['Website Visit', 'Sign Up', 'Complete Onboarding', 'Active Usage', 'Subscription'],
    'Users': [10000, 4500, 1800, 1200, 600]
}

df = pd.DataFrame(data)

# 2. Calculate Drop-off and Conversion Rates
df['Retention_Rate'] = (df['Users'] / df['Users'].iloc[0] * 100).round(2)
df['Drop_off_from_Previous'] = (1 - (df['Users'] / df.shift(1)['Users'])) * 100

# 3. Create a Professional Funnel Visualization
fig = px.funnel(df, x='Users', y='Stage', 
                title='SaaS Trial-to-Paid Conversion Funnel',
                color_discrete_sequence=['#636EFA'])

fig.update_traces(textinfo="value+percent initial")
fig.show()

# 4. Print Summary for the README
print(df)
