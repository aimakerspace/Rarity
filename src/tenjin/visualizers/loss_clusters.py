import plotly.graph_objects as go


def _plot_common_clusters(df, models, analysis_type):
    fig = go.Figure()
    if analysis_type == 'regression':  # regression task 
        x_m1 = df[f'cluster_{models[0]}']
        y_m1 = df[f'offset_{models[0]}']
        customdata_m1 = list(df.index)
        if len(models) == 2:
            x_m2 = df[f'cluster_{models[1]}']
            y_m2 = df[f'offset_{models[1]}']
            customdata_m2 = customdata_m1

    else:  # binary classification
        x_m1 = df[0]['cluster']
        y_m1 = df[0]['lloss']
        customdata_m1 = list(df[0].index)
        if len(models) == 2:
            x_m2 = df[1]['cluster']
            y_m2 = df[1]['lloss']
            customdata_m2 = list(df[1].index)

    fig.add_trace(go.Violin(x=x_m1,
                            y=y_m1,
                            legendgroup=models[0], scalegroup=models[0], name=models[0],
                            line_color='#1f77b4',
                            customdata=customdata_m1,
                            hovertemplate='index=%{customdata}<br>cluster=%{x}<br>offset=%{y}<br>',
                            showlegend=True))

    if len(models) == 2:
        fig.add_trace(go.Violin(x=x_m2,
                                y=y_m2,
                                legendgroup=models[1], scalegroup=models[1], name=models[1],
                                line_color='#FF7F0E',
                                customdata=customdata_m2,
                                hovertemplate='index=%{customdata}<br>cluster=%{x}<br>offset=%{y}<br>',
                                showlegend=True))

    # update characteristics shared by all traces
    fig.update_traces(meanline_visible=True,
                    box_visible=True,
                    points='all',  # show all points
                    jitter=0.05,  # add some jitter on points for better visibility
                    scalemode='count')  # scale violin plot area with total count

    fig.update_layout(
        title_x=0.5,
        xaxis_title='Cluster',
        width=1250,
        height=550,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        violingap=0.2, violingroupgap=0.3, violinmode='overlay')
    return fig


def plot_offset_clusters(df, analysis_type):
    '''
    For use in regression task only
    '''
    models = [col.replace('cluster_', '') for col in df.columns if 'cluster_' in col]
    fig = _plot_common_clusters(df, models, analysis_type)
    fig.update_layout(title_text='<b>Overview of Prediction Offset Clusters</b>', yaxis_title='Offset from baseline')
    return fig


def plot_logloss_clusters(dfs, analysis_type):
    '''
    For use in classification task only
    '''
    models = [df['model'].values[0] for df in dfs]
    fig = _plot_common_clusters(dfs, models, analysis_type)
    fig.update_layout(title_text='<b>Overview of Log-Loss Clusters on Miss-Prediction</b>', yaxis_title='Log-Loss')
    return fig


def plot_optimum_cluster_via_elbow_method(cluster_range, sum_squared_distance, models):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=cluster_range[0],
                            y=sum_squared_distance[0],
                            mode='lines+markers',
                            name=models[0],
                            line=dict(color='#1F77B4')))

    if len(cluster_range) == 2:
        fig.add_trace(go.Scatter(
                            x=cluster_range[1],
                            y=sum_squared_distance[1],
                            mode='lines+markers',
                            name=models[1],
                            line=dict(color='#FF7F0E')))

    fig.update_layout(title='<b>Overview of Optimum Cluster Count</b>',
                    xaxis_title='No. of Cluster',
                    yaxis_title='Sum of Squared Distance',
                    title_x=0.5,
                    showlegend=True,
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                    width=1000,
                    height=550)

    fig.update_xaxes(rangemode="tozero")
    return fig