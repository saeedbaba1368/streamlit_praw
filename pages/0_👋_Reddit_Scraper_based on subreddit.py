
import streamlit as st
from df_global_search import DataFrameSearch
from get_reddit import get_reddit
from get_subreddit_data import get_subreddit_data

reddit=get_reddit()
df={}


col1, col2, col3,col4 = st.columns(4)
with col1:
    topic = st.text_input('Subreddit Name')
with col2:
    limit= st.number_input('Number Filter', min_value=0, max_value=100, value=4, step=1)
with col3:
    attr=st.selectbox('Sort By:', ('top', 'hot', 'rising', 'new',"controversial"))
with col4:
    time_filter=st.selectbox('Time Filter:', ("hour","day",'week', 'month', 'year', 'all'))
    
button = st.button("Click to Start process")


if button:
	st.success(f'Welcome to the reddit scraper for , {topic} topic!')
	

if topic :
    
	
	df = get_subreddit_data(attr,reddit,topic,limit,time_filter)

    	
	search_bar_columns = st.columns((0.1, 1, 0.75, 0.75, 1))
	with search_bar_columns[1]:
		search_text = st.text_input(
				"Search", label_visibility="collapsed", placeholder="Search Text"
			)
	with search_bar_columns[2]:
			is_regex = st.toggle("Regex", value=False)
	with search_bar_columns[3]:
			case_sensitive = st.toggle("Case Sensitive", value=False)
	with search_bar_columns[4]:
			highlight_match = st.toggle("Highlight Matching Cells", value=True)

	with DataFrameSearch(
			dataframe=df,
			text_search=search_text,
			case_sensitive=case_sensitive,
			regex_search=is_regex,
			highlight_matches=highlight_match,
		) as df:
			st.dataframe(data=df, use_container_width=True, hide_index=True)
else:
    st.write("enjoy Reddit scraper")
