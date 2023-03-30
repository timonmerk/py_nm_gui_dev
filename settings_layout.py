import PySimpleGUI as sg

import json

WIDTH_LAYOUT = 280

with open("settings.json") as f:
    s = json.load(f)
    feature_names = list(s["features"].keys())
# everything in a column needs to be a layout beforehand

# check now layout with toggle buttons:
#sg.theme("DarkTeal11")

toggle_btn_on = b'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'

toggle_btn_off = b'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'

def add_fband_row(item_num, band_name:str, low_f: int, high_f:int, selected: bool=True,):
    """
    A "Row" in this case is a Button with an "X", an Input element and a Text element showing the current counter
    :param item_num: The number to use in the tuple for each element
    :type:           int
    :return:         List
    """
    row =  [sg.pin(sg.Col([[sg.Checkbox("",default=selected, k=("-SELECT_FBAND-", item_num,)),
                            #sg.T("Name"),
                            sg.In(band_name, size=(8,1), k=('-FBAND_NAME-', item_num)),
                            sg.Push(),
                            sg.T("Range:"),
                            sg.In(str(low_f), size=(3,1), k=('-FBAND_LOW_RANGE-', item_num)),
                            sg.T("-"), 
                            sg.In(str(high_f), size=(3,1), k=('-FBAND_HIGH_RANGE-', item_num)),
                            sg.T("Hz"), 
                            ]], k=('-ROW-', item_num), pad=(0,0), expand_x=True))]
    return row

def add_filter_row(item_num, low_f: int, high_f:int, selected: bool=True,):
    """
    A "Row" in this case is a Button with an "X", an Input element and a Text element showing the current counter
    :param item_num: The number to use in the tuple for each element
    :type:           int
    :return:         List
    """
    row =  [sg.pin(sg.Col([[sg.Checkbox("",default=selected, k=("-SELECT_FILTER-", item_num,)),
                            #sg.T("Name"),
                            sg.Push(),
                            sg.T("Filter Range:"),
                            sg.In(str(low_f), size=(3,1), k=('-FILTER_FBAND_LOW_RANGE-', item_num)),
                            sg.T("-"), 
                            sg.In(str(high_f), size=(3,1), k=('-FILTER_FBAND_HIGH_RANGE-', item_num)),
                            sg.T("Hz"), 
                            ]], k=('-ROWFILTER-', item_num), pad=(0,0), expand_x=True))]
    return row

layout_filter_sw = [
            [sg.Col([add_filter_row(idx, fil[0], fil[1]) for idx, fil in enumerate(s["sharpwave_analysis_settings"]["filter_ranges_hz"])], k='-TRACKING SECTION FILTER-')],
            [sg.T('+', enable_events=True, k='Add Item Filter', expand_x=True, tooltip='Add Another Filter')]]


def add_fband_row_seglength(fb, fb_idx, seg_length: int):
    row = [sg.pin(sg.Col([[sg.T(fb, key=f"-fb_idx_text_seg_length_{fb_idx}-"), sg.Push(), get_input(str(seg_length))]], pad=(0,0), expand_x=True), expand_x=True)]
    return row

def add_fband_row_burst(fb, fb_idx, checked: bool=True):
    row = [sg.pin(sg.Col([[sg.T(fb, key=f"-fb_idx_text_burst_sett_{fb_idx}-"), sg.Push(), sg.Checkbox("", default=checked)]], pad=(0,0), expand_x=True), expand_x=True)]
    return row

def get_selectred_fband_info(values: dict, get_all_bands: bool = True):
    vals_tuple = {key: values[key] for key in values.keys() if isinstance(key, tuple)}
    if get_all_bands is False:
        indexes = [i[1] for i in list(vals_tuple.keys()) if i[0] == '-SELECT_FBAND-' and vals_tuple[i] == True]
    else:
        indexes = [i[1] for i in list(vals_tuple.keys()) if i[0] == '-FBAND_NAME-']

    d = {}
    for i in indexes:
        d[values[("-FBAND_NAME-", i)]] = [values[("-FBAND_LOW_RANGE-", i)], values[("-FBAND_HIGH_RANGE-", i)]]
    return d

def slider_btn(turn_on: bool, key:str):
    img = toggle_btn_on if turn_on else toggle_btn_off
    return sg.Button(image_data=img, key=f"-TOGGLE_{key}", button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, metadata=False, pad=(0, 0), size=(0.5,0.5), image_subsample=3)

def get_input(text):
    return sg.Input(text, size=(5))

layout_normalization_raw = [[sg.T("normalization_time_s"), sg.Push(), get_input(s["raw_normalization_settings"]["normalization_time_s"])],
         [sg.T("clip"), sg.Push(), get_input(s["raw_normalization_settings"]["clip"])],
         [sg.T("normalization_method"), sg.Push(), sg.Combo(s["documentation_normalization_options"], "z-score", size=(10, 1))]
        ]
layout_normalization_feature = [[sg.T("normalization_time_s"), sg.Push(), get_input(s["feature_normalization_settings"]["normalization_time_s"])],
         [sg.T("clip"), sg.Push(), get_input(s["feature_normalization_settings"]["clip"])],
         [sg.T("normalization_method"), sg.Push(), sg.Combo(s["documentation_normalization_options"], "z-score", size=(10, 1))]
        ]

layout_sw_troughs = [[sg.T("estimate"), sg.Push(), slider_btn(s["sharpwave_analysis_settings"]["detect_troughs"]["estimate"], "sw_detect_troughs-")],
                   [sg.T("distance_troughs_ms"), sg.Push(), get_input(s["sharpwave_analysis_settings"]["detect_troughs"]["distance_troughs_ms"])],
                   [sg.T("distance_peaks_ms"), sg.Push(), get_input(s["sharpwave_analysis_settings"]["detect_troughs"]["distance_peaks_ms"])],
                   ]
layout_sw_peaks = [[sg.T("estimate"), sg.Push(), slider_btn(s["sharpwave_analysis_settings"]["detect_peaks"]["estimate"], "sw_detect_peaks-")],
                   [sg.T("distance_troughs_ms"), sg.Push(), get_input(s["sharpwave_analysis_settings"]["detect_peaks"]["distance_troughs_ms"])],
                   [sg.T("distance_peaks_ms"), sg.Push(), get_input(s["sharpwave_analysis_settings"]["detect_peaks"]["distance_peaks_ms"])],
                   ]

layout_fbands = [
            [sg.Col([add_fband_row(idx, fb_idx[0], fb_idx[1][0], fb_idx[1][1]) for idx, fb_idx in enumerate(s["frequency_ranges_hz"].items())], k='-TRACKING SECTION-')],
            [sg.T('+', enable_events=True, k='Add Item', expand_x=True, tooltip='Add Another Item')]]

layout_fbands_seg_lengths = [
    [sg.Col([add_fband_row_seglength(fb, fb_idx, s["bandpass_filter_settings"]["segment_lengths_ms"][fb]) for fb_idx, fb in enumerate(list(s["frequency_ranges_hz"].keys()))],
        k="-TRACK_SEC_FBAND_SEG_LENGTH-", expand_x=True)]
]

layout_bursts_fbands = [
    [sg.Col([add_fband_row_burst(fb, fb_idx, True if fb in s["burst_settings"]["frequency_bands"] else False) for fb_idx, fb in enumerate(list(s["frequency_ranges_hz"].keys()))],
            k="-TRACK_FBAND_BURSTS-", expand_x=True)]
]

layout_settings = [
    [sg.Frame("",
        [[sg.T("sampling_rate_features_hz"), sg.Push(), get_input(s["sampling_rate_features_hz"])],
         [sg.T("segment_length_features_ms"), sg.Push(), get_input(s["segment_length_features_ms"])],
        ],
        expand_x=True, font="bold"
    )],
    [sg.Frame("Preprocessing",
        [[sg.T("raw_resampling"), sg.Push(), slider_btn(True, "raw_resampling-")],
         [sg.T("resample_freq_hz"), sg.Push(), get_input(s["raw_resampling_settings"]["resample_freq_hz"])],
        [sg.T("notch_filter"), sg.Push(), slider_btn(True, "notch_filter-")],
        [sg.T("re_referencing"), sg.Push(), slider_btn(True, "notch_filter-")],
        [sg.T("raw_normalization"), sg.Push(), slider_btn(False, "raw_normalization-")]],
        expand_x=True,expand_y=True, font="bold"#size=(WIDTH_LAYOUT, )
    )],
    [sg.Frame("Features",
        [[sg.T(f), sg.Push(), slider_btn(f"{f}-", s["features"][f])] for f in feature_names],
        expand_x=True,expand_y=True, font="bold"
    )],
    [sg.Frame("Postprocessing",
        [[sg.T("feature_normalization"), sg.Push(), slider_btn(s["postprocessing"]["feature_normalization"], "feature_normalization-")],
        [sg.T("project_cortex"), sg.Push(), slider_btn(s["postprocessing"]["project_cortex"], "project_cortex-")],
        [sg.T("project_subcortex"), sg.Push(), slider_btn(s["postprocessing"]["project_subcortex"], "project_subcortex-")],
        ],expand_x=True,expand_y=True, font="bold"
    )],
    [sg.Frame("Normalization settings",
        [[sg.TabGroup(
            [[sg.Tab("Raw data", layout_normalization_raw), sg.Tab("Features", layout_normalization_feature)]],
            expand_x=True, expand_y=True)]],
        expand_x=True,expand_y=True, font="bold"
    )],
    [sg.Frame("Frequency band settings", layout_fbands, expand_x=True, font="bold")],
    [sg.Frame("FFT settings",
              [[sg.T("windowlength_ms"), sg.Push(), get_input(s["fft_settings"]["windowlength_ms"])],
               [sg.T("log_transform"), sg.Push(), slider_btn(s["fft_settings"]["log_transform"], "fft_settings_log_transform-")],
               [sg.T("kalman_filter"), sg.Push(), slider_btn(s["fft_settings"]["kalman_filter"], "fft_settings_kalman_filter-")]
               ], expand_x=True, font="bold"
    )],
    [sg.Frame("STFT settings",
              [[sg.T("windowlength_ms"), sg.Push(), get_input(s["stft_settings"]["windowlength_ms"])],
               [sg.T("log_transform"), sg.Push(), slider_btn(s["stft_settings"]["log_transform"], "stft_settings_log_transform-")],
               [sg.T("kalman_filter"), sg.Push(), slider_btn(s["stft_settings"]["kalman_filter"], "stft_settings_kalman_filter-")]
               ], expand_x=True, font="bold"
    )],
    [sg.Frame("bandpass_filter_settings",
        [[sg.T("log_transform"), sg.Push(), slider_btn(s["bandpass_filter_settings"]["log_transform"], "bandpass_filter_settings_log_transform")],
        [sg.T("kalman_filter"), sg.Push(), slider_btn(s["bandpass_filter_settings"]["kalman_filter"], "bandpass_filter_settings_kalman_filter")],
        [sg.Frame("bandpower_features", 
            [[sg.T("Hjorth activity"), sg.Push(), slider_btn(s["bandpass_filter_settings"]["bandpower_features"]["activity"], "bandpass_filter_settings_bandpower_features_activity")],
             [sg.T("Hjorth mobility"), sg.Push(), slider_btn(s["bandpass_filter_settings"]["bandpower_features"]["mobility"], "bandpass_filter_settings_bandpower_features_mobility")],
             [sg.T("Hjorth complexity"), sg.Push(), slider_btn(s["bandpass_filter_settings"]["bandpower_features"]["complexity"], "bandpass_filter_settings_bandpower_features_complexity")],
            ],expand_x=True)],
        # add here for each fband, that is stored in the current settings, an Input element with the segment length
        [sg.Frame("Segment lengths", layout_fbands_seg_lengths,
        expand_x=True)]], expand_x=True, font="bold"
    )],
    [sg.Frame("burst_settings",
        [[sg.T("threshold"), sg.Push(), get_input(s["burst_settings"]["threshold"])],
         [sg.T("time_duration_s"), sg.Push(), get_input(s["burst_settings"]["time_duration_s"])],
         [sg.Frame("burst_features", 
            [[sg.T("duration"), sg.Push(), slider_btn(s["burst_settings"]["burst_features"]["duration"], "burst_settings-burst_features-duration")],
             [sg.T("amplitude"), sg.Push(), slider_btn(s["burst_settings"]["burst_features"]["amplitude"], "burst_settings-burst_features-amplitude")],
             [sg.T("burst_rate_per_s"), sg.Push(), slider_btn(s["burst_settings"]["burst_features"]["burst_rate_per_s"], "burst_settings-burst_features-burst_rate_per_s")],
             [sg.T("in_burst"), sg.Push(), slider_btn(s["burst_settings"]["burst_features"]["in_burst"], "burst_settings-burst_features-in_burst")],
            ], expand_x=True)],
        [sg.Frame("Frequency bands", layout_bursts_fbands, expand_x=True)]
        ], expand_x=True, font="bold"
    )],
    [sg.Frame("sharpwave_analysis_settings",
        [[sg.T("threshold"), sg.Push(), get_input(s["burst_settings"]["threshold"])],
         [sg.T("time_duration_s"), sg.Push(), get_input(s["burst_settings"]["time_duration_s"])],
         [sg.Frame("sharpwave_features", 
            [[sg.T(sw_f), sg.Push(), slider_btn(f"sharpwave_analysis_settings-sharpwave_features-{sw_f}", s["sharpwave_analysis_settings"]["sharpwave_features"][sw_f])] for sw_f in list(s["sharpwave_analysis_settings"]["sharpwave_features"].keys())
            ], expand_x=True)],
         [sg.Frame("Filter specification",
                   layout_filter_sw, expand_x=True, key=""
        )]]
        #[sg.Frame("Detection parameters",
        #    [[sg.TabGroup(
        #    [[sg.Tab("Peaks", layout_sw_peaks), sg.Tab("Troughs", layout_sw_troughs, expand_x=True)]],
        #    expand_x=True, expand_y=True)]], expand_x=True)],
        #[sg.Frame("Estimators",
        #          [[for ]]
        #          expand_x=True)],
        #], expand_x=True, font="bold"
    )],

]

layout = [[sg.Column(layout_settings, scrollable=True, vertical_scroll_only=True, key="-COLUMN_SCROLL-",)]]  # size=(WIDTH_LAYOUT, 800),

window = sg.Window(
    "GUI Test",
    layout,
    auto_size_buttons=False,
    use_default_focus=False,
    finalize=False,
    size=(600, 800),
    metadata=len(list(s["frequency_ranges_hz"].keys()))-1
)

# idea: with each button press, the settings are also changed
# when fbands are added, they also in the setting dict changed
NUM_FILTERS_SW = len(s["sharpwave_analysis_settings"]["filter_ranges_hz"])-1

while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break

    if event.startswith("-TOGGLE"):
        window[event].metadata = not window[event].metadata
        window[event].update(image_subsample=3, image_data=toggle_btn_on if window[event].metadata else toggle_btn_off)
    if event == 'Add Item':
        window.metadata += 1
        window.extend_layout(window['-TRACKING SECTION-'], [add_fband_row(window.metadata, f"band_name_{window.metadata}", 5, 12, True)])
        window.extend_layout(window["-TRACK_SEC_FBAND_SEG_LENGTH-"], [add_fband_row_seglength(f"band_name_{window.metadata}", window.metadata, 1000)])
        window.extend_layout(window["-TRACK_FBAND_BURSTS-"], [add_fband_row_burst(f"band_name_{window.metadata}", window.metadata, False)])

        window.refresh()
        window['-COLUMN_SCROLL-'].contents_changed()
    elif event == "Add Item Filter":
        NUM_FILTERS_SW +=1
        window.extend_layout(window["-TRACKING SECTION FILTER-"], [add_filter_row(NUM_FILTERS_SW, 10, 20, True)])
        window.refresh()
        window['-COLUMN_SCROLL-'].contents_changed()
    else:
        # even if the fband is not selected, it should still be added to the segment length
        fbands = get_selectred_fband_info(values, get_all_bands=True)
        for i in range(window.metadata+1):
            window[f"-fb_idx_text_seg_length_{i}-"].update(list(fbands.keys())[i])
            window[f"-fb_idx_text_burst_sett_{i}-"].update(list(fbands.keys())[i])
        window.refresh()
        window['-COLUMN_SCROLL-'].contents_changed()
