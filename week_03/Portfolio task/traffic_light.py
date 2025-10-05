
# Your name: XXX
# Your student ID: XXX
# You state that the code submitted is wholly written by yourself. 
# Date: XXX

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

while systime < maxtime + 1:
  remainder = systime % 15
  if remainder < 4:
    state = "red"
  elif remainder >= 4 and remainder < 7:
    state = "red_amber"
  elif remainder >= 7 and remainder < 12:
    state = "green"
  elif remainder >= 12 and remainder < 15:
    state = "amber"
  print(f"Time {systime:03} State {state}")
  systime = systime + 1
# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14