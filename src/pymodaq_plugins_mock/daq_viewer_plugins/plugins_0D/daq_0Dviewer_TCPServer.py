from qtpy.QtCore import Signal
from easydict import EasyDict as edict
from collections import OrderedDict
from pymodaq.control_modules.viewer_utility_classes import DAQ_Viewer_TCP_server
from pymodaq.utils.daq_utils import ThreadCommand, getLineInfo
from pymodaq.utils.data import DataFromPlugins, DataToExport


class DAQ_0DViewer_TCPServer(DAQ_Viewer_TCP_server):
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
    command_server = Signal(list)

    def __init__(self, parent=None, params_state=None):
        super().__init__(parent, params_state,
                         grabber_type='0D')  # initialize base class with commom attributes and methods

        self.x_axis = None
        self.y_axis = None
        self.data = None

    def data_ready(self, data: list):
        """
            Send the grabed data signal.
        """

        self.dte_signal.emit(DataToExport('TCP0D', data=[DataFromPlugins(name='TCPServer', data=data, dim='Data0D')]))
