import py_neuromodulation as nm
from py_neuromodulation import nm_IO, nm_define_nmchannels, nm_settings, nm_stream_offline
import numpy as np

def get_default_stream() -> nm_stream_offline.Stream:
    RUN_NAME, PATH_RUN, PATH_BIDS, PATH_OUT, datatype = nm_IO.get_paths_example_data()

    data = np.random.random([1000, 3]).T

    nm_channels = nm_define_nmchannels.get_default_channels_from_data(data)

    settings = nm_settings.get_default_settings()

    settings = nm_settings.set_settings_fast_compute(settings)

    stream = nm.Stream(
        sfreq=1000,
        nm_channels=nm_channels,
        settings=settings,
        verbose=True,
    )

    return stream
