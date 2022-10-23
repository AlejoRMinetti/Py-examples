"""
Pure random actions of CartPole-v0
http://gym.openai.com/docs/
"""
import gym

# change games: CartPole-v0, MountainCar-v0, MsPacman-v0 or Hopper-v1
env = gym.make('MsPacman-v0')

env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()