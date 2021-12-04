import os, logging
from dns_records_update_runner import DnsRecordsUpdateRunner

dirname = os.path.dirname(__file__)
log_filename = os.path.join(dirname, 'log/app.log')

logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

task_runner = DnsRecordsUpdateRunner()
try:
    task_runner.run()
except Exception as error:
    logger.error(error)


