import numpy as np
import random
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from collections import deque

# Hyperparamètres
LEARNING_RATE = 0.001
DISCOUNT_FACTOR = 0.95
EPSILON = 1.0  # Exploration initiale
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.1
MEMORY_SIZE = 1000
BATCH_SIZE = 32

class ReplayMemory:
    def __init__(self, max_size):
        self.memory = deque(maxlen=max_size)

    def add(self, experience):
        self.memory.append(experience)

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def is_ready(self, batch_size):
        return len(self.memory) >= batch_size


class PongAI:
    def __init__(self):
        self.model = self.build_model()
        self.epsilon = EPSILON
        self.memory = ReplayMemory(MEMORY_SIZE)

    def build_model(self):
        model = Sequential([
            Dense(24, input_dim=4, activation="relu"),
            Dense(24, activation="relu"),
            Dense(2, activation="linear")  # Deux actions : haut ou bas
        ])
        model.compile(loss="mse", optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE))
        return model

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return random.choice([0, 1])  # Exploration
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])  # Exploitation

    def store_experience(self, state, action, reward, next_state, done):
        self.memory.add((state, action, reward, next_state, done))

    def train(self):
        if not self.memory.is_ready(BATCH_SIZE):
            return  # Pas assez de données pour entraîner

        batch = self.memory.sample(BATCH_SIZE)
        for state, action, reward, next_state, done in batch:
            target = reward
            if not done:
                target = reward + DISCOUNT_FACTOR * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)

        # Diminuer epsilon pour moins explorer avec le temps
        if self.epsilon > EPSILON_MIN:
            self.epsilon *= EPSILON_DECAY
