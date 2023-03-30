import sys
import numpy as np
import pandas as pd
import PySimpleGUI as sg
import py_neuromodulation as py_nm
import get_default_stream
import mne


from py_neuromodulation import nm_stream_offline, nm_define_nmchannels, nm_settings, nm_IO


def init_pynm(path, fs, linenoise,) -> nm_stream_offline.Stream:
    set_channels_by_mne = False
    if ".csv" in path:
        # design stream "by hand"
        df = pd.read_csv(path)
        data = df.to_numpy()
        channels = df.columns
        nm_channels = nm_define_nmchannels.get_default_channels_from_data(data.T, car_rereferencing=True)
        nm_channels["name"] = channels
    elif ".npy" in path:
        data = np.load(path)
        nm_channels = nm_define_nmchannels.get_default_channels_from_data(data, car_rereferencing=True)
    elif ".vhdr" in path:
        raw = mne.io.read_raw_brainvision(path)
        set_channels_by_mne = True
    elif ".edf" in path:
        raw = mne.io.read_raw_edf(path)
        set_channels_by_mne = True
    elif ".fif" in path:
        raw = mne.read_raw_fif(path)
        set_channels_by_mne = True
    if set_channels_by_mne == True:
        nm_channels = nm_define_nmchannels.set_channels(
            raw.ch_names,
            raw.get_channel_types(),
            "default",
            raw.bad,
            "default"
        )

    settings = nm_settings.get_default_settings()
    stream = nm_stream_offline.Stream(fs, nm_channels, settings)
    return  stream

stream = get_default_stream.get_default_stream()

layout_1 = [
           [sg.Text(text="Welcome to py_neuromodulation", size=(30,1), font="bold")],
           [sg.Text(text="Stream initialization", size=(15,1))],
           [sg.In(key="-filepath-") ,sg.FileBrowse(file_types=(("Data Files", ["*.fif", "*.vhdr", "*.npy", "*.csv"]),))],
           [sg.InputText("1000", key="-fs-"), sg.Text("Sampling frequency [Hz]")],
           [sg.InputText("50", key="-linenoise-"), sg.Text("Line noise [Hz]")],
           [sg.Button("Start Initialization")]
]

layout_2 = [
    [sg.Text(text="Welcome to py_neuromodulation", size=(30,1), font="bold")],
    [sg.Text(text="Specify nm_channels", size=(20, 2))],
    [sg.Table(
        values=stream.nm_channels.values.tolist(),
        headings=list(stream.nm_channels.columns),
        auto_size_columns=False,
        col_widths=list(map(lambda x:len(x)+1, list(stream.nm_channels.columns))),
        key="-nmtable-"
    )]
]

layout_3 = [
    [sg.Text(text="Welcome to py_neuromodulation", size=(30,1), font="bold")],
    [sg.Text(text="Feature Visualization", size=(20, 2))]
]

layout = [
    [
        sg.Column(layout_1, key='-COL1-'),
        sg.Column(layout_2, key='-COL2-', visible=False),
        sg.Column(layout_3, key='-COL3-', visible=False)
    ],
    [sg.Button("Stream Init"), sg.Button("Parametrization"), sg.Button("Features")],
]

window = sg.Window(
    "py_neuromodulation GUI",
    layout,
    auto_size_buttons=False,
    default_button_element_size=(12,1),
    use_default_focus=False,
    finalize=True,
    size=(600, 500)
)


while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Start Initialization":
        # read data from .txt, .npy or .bids path
        # fill out automatically the table and jump to Stream Init page
        if "" in [values["-filepath-"], values["-fs-"], values["-linenoise-"]] :
            sg.Popup('Please fill in filepath, fs and linenoise', title="Error stream init")
        else:
            stream = init_pynm(values["-filepath-"], float(values["-fs-"]), float(values["-linenoise-"]))
            window[f'-COL1-'].update(visible=False)
            window[f'-COL2-'].update(visible=True)
            window.Element("-nmtable-").update(
                values=stream.nm_channels.values.tolist(),
            )
            window[f'-COL3-'].update(visible=False)
    elif event == "Stream Init":
        window[f'-COL1-'].update(visible=True)
        window[f'-COL2-'].update(visible=False)
        window[f'-COL3-'].update(visible=False)
    elif event == "Parametrization":
        window[f'-COL1-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)
        window[f'-COL3-'].update(visible=False)
    elif event == "Features":
        window[f'-COL1-'].update(visible=False)
        window[f'-COL2-'].update(visible=False)
        window[f'-COL3-'].update(visible=True)
window.close()