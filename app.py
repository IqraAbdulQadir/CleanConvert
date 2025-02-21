import streamlit as st #python library for UI
import pandas as pd #python library for data
import os #python library for file operations
from io import BytesIO #module for input /output operations
from datetime import datetime #module for date and time operations

# Set up my App
st.set_page_config(page_title="CleanConvert", layout='wide')
st.title("Clean Convert")
st.write("Easily clean, convert, and visualize your data with seamless CSV and Excel transformations!")

# A closable sidebar to try better UI
st.sidebar.header("Settings")
#File Uploader
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)
st.sidebar.write(f"📂 {len(uploaded_files)} file(s) uploaded") #len used to display number of files

#conditions to read files
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower() #get file extension in lower case
        
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"File type not supported: {file_ext}") #Will never show up.
            continue
        
        # Display file details
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB") #Rounds to 2 decimal places

        # Shows data preview
        st.write("**Preview your first five columns of data!**")
        st.write(df.head())
        
        # Shows Data Summary
        if st.checkbox("Show Data Summary"):
            st.write(df.describe())
        
        # Data Cleaning Options
        with st.expander("🔧 Data Cleaning Options"):
            duplicates = df.duplicated().sum()
            st.write(f"🔍 Found {duplicates} duplicate rows")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")
            
            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values filled!")
        
        # Column Selection
        with st.expander("📊 Select Columns to Keep"):
            columns = st.multiselect("Choose Columns", df.columns, default=df.columns)
            df = df[columns]
        
        # Data Visualization
        with st.expander("📈 Data Visualization"):
            if st.checkbox(f"Show Visualization for {file.name}"):
                st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])
        
        # File Conversion Options
        with st.expander("🔄 Conversion Options"):
            conversion_type = st.selectbox("Convert to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = f"data_{timestamp}.csv"
                    mime_type = "text/csv"
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False)
                    file_name = f"data_{timestamp}.xlsx"
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                
                buffer.seek(0)
                st.download_button(label=f"Download {file_name}", data=buffer, file_name=file_name, mime=mime_type)
                st.success(f"🎉 {file_name} successfully downloaded!")

st.success("✅ All files processed!")
