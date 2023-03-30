import PySimpleGUI as sg

# everything in a column needs to be a layout beforehand

# check now layout with toggle buttons:

toggle_btn_on = b'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'

toggle_btn_off = b'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'


def slider_btn():
    return sg.Button(image_data=toggle_btn_off, key='-TOGGLE-GRAPHIC-', button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=1, metadata=False, pad=(0, 0), size=(0.5,0.5), image_subsample=3)


layout_col_1 = [
    [sg.Frame("Preprocessing",
        [[sg.T("1"*(i+1)), sg.Push(), slider_btn()] for i in range(5)],
        expand_x=True,expand_y=True,
    )],
    [sg.Frame("Postprocessing",
         [[sg.Text("PostProcessing 1"), sg.Push(), sg.Combo(["choice 1", "choice 2", "choice 3"])]],
         expand_x=True,expand_y=True,
    )],
]

layout_col_2_2 = [[sg.T("2", pad=(0,0)), sg.B("2", pad=(0,0))] for i in range(20)
                ]
frame_settings = sg.Frame("nm_settings", [[sg.Column(layout_col_1, scrollable=True, size=(200, 500))]])
frame_nm_channels = sg.Frame("nm_channels", [[sg.Column(layout_col_2_2, element_justification="right")]], size=(200, 500))

layout_out = [[sg.Text(text="Welcome to py_neuromodulation", size=(30,1), font="bold")],
              [sg.Text(text="Stream initialization", size=(15,1))],
              [sg.In(key="-filepath-") ,sg.FileBrowse(file_types=(("Data Files", ["*.fif", "*.vhdr", "*.npy", "*.csv"]),))],
              [sg.InputText("1000", key="-fs-"), sg.Text("Sampling frequency [Hz]")],
              [sg.InputText("50", key="-linenoise-"), sg.Text("Line noise [Hz]")],
              [frame_settings, frame_nm_channels]]



#layout = [col]

window = sg.Window(
    "GUI Test",
    layout_out,
    auto_size_buttons=False,
    default_button_element_size=(12,1),
    use_default_focus=False,
    finalize=True,
    size=(600, 500),
    margins=(0,0),
)

while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
