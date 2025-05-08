from PIL import Image, ImageOps
import streamlit as st
import base64

st.set_page_config(layout="centered")

#font size setting

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 20px !important;
    }

    [data-baseweb="tab"] button[aria-selected="true"] {
    color: #FF4B4B !important;
    border-bottom: 3px solid #FF4B4B !important;
    }
    </style>
""", unsafe_allow_html=True)

def get_base64_bg(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{data}"

bg_image = get_base64_bg("bg.jpg")  # or .png

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{bg_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

#st.markdown("<h3 style='text-align: center; font-size:24px;'>My Smaller Title</h3>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left;'>    Olivia Liuxin Pan </h1>", unsafe_allow_html=True)
#st.title("Olivia Pan | Personal Website")
st.write("""
**Email:** panliuxin010203@gmail.com  
**Phone Number:** 832-638-6723  
**Location:** Austin, TX  
**LinkedIn:** [https://linkedin.com/in/pan-olivia/](https://linkedin.com/in/pan-olivia/)  
**Legal Status:** US Citizen
""")
st.markdown("<br>", unsafe_allow_html=True)

#pics
col1, col2 = st.columns(2)

with col1:
    image1 = Image.open("olivia.jpg")
    image1 = ImageOps.exif_transpose(image1) 
    st.image(image1, width=600)

with col2:
    image2 = Image.open("olivia2.jpg")
    st.image(image2, width=500)

st.write("")

st.markdown("""
### 🗂️ Table of Contents
- [Education](#education)
- [Major Specific Experience](#experience)
- [Leaderships](#lea)
- [Competition](#comp)
- [Languages](#languages)
""", unsafe_allow_html=True)

st.markdown(
    "<hr style='border: 1.5px solid #FF7F50; margin: 40px 0;'>",
    unsafe_allow_html=True
)



st.markdown('<a name="education"></a>', unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left;'>Education</h3>", unsafe_allow_html=True)
st.markdown("""
    **The University of Texas at Austin**  
    *Bachelor of Science, double major in Statistics and Data Science & Economics*  
    GPA: 3.83  
    Expected graduation: May 2026
    """)
st.markdown('<a name="experience"></a>', unsafe_allow_html=True)

st.write("") 

st.write("") 
#resume
tab1, tab2 = st.tabs(["📄 Resume A: Statistics and Data Science Track Related", "📄 Resume B: Economics Track Related"])

# --- Tab 1 Content ---
with tab1:

    st.markdown("<h3 style='text-align: left;'>Project Experience</h2>", unsafe_allow_html=True)
    
    #proj1
    st.markdown("""
    **Time Series Forecasting Class Project** — *Team Leader*  
    _Feb 2025 – May 2025_  
    - Goal was to predict the house sales volume in each month in the UK based on past observations
    - Analyzed and seasonally adjusted time series data from 2010–2025 using ARIMA, GARCH, with pandemic effect taken care of; forecasted future patterns using R programming language
""")
    with open("proj_2.html", "r", encoding='utf-8') as f:
        html_content = f.read()
    with st.expander("🔽 R Code"):
        st.components.v1.html(html_content, height=500, scrolling=True)

    with open("proj_2_rep.pdf", "rb") as f:
        base64_pdf11 = base64.b64encode(f.read()).decode("utf-8")

# Generate HTML to embed the PDF in an iframe
    pdf_viewer = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf11}" width="100%" height="600" type="application/pdf"></iframe>
"""

# Add collapsible reader
    with st.expander("🔗 Project Report"):
        st.markdown(pdf_viewer, unsafe_allow_html=True)

    st.write("") 

    #proj 2
    st.markdown("""
    **Data Visualization Class Project** — *Individual Project Owner*  
    _Feb 2025 – May 2025_  
    - Applied Principal Component Analysis (PCA) for dimensionality reduction to simplify complex datasets while preserving key variance; interpreted results using rotation matrix and PC1 vs. PC2 scatterplots
    - Customized visualizations by designing appropriate plot types for different data
    """)
    with open("pca_analysis.pdf", "rb") as f:
        base64_pdfj = base64.b64encode(f.read()).decode("utf-8")
# Generate HTML to embed the PDF in an iframe
    pdf_viewer = f"""
    <iframe src="data:application/pdf;base64,{base64_pdfj}" width="100%" height="600" type="application/pdf"></iframe>
"""
# Add collapsible reader
    with st.expander("🔽 R Code for Stacked Barplot, Boxplot, and Sina plot Creation"):
        st.markdown(pdf_viewer, unsafe_allow_html=True)
        
    with open("sds_pro2.pdf", "rb") as f:
        base64_pdfz = base64.b64encode(f.read()).decode("utf-8")
# Generate HTML to embed the PDF in an iframe
    pdf_viewer = f"""
    <iframe src="data:application/pdf;base64,{base64_pdfz}" width="100%" height="600" type="application/pdf"></iframe>
"""
# Add collapsible reader
    with st.expander("🔽 R Code for Principle Component Analysis"):
        st.markdown(pdf_viewer, unsafe_allow_html=True)
    
    st.write("") 

    #proj3
    st.markdown("""
    **Practical Machine Learning Project** — *Member*  
    _Oct 2024 – Dec 2024_  
    - The project aimed to study what features of a post in reddit regarding NFL contests contribute most significantly to comment engagement
    - Used Python to clean data and apply a decision tree model
""")
    st.markdown("""
    [🔗Machine Learning Project Python Code](https://colab.research.google.com/drive/1WtdULE0xIIFWzL7l-5xrkcjCYH623pgQ?usp=sharing)
    """)
    
    image22 = Image.open("res.jpg")  # or .jpg, .jpeg, etc.
    # Create an expander
    with st.expander("📷 Key finding in the project"):
        st.image(image22, caption="", use_container_width=True)
    st.write("") 
    
    
    #proj4
    st.markdown("""
    **Elements of Software Design Project** — *Team Member*  
    _Jun 2024 – Sep 2024_  
    - The UT Shuttles Planner project provides users with the most time efficient plan of which UT shuttles to take given a user’s desired starting location and the destination
""")

    image111 = Image.open("map.jpg")  # or .jpg, .jpeg, etc.
    # Create an expander
    with st.expander("🚌 Bus Routes Map"):
        st.image(image111, caption="", use_container_width=True)

    image222 = Image.open("exa.jpg")  # or .jpg, .jpeg, etc.
    # Create an expander
    with st.expander("📷 Example Result"):
        st.image(image222, caption="", use_container_width=True)
        
    with st.expander("📄 View Python code"):
        with open("final_version.py", "r", encoding="utf-8") as f:
            code = f.read()
        st.code(code, language='python')

    st.write("")

    
 #work experience
    st.markdown("<h3 style='text-align: left;'>Work Experience</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    **Forte Capital Group** — *Research Analyst Intern*,  
    Remote  
    _Jun 2024 – Sep 2024_  
    - Created an Excel list of qualified investors for pre-IPO investments by conducting around 1000 reverse searches, enlarging the company’s customer group
    - Researched and presented Flexport company’s current and future market performance, providing investment suggestions regarding Flexport company
""")
    st.write("")

    st.markdown("""
**Austin Voices and Education** — *Data Entry Specialist*,  
Austin, TX  
_Sep 2022 – Jul 2023_  

- Streamlined data management on the Austin ISD website, ensuring accuracy and efficiency in updating student information  
- Facilitated the distribution of support for around 70,000 Austin ISD students by promptly responding to inquiries and requests
""")

    st.write("")
   
    st.markdown("<h3 style='text-align: left;'>SDS Related Skills and Affiliations</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Technical Skills**:  
    Intermediate Python, Advanced R, MySQL, PostgreSQL, MongoDB, Neo4j, Apache, BigQuery, Excel, Stata, Google Slides, Google Docs  
""") 
    st.markdown("""
    - **Technical Classes**:  
    Regression, Time Series Forecasting, Data Visualization, Elements of Databases, Practical Machine Learning, Possibility/Statistic Inference, Introduction to Data Science, Matrices and Matrix Calculations, \
        Calculus, Multivariate Calculus, Statistical Thinking, Elements of Software Design  
""")

    st.markdown("""
    - **Affiliations**:  
    American Statistical Association UT Austin, Machine Learning & Data Science Club
""", unsafe_allow_html=True)

################--- Tab 2 Content ---
with tab2:
    
    st.markdown("<h3 style='text-align: left;'>Work Experience</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    **Pearl Tech** — *Marketing Intern*,  
    Austin, TX  
    _Apr 2025 – Present_  
    - Initiated contact with influencers to drive pre-order purchases and enhance product visibility 
    - Designed and produced promotional video clip, posted on social media platforms to attract potential customers
""")
    st.write("")

    st.markdown("""
    **Nestplus Realty** — *Marketing Intern*,  
    Austin, TX  
    _Oct 2024 – Feb 2025_  
    - Created and edited 2 comprehensive reports on the Austin residential and commercial real estate market in 2024, each generating thousands of views
    - Contributed to the Nestplus YouTube channel’s video production by developing creative video concepts, writing video scripts, and assisting with video recording

""")
    st.write("")
    st.markdown("""
    **Forte Capital Group** — *Research Analyst Intern*,  
    Remote  
    _Jun 2024 – Sep 2024_  
    - Created an Excel list of qualified investors for pre-IPO investments by conducting around 1000 reverse searches, enlarging the company’s customer group
    - Researched and presented Flexport company’s current and future market performance, providing investment suggestions regarding Flexport company
""")
    st.write("")
    st.markdown("""
    **iQIYI** — *Marketing Intern*,  
    Remote  
    _Oct 2023 – Jan 2024_  
    - Utilized Capcut and Microsoft Clipchamp to edit short video clips that brought thousands of views to promote Asian TV series streamed by IQIYI, significantly increasing IQIYI’s brand awareness
    - Published articles and videos on social media platforms (TikTok, Facebook) to market Asian TV series and direct potential audiences to watch on the IQIYI website
    - Devised and implemented innovative marketing strategies, including hosting lotteries in the comment section, and drove hundreds of VIP purchases on the IQIYI website 
""")
    st.write("")

    st.markdown("<h3 style='text-align: left;'>Project Experience</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    **Econometrics Class Paper**  
    - Proposed a research paper topic, collected statistical data from authentic websites, conducted analysis through Stata, and authored a paper discussing the findings 
""")
    
    with open("fin_pa.pdf", "rb") as f:
        base64_pdfr = base64.b64encode(f.read()).decode("utf-8")

# Generate HTML to embed the PDF in an iframe
    pdf_viewer = f"""
    <iframe src="data:application/pdf;base64,{base64_pdfr}" width="100%" height="600" type="application/pdf"></iframe>
"""

# Add collapsible reader
    with st.expander("🔗 Econometrics Research Report"):
        st.markdown(pdf_viewer, unsafe_allow_html=True)

    st.write("") 

    st.markdown("<h3 style='text-align: left;'>Economics Related Skills and Affiliations</h2>", unsafe_allow_html=True)

    st.markdown("""
    - **Technical Skills**:  
    Intermediate Python, Advanced R, Excel, Stata, Google Slides, Google Docs  
""") 

    st.markdown("""
    - **Technical Classes**:  
    Economics of Auctions, Foundations of Finance, Macroeconomic Theory, Introduction to Econometrics, \
        Math Microeconomics Theory Through Advanced Application, Foundations of Accouting,\
            Economic Statistics, Economics of Money
    
""")

    st.markdown("""
    - **Affiliations**:  
    Texas Economics Association
""", unsafe_allow_html=True)

st.write("")
    #outside tabs
st.markdown('<a name="comp"></a>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left;'>Competition Experience</h2>", unsafe_allow_html=True)
st.markdown("""
    **Global Case Competition at Harvard** — *Member*  
    _Feb 2025 – Apr 2025_  
    - Designed bar plots, time series line graphs, pie charts with R programming language, and customized slide templates with Canva for competition submissions
    - Reached the solution of acquiring a potential alternative acquisition target after analyzing financial feasibility with Excel and researching the luxury automotive and motorsport markets
""")

with open("case.pptx", "rb") as f:
    ppt_data = f.read()
# Generate HTML to embed the PDF in an iframe
st.download_button(
    label="📥 Download Presentation",
    data=ppt_data,
    file_name="case.pptx",
    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
)
st.write("")

st.markdown("""    
    **KBH Energy Finance Case Competition** — *Member*  
    _Sep 2024 – Oct 2024_  
    - The project in the competition aimed to propose and justify an acquisition target in the energy sector
    - Conducted energy sector research, implemented a financial statement and an LBO model for the company using Excel, and presented the project
    """)

with open("array.pdf", "rb") as f:
    base64_pdf33 = base64.b64encode(f.read()).decode("utf-8")
# Generate HTML to embed the PDF in an iframe
pdf_viewer2 = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf33}" width="100%" height="600" type="application/pdf"></iframe>
"""
# Add collapsible reader
with st.expander("🔽 Presentation Slides"):
    st.markdown(pdf_viewer2, unsafe_allow_html=True)

st.write("")

st.markdown('<a name="lea"></a>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left;'>🌟 Leaderships</h2>", unsafe_allow_html=True)
st.markdown("""
    - **American Express Formula 1** — Brand Ambassador (Oct 2024)
    - **Tzu Chi Collegiate Association** — Lecturer (Oct 2022 – Sep 2024)
    - **Matriculate** — Advisor (Oct 2022 – May 2024)
    """)

st.write("")

st.markdown('<a name="languages"></a>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left;'>🌍 Languages</h2>", unsafe_allow_html=True)
st.markdown("""
    - Fluent Mandarin  
    - Advanced Cantonese
""")

