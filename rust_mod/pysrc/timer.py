import numpy as np 
from sklearn import linear_model
import timeit
from plotly import graph_objects as go

COLORS = ['#55AA55','#AA5555', '#5555AA']

def time_function(names, timeit_fun, timeit_setup, test_input, num_repeats = 100):
    values = {name: [] for name in names}
    for i in test_input:
        for name in names:
            v = timeit.timeit(f"{timeit_fun[name]}({i})", setup=f"{timeit_setup[name]}", number=num_repeats)
            values[name].append(v / num_repeats)
            
        if i % ((len(test_input)//10+1)) == 0:
            print(i, 'out of ', test_input[-1])
    return values

def calc_linear_approximation(names, test_input, values):
    params = {}
    for name in names:
        params[name] = {}
        X = np.array(test_input).reshape(len(test_input), 1)
        y = np.array(values[name])
        # Robustly fit linear model with RANSAC algorithm
        ransac = linear_model.RANSACRegressor()
        ransac.fit(X, y)
        
        v = ransac.predict(np.array([[0.],[1]]))
        params[name]['m'] = v[0]
        params[name]['k'] = v[1]-v[0]
    return params

def plot_time_figure(names, test_input, values, params):
    
    min_val = min([min(values[name]) for name in names])
    max_val = max([max(values[name]) for name in names])
    text_start = [min(test_input) + 2/10*(max(test_input) - min(test_input)),
                min_val + 9/10*(max_val - min_val)]
    y_diff = 1/10*(max_val - min_val)

    fig = go.Figure(
        data = [
                go.Scatter(x = test_input, y = values[name],
                    mode='markers',
                    name=name,
                    marker = {'color': COLORS[i]})
                for i, name in enumerate(names)] +
            [
                go.Scatter(x = [min(test_input), max(test_input)], y = [params[name]['m'], params[name]['m']+max(test_input)*params[name]['k']],
                    mode='lines',
                    showlegend = False,
                    line = {'color': COLORS[i]} )
                for i, name in enumerate(names)] +
            [
                go.Scatter(x = [text_start[0]], y = [text_start[1]-i*y_diff],
                        mode='text',
                        showlegend = False,
                        text = f"{name}: {params[name]['k']:0.2}x+{params[name]['m']:0.2}")
                    for i, name in enumerate(names)]
    )
    return fig


