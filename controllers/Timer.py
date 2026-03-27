class Timer:
    #Create the timer and set default values
    def __init__(self,window):
        self.window=window
        self.seconds=0
        self.is_running=False
        self.timer_id=None
    
    #Start the timer if it is not running
    def start(self):
     
     if not self.is_running:
        self.is_running=True
        self.tick()
    
    #Stop the timer and cancel the next tick
    def stop(self):
       
       self.is_running=False
       if self.timer_id is not None:
          self.window.after_cancel(self.timer_id)
    
    #Stop the timer and put seconds back to zero
    def reset(self):
       
       self.stop()
       self.seconds=0
       self.window.hud.update_timer(self.seconds)
    
    #Add one second and update the screen
    def tick(self):
       
       if self.is_running:
          self.seconds+=1
          self.window.hud.update_timer(self.seconds)
          self.timer_id=self.window.after(1000,self.tick)