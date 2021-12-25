import logging
from dns_records_update_runner import DnsRecordsUpdateRunner
from api.helper import get_absolute_path

log_filename = get_absolute_path('log/app.log')

logging.basicConfig(filename=log_filename, level=logging.ERROR, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

task_runner = DnsRecordsUpdateRunner()
try:
    task_runner.run()
except Exception as error:
    logger.error(error)


