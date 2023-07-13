import logging

from spaceone.core.manager import BaseManager
from spaceone.cost_analysis.connector import GoogleStorageConnector
from spaceone.cost_analysis.model import PluginMetadata

_LOGGER = logging.getLogger(__name__)


class DataSourceManager(BaseManager):

    @staticmethod
    def init_response(options):
        plugin_metadata = PluginMetadata()
        plugin_metadata.validate()

        return {
            'metadata': plugin_metadata.to_primitive()
        }

    def verify_plugin(self, options, secret_data, schema):
        google_storage_connector: GoogleStorageConnector = self.locator.get_connector(GoogleStorageConnector)
        google_storage_connector.create_session(options, secret_data, schema)
