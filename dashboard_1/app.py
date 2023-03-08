import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Covid-19 Cases in Prison Facilities Dashboard",
    page_icon=":mask:",
    layout='wide'
)

#copy entire path otherwise streamlit localhost would not read it
df = pd.read_csv('/home/amina/Desktop/per/python-programs/dashboard_one/facilities.csv')

#cases_in_alabama = df[(df['facility_state'] == 'Alabama')]

#st.dataframe(df) #localhost

st.sidebar.header("Filter Here:")
state = st.sidebar.multiselect(
    "Select the Facility State:",
    options=df["facility_state"].unique(),
    default=df["facility_state"].unique()
)

country = st.sidebar.multiselect(
    "Select the Facility Country:",
    options=df["facility_county"].unique(),
    default=df["facility_county"].unique()
)

city = st.sidebar.multiselect(
    "Select the Facility City:",
    options=df["facility_city"].unique(),
    default=df["facility_city"].unique()
)

#THE QUERY

df_selection = df.query(
    "facility_state == @state & facility_county == @country & facility_city == @city "
)

# ---------- MAIN PAGE ----------
st.title(":bar_chart: USA Covid-19 Cases in Prison Facilities")
st.markdown("##")

total_cases_inmates = int(df_selection["total_inmate_cases"].sum())
average_death_rate_inmates = (df_selection["total_inmate_deaths"].sum() / df_selection["max_inmate_population_2020"].sum()) * 100000

total_cases_officers = int(df_selection["total_officer_cases"].sum())
average_death_rate_officers = (df_selection["total_officer_deaths"].sum() / df_selection["total_officer_cases"].sum()) * 100000

average_death_rate = format(average_death_rate_officers + average_death_rate_inmates, ".2f")

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Inmates Cases:")
    st.subheader(f"{total_cases_inmates}")
with middle_column:
    st.subheader("Total Officers Cases:")
    st.subheader(f"{total_cases_officers}")
with right_column:
    st.subheader("Average Death Rate:")
    st.subheader(f"{average_death_rate}")

st.markdown("---")


# ---------- BAR CHART, CASES PER FACILITY ----------
cases_per_facility_type = (
    df_selection.groupby(by=["facility_type"]).sum()[["total_inmate_cases"]].sort_values(by=f"facility_type")
)

fig_cases_per_facility = px.bar(
    cases_per_facility_type,
    x="total_inmate_cases",
    y=cases_per_facility_type.index,
    orientation="h",
    title="<b>Cases Per Facility Type</b>",
    color_discrete_sequence=["#9CC5A1"] * len(cases_per_facility_type),
    template="plotly_white",
    height=700,
)


st.plotly_chart(fig_cases_per_facility)


# ------ HIDE STREAMLIT STYLE -------
hide_st_styles = """
                <style>
                #MainMenu {visibility:hidden;}
                footer {visibility:hidden:}
                header {visibility:hidden:}
                </style>
                """
st.markdown(hide_st_styles, unsafe_allow_html=True)
#print(len(df))

#FOR VISUALAZATION: pip install plotly-express

#print(df.head())