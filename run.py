import logging
from dns_records_update_runner import DnsRecordsUpdateRunner

logging.basicConfig(filename='log/app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

task_runner = DnsRecordsUpdateRunner()
try:
    task_runner.run()
except Exception as error:
    logger.error(error)


