#pip install requests
#pip install schedule
#pip install backoff
#pip install ratelimit

import datetime
import time

from schedule import every, repeat, run_pending
from ingestors import DaysummaryIngestor
from writers import DataWriter

if __name__ == "__main__":
    day_summary_ingestor = DaysummaryIngestor(
        writer=DataWriter, 
        coins=["BTC", "ETH", "LTC", "BCH"], 
        default_start_date=datetime.date(2022, 2, 1))


    #traders_ingestor = TradersIngestor() 
    ##Não foi criada ainda
    ##Para criar, basta implementar a classe em ingestors 

    @repeat(every(1).seconds)
    def job():
        day_summary_ingestor.ingest()
        #trades_ingestor.ingest()

    while True:
        run_pending()
        time.sleep(0.5)