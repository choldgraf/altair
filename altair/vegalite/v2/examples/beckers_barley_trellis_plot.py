"""
Becker's Barley Trellis Plot
----------------------------
This example shows how to make a Trellis Plot with the barley dataset.
"""

import altair as alt
from vega_datasets import data

source = data.barley()

chart = alt.Chart(source).mark_point().encode(
    alt.X('median(yield)', scale=alt.Scale(zero = False)),
    alt.Y(
        'variety',
        sort=alt.SortField(field='yield', op='median', order='descending'),
        scale=alt.Scale(rangeStep=20)
    ),
    color='year:N',
    row='site'
)
