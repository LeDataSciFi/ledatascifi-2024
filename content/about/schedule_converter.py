import pandas as pd
import numpy as np
import os

df = pd.read_excel('Schedule.xlsx',sheet_name='Overall')
df['Date'] = pd.to_datetime(df['Date'])

df.columns

# get the dates starting at the most recent Sunday and going 3 weeks forward

# date of most recent Sunday (including today)
from datetime import datetime, timedelta
today = datetime.now()
days_to_subtract = (today.weekday() + 1) % 7
most_recent_sunday = today - timedelta(days=days_to_subtract)
# make most recent sunday at midnight
most_recent_sunday = datetime(most_recent_sunday.year, most_recent_sunday.month, most_recent_sunday.day)
date_after_21_days = most_recent_sunday + timedelta(days=21)

#########################################
# tasks pane 
#########################################

# find the task rows for this time period, including the blank rows 

rows = df.query('Hbool in ["Tasks", "ASGN"] & (Date >= @most_recent_sunday) & (Date <= @date_after_21_days)')

# Start building the HTML table string with inline styles for padding
table_md = """
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
"""

# Adding header with bold and underline using HTML, with inline styles if needed
for column in ['Due By', 'Task']:
    table_md += f'<th style="border: 1px solid black; padding: 10px; background-color: #f2f2f2;"><strong><u>{column}</u></strong></th>\n'

table_md += "</tr>\n</thead>\n<tbody>\n"

# Assuming 'rows' is your DataFrame
# Sample DataFrame iteration (adapt or replace placeholders as needed)
for index, row in rows.iterrows():
    
    if pd.notnull(row['Hyperlink']) and row['Hyperlink'] != '':
        # If "ASGN", format with hyperlink and styling
        if row['Hbool'] == "ASGN":
            task_or_topic = f"<a href='{row['Hyperlink']}' style='color: red;'><strong>{row['Task or Topic']}</strong></a>"
        else:  # Non-"ASGN" with hyperlink
            task_or_topic = f"<a href='{row['Hyperlink']}'>{row['Task or Topic']}</a>"
    else:
        task_or_topic = row['Task or Topic']
        
    if row['Hbool'] == "ASGN":
        table_md += f"<tr><td style='border: 1px solid black; padding: 10px; color: red;'><strong>{row['Date'].strftime('%b %d')}</strong></td><td style='border: 1px solid black; padding: 10px; color: red;'><strong>{task_or_topic}</strong></td></tr>\n"
    else:
        table_md += f"<tr><td style='border: 1px solid black; padding: 10px;'>{row['Date'].strftime('%b %d')}</td><td style='border: 1px solid black; padding: 10px;'>{task_or_topic}</td></tr>\n"

table_md += "</tbody>\n</table>"

# You can write table_md to a markdown file as needed
with open('tasks.html', 'w') as file:
    file.write(table_md)



#########################################
# class pane 
#########################################

# find the task rows for this time period, including the blank rows 

rows = df.query('Hbool in ["Lecture"] & (Date >= @most_recent_sunday) & (Date <= @date_after_21_days)')

# Start building the HTML table string with inline styles for padding
table_md = """
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
"""

# Adding header with bold and underline using HTML, with inline styles if needed
for column in ['Date', 'Class']:
    table_md += f'<th style="border: 1px solid black; padding: 10px; background-color: #f2f2f2;"><strong><u>{column}</u></strong></th>\n'

table_md += "</tr>\n</thead>\n<tbody>\n"

# Assuming 'rows' is your DataFrame
# Sample DataFrame iteration (adapt or replace placeholders as needed)
for index, row in rows.iterrows():
    if row['Hbool'] == "ASGN":
        table_md += f"<tr><td style='border: 1px solid black; padding: 10px; color: red;'><strong>{row['Date'].strftime('%b %d')}</strong></td><td style='border: 1px solid black; padding: 10px; color: red;'><strong>{row['Task or Topic']}</strong></td></tr>\n"
    else:
        table_md += f"<tr><td style='border: 1px solid black; padding: 10px;'>{row['Date'].strftime('%b %d')}</td><td style='border: 1px solid black; padding: 10px;'>{row['Task or Topic']}</td></tr>\n"

table_md += "</tbody>\n</table>"

# You can write table_md to a markdown file as needed
with open('classes.html', 'w') as file:
    file.write(table_md)
    

#########################################
# past tasks pane 
#########################################

# find the task rows for this time period, including the blank rows 

rows = df.query('Hbool in ["Tasks", "ASGN"] & (Date < @most_recent_sunday) ')
rows = rows.sort_values('Date',ascending=False)

# Start building the HTML table string with inline styles for padding
table_md = """
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
"""

# Adding header with bold and underline using HTML, with inline styles if needed
for column in ['Due By', 'Task']:
    table_md += f'<th style="border: 1px solid black; padding: 10px; background-color: #f2f2f2;"><strong><u>{column}</u></strong></th>\n'

table_md += "</tr>\n</thead>\n<tbody>\n"

# Assuming 'rows' is your DataFrame
# Sample DataFrame iteration (adapt or replace placeholders as needed)
for index, row in rows.iterrows():
    if row['Hbool'] == "ASGN":
        table_md += f"<tr><td style='border: 1px solid black; padding: 10px; color: red;'><strong>{row['Date'].strftime('%b %d')}</strong></td><td style='border: 1px solid black; padding: 10px; color: red;'><strong>{row['Task or Topic']}</strong></td></tr>\n"
    else:
        table_md += f"<tr><td style='border: 1px solid black; padding: 10px;'>{row['Date'].strftime('%b %d')}</td><td style='border: 1px solid black; padding: 10px;'>{row['Task or Topic']}</td></tr>\n"

table_md += "</tbody>\n</table>"

# You can write table_md to a markdown file as needed
with open('past_tasks.html', 'w') as file:
    file.write(table_md)



#########################################
# big pic pane 
#########################################

# find the task rows for this time period, including the blank rows 

rows = df.query('Hbool in ["Header", "Extra-Header"]')
rows['Header']

# Start building the HTML table string
table_html = "<table>\n"

# Add a header or adjust as needed. For simplicity, no header is added here.

for index, row in rows.iterrows():
    content = row['Header']
    if pd.isna(content):
        # Blank row for NaN
        table_html += "<tr><td style='height: 20px;'></td></tr>\n"
    elif str(content).startswith("MODULE"):
        # Bold and underline for rows starting with "MODULE"
        table_html += f"<tr><td><strong><u>{content}</u></strong></td></tr>\n"
    else:
        # Italics for other rows
        table_html += f"<tr><td><em>{content}</em></td></tr>\n"

table_html += "</table>"

# You can write table_md to a markdown file as needed
with open('big_pic.html', 'w') as file:
    file.write(table_html)
    
