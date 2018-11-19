from flask import Blueprint, current_app
from .list import DeviceListView
from .myself import MyselfDeviceView
from .bind import BindView, BindManageView

from StarMember.agent import DeviceList, LANDeviceProberConfig
from StarMember.utils.network import NetworkList

bind_api = Blueprint('DeviceBindAPI', __name__, url_prefix = '/v1/star/device')
bind_api.add_url_rule('/list', view_func = DeviceListView.as_view('DeviceList'))
bind_api.add_url_rule('/myself', view_func = MyselfDeviceView.as_view('MyselfDevice'))
bind_api.add_url_rule('/mine', view_func =  BindView.as_view('Mine'))
bind_api.add_url_rule('/mine/<string:mac>', view_func = BindManageView.as_view('BindManage'))



@bind_api.before_app_request
def bind_api_init():
    #current_app.landev_cfg = LANDeviceProberConfig()
    #current_app.landev_cfg.FromDict(current_app.config)
    #current_app.device_list = DeviceList(current_app.landev_cfg)
    current_app.device_list = NetworkList(
        _redis_port = current_app.config['REDIS_PORT']
        , _redis_host = current_app.config['REDIS_HOST']
        , _redis_prefix = current_app.config['LAN_DEV_REDIS_PROBER_IDENT_PREFIX']
    )
