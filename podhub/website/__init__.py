from flask.ext.sqlalchemy import SQLAlchemy
from podhub.meh import Meh
from pkgutil import extend_path


__path__ = extend_path(__path__, __name__)

_config = {
    'DB_PASSWORD': 'ni0Thoug uti1Dei7 geoShah4 wie1Ahch',
    'DB_USER': 'mehdev',
    'DB_DATABASE': 'mehdev',
    'DB_HOST': 'localhost',
}
_config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(
    _config.get('DB_USER'), _config.get('DB_PASSWORD'),
    _config.get('DB_HOST'), _config.get('DB_DATABASE'))

app = Meh(__name__, config=_config).app
db = SQLAlchemy(app)

from . import models
