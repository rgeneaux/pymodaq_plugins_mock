from qtpy.QtCore import Signal
from easydict import EasyDict as edict
from collections import OrderedDict
from pymodaq.control_modules.viewer_utility_classes import DAQ_Viewer_TCP_server
from pymodaq.utils.daq_utils import ThreadCommand, getLineInfo
from pymodaq.utils.data import DataFromPlugins, Axis, DataToExport


class DAQ_1DViewer_TCPServer(DAQ_Viewer_TCP_server):
    """
        ================= ==============================
        **Attributes**      **Type**
        *command_server*    instance of Signal
        *x_axis*            1D numpy array
        *y_axis*            1D numpy array
        *data*              double precision float array
        ================= ==============================

        See Also
        --------
        utility_classes.DAQ_TCP_server
    """
    params_GRABBER = []

    # params = DAQ_TCP_server.params

    command_server = Signal(list)

    # params=DAQ_TCP_server.params
    def __init__(self, parent=None, params_state=None):
        super().__init__(parent, params_state,
                         grabber_type='1D')  # initialize base class with commom attributes and methods

        self.x_axis = None
        self.y_axis = None
        self.data = None

    def data_ready(self, data):
        """
            Send the grabed data signal.
        """
        self.dte_signal.emit(DataToExport('TCP1D', data=[DataFromPlugins(name='TCP Server', data=data, dim='Data1D')]))
