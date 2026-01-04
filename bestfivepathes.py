
# العثور على أفضل 5 مسارات لكل دولة & الحل
top_paths = paths_df.groupby(['Country', 'solution', 'types']).size().reset_index(name='count')
top_paths = top_paths.sort_values(['Country', 'solution', 'count'], ascending=[True, True, False])
top_5_paths = top_paths.groupby(['Country', 'solution']).head(5)
