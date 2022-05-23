# ezNbeats
## keras style wrapper for N_Beats time series prediction model library, plot prediction data, get prediction data, improved errors and guardrails for simple prediction use.

Download directions are at the bottom of the page

## Plotting Function

```
import ezNbeats as Nbeats 

Nbeats.run_prediction_and_plot('ethdata.csv', 'period_prediction_in_integer_value')

```

Returns:

![readmeethdata](https://user-images.githubusercontent.com/61128114/163050549-daa91a46-4953-4a3d-8fc1-8f89034ce7fc.png)


## Return Prediction Values

```
Nbeats.return_prediction('ethdata.csv', 'period_prediction_in_integer_value')
```

Returns:

```
array([[4533.275 ],
       [4763.67  ],
       [3268.3918],
       [4135.316 ],
       [4364.2817],
       [2880.5466],
       [4336.967 ],
       [4308.3403],
       [4175.3003],
       [4983.2505],
       [4494.187 ],
       [4606.2715],
       [4599.9175],
       [4616.081 ],
       [5306.367 ],
       [5355.2334],
       [5408.6665],
       [5590.524 ],
       [4804.6304],
       [5413.8545],
       [5110.1167],
       [4739.2515],
       [5725.405 ],
       [4756.4424],
       [5187.714 ],
       [5316.915 ],
       [5154.975 ],
       [4508.4106],
       [4495.5225],
       [4979.912 ],
       [6297.265 ],
       [4575.6895],
       [4595.218 ],
       [4784.8228],
       [4837.4814],
       [4257.399 ],
       [4152.7993],
       [5176.271 ],
       [5433.6543],
       [6237.472 ],
       [5223.8813],
       [5309.657 ],
       [5729.7686],
       [5129.54  ],
       [6764.619 ],
       [7174.92  ],
       [6157.9614],
       [6530.81  ],
       [6562.5435],
       [6785.9463],
       [6472.0635],
       [6528.72  ],
       [5347.449 ],
       [6292.9966],
       [5805.043 ],
       [6684.3423],
       [6143.1997],
       [5369.238 ],
       [6882.697 ],
       [5556.365 ],
       [5842.768 ],
       [5629.788 ],
       [6172.0137],
       [5913.5005],
       [5939.173 ],
       [5678.9614],
       [5247.0776],
       [5601.757 ],
       [6229.9883],
       [6342.4746]], dtype=float32)
```


## Download Instructions

Clone repo
Cd into repo in terminal
`pip3 install .`
in python file:
`import ezNbeats as Nbeats`

dependencies are tough as pytorch, sci libraries, and nbeats_forecast all require different versions of numpy and etc. Recommended install in a venv, and add dependecies one by one, finally install nbeats_forecast as *pip3 install nbeats_forecast --no-cache-dir*

Contact me if you have issues downloading
