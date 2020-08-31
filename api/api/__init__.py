from apscheduler.schedulers.background import BackgroundScheduler
import requests

def set_ticket_expired():
    print("hi")
    URL = "http://localhost:8000/ticket/expire/"
    requests.put(url=URL)
    print("expired worked")
    return

def delete_expired_ticket():
    URL = "http://localhost:8000/ticket/deleteexpired/"
    requests.put(url=URL)
    print("delete worked")
    return

scheduler = BackgroundScheduler()
scheduler.add_job(set_ticket_expired, trigger='interval', seconds=5*60*60)
scheduler.add_job(delete_expired_ticket, trigger='interval', seconds=24*60*60)
scheduler.start()
print("hello")