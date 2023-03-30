import PySimpleGUI as sg
import json

with open("settings.json") as f:
    s = json.load(f)
    feature_names = list(s["features"].keys())

def add_fband_row(item_num, band_name:str, low_f: int, high_f:int, selected: bool=True,):
    """
    A "Row" in this case is a Button with an "X", an Input element and a Text element showing the current counter
    :param item_num: The number to use in the tuple for each element
    :type:           int
    :return:         List
    """
    row =  [sg.pin(sg.Col([[sg.Checkbox(" ",default=selected, k=("-SELECT_FBAND-", item_num,)),
                            sg.T("Name"),
                            sg.In(band_name, size=(8,1), k=('-FBAND_NAME-', item_num)),
                            sg.T("Range:"),
                            sg.In(str(low_f), size=(3,1), k=('-FBAND_LOW_RANGE-', item_num)),
                            sg.T("-"), 
                            sg.In(str(high_f), size=(3,1), k=('-FBAND_HIGH_RANGE-', item_num)),
                            sg.T("Hz"), 
                            ]], k=('-ROW-', item_num), pad=0))]
    return row

def get_selectred_fband_info(values: dict):
    indexes = [i[1] for i in list(values.keys()) if i[0] == '-SELECT_FBAND-' and values[i] == True]
    d = {}
    for i in indexes:
        d[values[("-FBAND_NAME-", i)]] = [values[("-FBAND_LOW_RANGE-", i)], values[("-FBAND_HIGH_RANGE-", i)]]
    return d


def make_window():

    layout = [  [sg.Text('Add Frequency bands', font='_ 15')],
                [sg.Col([add_fband_row(idx, fb_idx[0], fb_idx[1][0], fb_idx[1][1]) for idx, fb_idx in enumerate(s["frequency_ranges_hz"].items())], k='-TRACKING SECTION-')],
                [sg.T('+', enable_events=True, k='Add Item', tooltip='Add Another Item')]]


    layout_frame = [[sg.Frame("none", layout)]]

    layout_columns = [[sg.Column(layout_frame, scrollable=True, key="-column_scroll-", vertical_scroll_only=True)],
                      [sg.In("Hallo, stay here")]]

    window = sg.Window('Window Title', layout_columns, use_default_focus=False, font='_ 15', metadata=len(list(s["frequency_ranges_hz"].keys()))-1)

    return window

def main():

    window = make_window()
    while True:
        event, values = window.read()     # wake every hour
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Add Item':
            window.metadata += 1
            window.extend_layout(window['-TRACKING SECTION-'], [add_fband_row(window.metadata, "band_name", 5, 12, True)])
            window.refresh()    
            window['-column_scroll-'].contents_changed() 
    window.close()


if __name__ == '__main__':
    main()