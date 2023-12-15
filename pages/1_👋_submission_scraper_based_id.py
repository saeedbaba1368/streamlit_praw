import streamlit as st
from df_global_search import DataFrameSearch
from get_reddit import get_reddit
from get_submission_data_by_id import get_submission_data_by_id
reddit=get_reddit()
df_attr={}
col1,col2 = st.columns(2)
with col1:
    submission_id = st.text_input('Submission_Id')
with col2:
    attr=st.selectbox('Choose :', ('comments', 'submission'))
    
button = st.button("Click to Start process")


if button:
	st.success(f'Welcome to the reddit scraper for , {submission_id} submission_id!')

if submission_id :
    df_submission, df_comments = get_submission_data_by_id(submission_id,reddit)
    if attr=="comments":
        df_attr=df_comments
    else:
        df_attr=df_submission
    search_bar_columns_submission = st.columns((0.01, 1))
    with search_bar_columns_submission[1]:
        search_text_submission = st.text_input(
				"Search", label_visibility="collapsed", placeholder="Search Text"
			)

    with DataFrameSearch(
			dataframe=df_attr,
			text_search=search_text_submission,
			
		) as df_attr:
            st.dataframe(data=df_attr, use_container_width=True, hide_index=True)
else:
    st.write("enjoy Reddit scraper")















































