from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
import atexit
from agents.crew import crew

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        
        def run_task():
            result = crew.kickoff()
            print("Task ran:", result)

        scheduler = BackgroundScheduler()
        scheduler.add_job(run_task, 'interval', minutes=4)
        print("Scheduler started, running every 4 minute.")
        scheduler.start()

        # Shut down scheduler on exit
        atexit.register(lambda: scheduler.shutdown())
