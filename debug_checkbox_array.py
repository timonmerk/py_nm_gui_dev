import PySimpleGUI as sg
import json
with open("settings.json") as f:
    s = json.load(f)

def get_sw_feature_layout(estimator_list:list, list_sw_features: list):

    head_sw_est =  [[sg.Text("Empty", s=(9,1))] + [sg.Text(h, s=(5,1)) for h in estimator_list]]

    def add_row_sw_est(feature_name:str, num_cols: int):
        return [[sg.Text(feature_name, s=(9,1))] + [sg.Checkbox('', size=(2, 1), default=True, k=f"-sharpwave_feature_{feature_name}_estimator_{col_estimator}") for _, col_estimator in enumerate(range(num_cols))]]

    return head_sw_est + [add_row_sw_est(f, len(estimator_list)) for f in list_sw_features]

estimator_list = ["mean", "min", "max", "median", "var"]
list_sw_features = ["Trough", "Interval", "Prominence", "Rise time", "Decay time"]

#layout = get_sw_feature_layout(estimator_list, list_sw_features)
layout_sw_est = get_sw_feature_layout(list(s["sharpwave_analysis_settings"]["estimator"].keys()), list(s["sharpwave_analysis_settings"]["sharpwave_features"].keys()))
layout = [[sg.Frame("Estimators", layout=layout_sw_est, )]]

#layout = get_sw_feature_layout(list(s["sharpwave_analysis_settings"]["estimator"].keys()), list(s["sharpwave_analysis_settings"]["sharpwave_features"].keys())),

window = sg.Window('Test', layout)#, default_element_size=(15,1), auto_size_text=False)
event, values = window.read()
window.close()



import PySimpleGUI as sg

NUM_COLS = 5
NUM_ROWS = 8

list_estimators = ["mean", "min", "max", "median", "var"]



def add_column_sw_feature(col_name: str, num_rows: int):
    return sg.Column([[sg.T(col_name)]] + [[sg.Checkbox("", True, s=(1,5))] for i in range(num_rows)], pad=(0,0))

first_col = sg.Column([[sg.T("", s=(5,1))]] + [[sg.T(f, s=(5,1))] for f in list_sw_features],pad=(0,0))

layout = [[first_col] + [add_column_sw_feature(col_name, len(list_sw_features)) for col_name in list_estimators]]


window = sg.Window(
    "GUI Test",
    layout,
    auto_size_buttons=False,
    default_button_element_size=(12,1),
    use_default_focus=False,
    default_element_size=(15,1),
    auto_size_text=False,
    finalize=True,
    size=(600, 500),
    margins=(0,0),
)

while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
