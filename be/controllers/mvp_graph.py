"""Creates and returns mvp graph."""
from sample_data import genotype_list
import plotly.graph_objects as go
import pandas as pd

def mvp_graph(df, type, result, genotype):
    """Create a scatter graph on filtered data frame."""
    graph = go.Figure()
    count = 0
    # data = df.loc[df['type'] == type]
    # data = data.loc[data['result'] == result]
    for gn in genotype_list:
        temp_df = df[df['mvp'] == int(gn)]
        if not temp_df.empty:
            day_group = temp_df.groupby('day')
            graph_df = pd.DataFrame()
            graph_df['count'] = day_group['mvp'].count()
            graph_df = graph_df.reset_index()
            if gn == genotype:
                visibility = True
            else:
                visibility = 'legendonly'
            graph.add_trace(go.Scatter(x=graph_df['day'], y=graph_df['count'], mode='markers+lines', name=gn, marker_symbol= count, showlegend=True, visible=visibility))
            count += 1
    graph.update_layout(legend_title_text = "Genotype")
    graph.update_yaxes(title_text='number')
    return [graph, graph_df]