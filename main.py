import gymnasium
import matplotlib.pyplot as plt 
import time 

env = gymnasium.make('MountainCar-v0', render_mode="rgb_array")

# Observation and action space 
obs_space = env.observation_space
action_space = env.action_space
print("The observation space: {}".format(obs_space))
print("The action space: {}".format(action_space))

# Number of steps you run the agent for 
num_steps = 1500

# reset the environment and see the initial observation
obs = env.reset()

for step in range(num_steps):
    # take random action, but you can also do something more intelligent
    # action = my_intelligent_agent_fn(obs) 
    action = env.action_space.sample()
    
    # apply the action
    obs, reward, terminated, truncated, info = env.step(action)
    
    # Render the env
    env.render()

    # Wait a bit before the next frame unless you want to see a crazy fast video
    time.sleep(0.001)
    
    # If the epsiode is up, then start another one
    if terminated:
        env.reset()

# Close the env
env.close()

