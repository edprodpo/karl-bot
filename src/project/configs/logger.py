import logging
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

from src.project.configs.general import (
    Environment,
    GeneralSettings,
)


class TZFormatter(logging.Formatter):
    def __init__(self, *args, time_zone: ZoneInfo = ZoneInfo('UTC'), **kwargs):
        super().__init__(*args, **kwargs)
        self.time_zone: ZoneInfo = time_zone

    def formatTime(
        self,
        record: logging.LogRecord,
        datefmt: str | None = None,
    ) -> str:
        dt = datetime.fromtimestamp(record.created, self.time_zone)

        if datefmt:
            return dt.strftime(datefmt)

        return dt.isoformat()


class ErrorMetaFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool: # noqa
        if not hasattr(record, 'error_meta'):
            record.error_meta = ''
        return True


class LoggingSettings(GeneralSettings):
    def _tz_formatter(self) -> logging.Formatter:
        return TZFormatter(
            fmt=(
                '%(levelname)s %(asctime)s %(module)s %(process)d '
                '%(thread)d %(message)s error_meta:\n%(error_meta)s'
            ),
            datefmt='%Y-%m-%d %H:%M:%S',
            time_zone=self.TIME_ZONE,
        )

    def _error_filter(self) -> logging.Filter:
        return ErrorMetaFilter()

    def config_local_logger(self) -> None:
        logging.basicConfig(level=logging.INFO)

    def config_server_logger(self) -> None:
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)

        tz_formatter = self._tz_formatter()
        error_filter = self._error_filter()

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(tz_formatter)
        console_handler.addFilter(error_filter)

        file_handler = logging.FileHandler(
            filename='logs.log',
            encoding='utf-8',
        )
        file_handler.setFormatter(tz_formatter)
        file_handler.addFilter(error_filter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    def config_logger(self) -> None:
        if self.ENVIRONMENT == Environment.LOCAL:
            self.config_local_logger()
        else:
            self.config_server_logger()
