from apscheduler.schedulers.background import BackgroundScheduler
import requests


def create_app():
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(set_ticket_expired, trigger='interval', seconds=1*60*60)
    scheduler.add_job(delete_expired_ticket, trigger='interval', seconds=24*60*60)
    scheduler.start()
    try:
        return app
    except:
        scheduler.shutdown()

def set_ticket_expired():
    URL = "http://localhost:8000/ticket/expire/"
    requests.put(url=URL)
    return

def delete_expired_ticket():
    URL = "http://localhost:8000/ticket/deleteexpired/"
    requests.put(url=URL)
    return