"""
Observation & Space example in CartPole-v0
http://gym.openai.com/docs/
"""
import gym

# change games: CartPole-v0, MountainCar-v0, MsPacman-v0 or Hopper-v1
env = gym.make('CartPole-v0')
# CartPole-v0:
# https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
print(env.action_space)
print(env.observation_space)
Txt = 0
for i_episode in range(20):
    observation = env.reset()
    for t in range(1000):
        env.render()
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if Txt != reward:
            Txt = reward
            print(Txt)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()


