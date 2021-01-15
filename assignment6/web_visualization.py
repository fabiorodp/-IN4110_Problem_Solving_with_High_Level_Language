# UiO: IN4110 - H20
# Assignment 6
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no

"""
Flask app to create a website where the user can choose different Counties,
Chart's types, periodicity, and date-rage.
"""

import pandas as pd
import altair as alt
import altair_viewer
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import tempfile
import datetime
import os

app = Flask(__name__, static_url_path='/', static_folder='docs/_build/html/')


def plot_reported_cases(county='Alle_Fylker', periodicity='day',
                        start=None, end=None, plot_lib='Altair',
                        view_plot=False, plot_title=False,
                        width=800, height=500):
    """
    Function to generate a bar-plot for Covid19's total daily cases from
    FHI/Norway.

    Parameters:
    ~~~~~~~~~~~~~~~~~~~~
    :param county: str: Name od the county to be analyzed, which could
                        be  'Agder', 'Innlandet', 'More_og_Romsdal',
                        'Nordland', 'Oslo', 'Rogaland',
                        'Troms_og_Finnmark', Trondelag',
                        'Vestfold_og_Telemark', 'Vestland',
                        'Viken'or 'Alle_Fylker' for all counties.
    :param periodicity: str: Periodicity to display the plot, which could
                             be 'day' or 'week'. Default 'day'.
    :param start: str or date object: The starting date for the analysis.
    :param end: str or date object: The ending date for the analysis.
    :param plot_lib: str: The name of the plotting library to be used.
                          Default is 'Altair' which uses Altair. A option
                          is 'plt' which uses matplotlib.
    :param view_plot: bool: The default is False to not show the plot.
    :param plot_title: bool: The default is False to not display the
                             plot's title.
    :param width: int: Only used for 'Altair' plot. Define the width of
                       the plotting. Default is 800.
    :param height: int: Only used for 'Altair' plot. Define the height of
                       the plotting. Default is 500.

    Notes:
    ~~~~~~~~~~~~~~~~~~~~
    - If start and end are None, them it will plot the entire data-base.
    """
    # setting fixed parameters
    col = 'Nye tilfeller'
    title = 'Number of reported cases'

    # setting prefix and suffix for the data-files
    path = 'data/'
    if periodicity == 'day':
        prefix = path + 'antall-meldte-covid-19-t_day_'

    elif periodicity == 'week':
        prefix = path + 'antall-meldte-covid-19-t_week_'

    else:
        raise ValueError("Error: The given periodicity is not valid.")

    suffix = '.csv'

    # reading data as DataFrame
    df = pd.read_csv(filepath_or_buffer=prefix + county + suffix,
                     sep=',', index_col='Dato')

    # setting data range
    df = df[start:end]

    # creating Altair's plotting
    if plot_lib == 'Altair':

        # fixing datetime for Altair
        df.reset_index(inplace=True)

        if periodicity == 'day':
            df['Dato'] = pd.to_datetime(df["Dato"], dayfirst=True)

            # plotting bar and lines in dual-axis
            chart = alt.Chart(df).mark_bar().encode(
                alt.X('Dato:T'),
                alt.Y(col + ':Q', title=title),
                tooltip=['Dato', col])

        elif periodicity == 'week':
            # plotting bar and lines in dual-axis
            chart = alt.Chart(df).mark_bar().encode(
                alt.X('Dato',
                      scale=alt.Scale(zero=False)),
                alt.Y(col + ':Q', title=title),
                tooltip=['Dato', col])

        # plotting
        chart = chart.properties(
            width=width,
            height=height,
            title=f'Data Vs ({title}) for {county}'
        ).interactive()

        # viewing the plot
        if view_plot is True:
            # altair_viewer.show(chart)
            altair_viewer.display(chart)

        return chart

    # creating Matplotlib plot
    elif plot_lib == 'plt':

        # plotting using matplotlib
        plt.bar(x=df.index, height=df[col])

        # plotting set-up
        if plot_title is True:
            plt.title(f'Data Vs {title} for {county}')

        plt.xlabel('Date')
        plt.ylabel(f'{title}')
        plt.xticks(rotation='vertical')

        # viewing plot
        if view_plot is True:
            plt.show()

    else:
        raise ValueError(f"Error: Plot type {plot_lib} not implemented.")


def plot_cumulative_cases(county='Alle_Fylker', periodicity='day',
                          start=None, end=None, plot_lib='Altair',
                          view_plot=False, plot_title=False,
                          width=800, height=500):
    """
    Function to generate a line-plot for Covid19's total daily cases from
    FHI/Norway.

    Parameters:
    ~~~~~~~~~~~~~~~~~~~~
    :param county: str: Name od the county to be analyzed, which could
                        be  'Agder', 'Innlandet', 'More_og_Romsdal',
                        'Nordland', 'Oslo', 'Rogaland',
                        'Troms_og_Finnmark', Trondelag',
                        'Vestfold_og_Telemark', 'Vestland',
                        'Viken'or 'Alle_Fylker' for all counties.
    :param periodicity: str: Periodicity to display the plot, which could
                             be 'day' or 'week'. Default 'day'.
    :param start: str or date object: The starting date for the analysis.
    :param end: str or date object: The ending date for the analysis.
    :param plot_lib: str: The name of the plotting library to be used.
                          Default is 'Altair' which uses Altair. A option
                          is 'plt' which uses matplotlib.
    :param view_plot: bool: The default is False to not show the plot.
    :param plot_title: bool: The default is False to not display the
                             plot's title.
    :param width: int: Only used for 'Altair' plot. Define the width of
                       the plotting. Default is 800.
    :param height: int: Only used for 'Altair' plot. Define the height of
                       the plotting. Default is 500.

    Notes:
    ~~~~~~~~~~~~~~~~~~~~
    - If start and end are None, them it will plot the entire data-base.
    """

    # setting fixed parameters
    col = 'Kumulativt antall'
    title = 'Cumulative number of cases'

    # setting prefix and suffix for the data-files
    path = 'data/'
    if periodicity == 'day':
        prefix = path + 'antall-meldte-covid-19-t_day_'

    elif periodicity == 'week':
        prefix = path + 'antall-meldte-covid-19-t_week_'

    else:
        raise ValueError("Error: The given periodicity is not valid.")

    suffix = '.csv'

    # reading data as DataFrame
    df = pd.read_csv(filepath_or_buffer=prefix + county + suffix,
                     sep=',', index_col='Dato', infer_datetime_format=True)

    # setting data range
    df = df[start:end]

    # creating Altair's plotting
    if plot_lib == 'Altair':

        # fixing datetime for Altair
        df.reset_index(inplace=True)

        if periodicity == 'day':
            df['Dato'] = pd.to_datetime(df["Dato"], dayfirst=True)

            # plotting bar and lines in dual-axis
            chart = alt.Chart(df).mark_line().encode(
                alt.X('Dato:T'),
                alt.Y(col + ':Q', title=title),
                tooltip=['Dato', col])

        elif periodicity == 'week':
            # plotting bar and lines in dual-axis
            chart = alt.Chart(df).mark_line().encode(
                alt.X('Dato',
                      scale=alt.Scale(zero=False)),
                alt.Y(col + ':Q', title=title),
                tooltip=['Dato', col])

        # plotting
        chart = chart.properties(
            width=width,
            height=height,
            title=f'Data Vs ({title}) for {county}'
        ).interactive()

        # viewing the plot
        if view_plot is True:
            # altair_viewer.show(chart)
            altair_viewer.display(chart)

        return chart

    # creating Matplotlib or Seaborn plot
    if plot_lib == 'plt':

        # plotting from matplotlib
        plt.plot(df.index, df[col], color='red', label=title)

        # plotting set-up
        if plot_title is True:
            plt.title(f'Data Vs {title} for {county}')

        plt.xlabel('Date')
        plt.ylabel(f'{title}')
        plt.xticks(rotation='vertical')
        plt.legend()

        # viewing plot
        if view_plot is True:
            plt.show()

    else:
        raise ValueError(f"Error: Plot type {plot_lib} not implemented.")


def plot_both(county='Alle_Fylker', periodicity='day',
              start=None, end=None, plot_lib='Altair',
              view_plot=False, plot_title=False,
              width=800, height=500):
    """
    Function to generate a line-plot for Covid19's total daily cases from
    FHI/Norway.

    Parameters:
    ~~~~~~~~~~~~~~~~~~~~
    :param county: str: Name od the county to be analyzed, which could
                        be  'Agder', 'Innlandet', 'More_og_Romsdal',
                        'Nordland', 'Oslo', 'Rogaland',
                        'Troms_og_Finnmark', Trondelag',
                        'Vestfold_og_Telemark', 'Vestland',
                        'Viken'or 'Alle_Fylker' for all counties.
    :param periodicity: str: Periodicity to display the plot, which could
                             be 'day' or 'week'. Default 'day'.
    :param start: str or date object: The starting date for the analysis.
    :param end: str or date object: The ending date for the analysis.
    :param plot_lib: str: The name of the plotting library to be used.
                          Default is 'Altair' which uses Altair. A option
                          is 'plt' which uses matplotlib.
    :param view_plot: bool: The default is False to not show the plot.
    :param plot_title: bool: The default is False to not display the
                             plot's title.
    :param width: int: Only used for 'Altair' plot. Define the width of
                       the plotting. Default is 800.
    :param height: int: Only used for 'Altair' plot. Define the height of
                       the plotting. Default is 500.

    Notes:
    ~~~~~~~~~~~~~~~~~~~~
    - If start and end are None, them it will plot the entire data-base.
    """
    # creating Matplotlib or Seaborn plot
    if plot_lib == 'plt':

        # plotting cumulative cases
        plot_cumulative_cases(county=county, start=start, end=end,
                              plot_lib=plot_lib, view_plot=False,
                              plot_title=False)

        # setting plots together but with independent y-axis
        plt.twinx()

        # plotting daily reported cases
        plot_reported_cases(county=county, start=start, end=end,
                            plot_lib=plot_lib, view_plot=False,
                            plot_title=False)

        # setting plot's title
        if plot_title is True:
            plt.title(f'Data Vs (cumulative and daily cases) '
                      f'for {county}')

        # viewing plot
        if view_plot is True:
            plt.show()

    elif plot_lib == 'Altair':
        # setting fixed parameters
        col1 = 'Kumulativt antall'
        title1 = 'Cumulative nrs.'

        col2 = 'Nye tilfeller'
        title2 = 'New report nrs.'

        # setting prefix and suffix for the data-files
        path = 'data/'
        if periodicity == 'day':
            prefix = path + 'antall-meldte-covid-19-t_day_'

        elif periodicity == 'week':
            prefix = path + 'antall-meldte-covid-19-t_week_'

        else:
            raise ValueError("Error: The given periodicity is not valid.")

        suffix = '.csv'

        # reading data as DataFrame
        df = pd.read_csv(filepath_or_buffer=prefix + county + suffix,
                         sep=',', index_col='Dato',
                         infer_datetime_format=True)

        # setting data range
        df = df[start:end]

        # fixing datetime for Altair
        df.reset_index(inplace=True)

        base = None
        if periodicity == 'day':
            df['Dato'] = pd.to_datetime(df["Dato"], dayfirst=True)

            # creating base for Altair plot as a function of daily-dates
            base = alt.Chart(df).encode(
                alt.X('Dato:T',
                      axis=alt.Axis(format='%Y-%m-%d'),
                      scale=alt.Scale(zero=False)))

        if periodicity == 'week':
            # creating base for Altair plot as a function of weekly-dates
            base = alt.Chart(df).encode(
                alt.X('Dato',
                      scale=alt.Scale(zero=False)))

        # drawing bars
        bar = base.mark_bar(opacity=0.3).encode(
            y=alt.Y(col2, axis=alt.Axis(title=title2, orient='left')), )

        # drawing line
        line = base.mark_line(color='red').encode(
            y=alt.Y(col1, axis=alt.Axis(title=title1, orient='right')), )

        # creating x-axis selections
        nearest = alt.selection(type='single', nearest=True, on='mouseover',
                                fields=['Dato'], empty='none')

        # Transparent selectors across the chart. This is what tells us
        # the x-value of the cursor
        selectors = alt.Chart(df).mark_point().encode(
            x='Dato', opacity=alt.value(0), ).add_selection(nearest)

        # drawing points on the line, and highlight based on selection
        points = line.mark_point().encode(
            opacity=alt.condition(nearest, alt.value(1), alt.value(0)))

        # drawing a rule at the location of the selection
        rules = alt.Chart(df).mark_rule(color='gray').encode(
            x='Dato', ).transform_filter(nearest)

        # setting dual-axis
        chart = alt.layer(line, bar, selectors, points, rules).resolve_scale(
            y='independent')

        # setting properties and interactiveness
        chart = chart.properties(
            width=width,
            height=height,
            title=f'Covid19 reports for {county}'
        ).interactive()

        # adding tooltips
        chart = chart.encode(
            tooltip=[alt.Tooltip('Dato', title='Date'),
                     alt.Tooltip(col1, title=title1),
                     alt.Tooltip(col2, title=title2)])

        # viewing the plot
        if view_plot is True:
            altair_viewer.show(chart)
            # altair_viewer.display(chart)

        return chart

    else:
        raise ValueError(f"Error: Plot type {plot_lib} not implemented.")


@app.route('/')
def index():
    """Publishing the index web page."""
    return render_template('main.html')


@app.route('/chart_frame')
def chart_frame():
    """Publishing the initial chart's frame web page."""
    return render_template('chart_frame.html')


@app.route('/handle_form', methods=['POST'])
def handle_form():
    """Handling the form and getting the chosen chart."""
    # accessing form values and defining standard ones
    county = request.form["county"]
    start = request.form["start"]
    end = request.form["end"]

    periodicity = request.form["periodicity"]
    if periodicity == '':
        periodicity = 'day'

    if periodicity == 'day':
        start = start[8:] + '.' + start[5:7] + '.' + start[:4]
        end = end[8:] + '.' + end[5:7] + '.' + end[:4]

    elif periodicity == 'week':
        year = start[:4]
        month = start[5:7]
        day = start[8:]
        week = datetime.date(int(year), int(month), int(day)).isocalendar()[1]
        start = year + '-' + str(week)

        year = end[:4]
        month = end[5:7]
        day = end[8:]
        week = datetime.date(int(year), int(month), int(day)).isocalendar()[1]
        end = year + '-' + str(week)

    plot_type = request.form["plot_type"]
    if plot_type == '':
        plot_type = 'both'

    # retrieving the specific chart from python functions
    fig = None
    if plot_type == 'reported_cases':
        fig = plot_reported_cases(
            county=county, periodicity=periodicity,
            start=start, end=end, plot_lib='Altair',
            view_plot=False, plot_title=True,
            width=400, height=400)

    elif plot_type == 'cumulative_cases':
        fig = plot_cumulative_cases(
            county=county, periodicity=periodicity,
            start=start, end=end, plot_lib='Altair',
            view_plot=False, plot_title=True,
            width=400, height=400)

    elif (plot_type == 'both') or (plot_type == ''):
        fig = plot_both(
            county=county, periodicity=periodicity,
            start=start, end=end, plot_lib='Altair',
            view_plot=False, plot_title=True,
            width=400, height=400)

    # generating the Altair's html file
    fig.save('plot.html')

    # publishing the charting the html file
    with open('plot.html') as file:
        return file.read()

    #     tmp = tempfile.NamedTemporaryFile(suffix=".json")
    #     fig.save(tmp.name)
    #
    #     with open(tmp.name) as file:
    #         return file.read()


@app.route('/')
@app.route('/<path:path>')
def serve_sphinx_docs(path='index.html'):
    """Handling Sphinx documentation on Flask."""
    return app.send_static_file(path)


if __name__ == '__main__':
    # running the website
    app.run()
