import art
import game_data
import random
import replit

is_correct = True
score = 0
data = game_data.data

def fetch_random_data():
  global score
  # Fetch random data from the list
  random_entry = random.choice(data)
  
# Extract the values for name, description, and country
  random_name = random_entry['name']
  random_description = random_entry['description']
  random_country = random_entry['country']
  
# Fetch random data from the list
  random_entry1 = random.choice(data)
# Extract the values for name, description, and country
  random_name1 = random_entry1['name']
  random_description1 = random_entry1['description']
  random_country1 = random_entry1['country']
    
  print(f"Compare A: {random_name}, a {random_description}, from {random_country}")
  print(art.vs)
  print(f"Compare B: {random_name1}, a {random_description1}, from {random_country1}")

  response = input("Who has more followers? Type 'A' or 'B': ")
  
  if response == "A" and random_entry['follower_count'] > random_entry1['follower_count']:
    #print("Continue")
    is_correct = True
    score += 1
    replit.clear()
    print(art.logo)
    print(f"You are correct. Current score: {score}")
    fetch_random_data()
  elif response == "B" and random_entry['follower_count'] < random_entry1['follower_count']:
    #print("Continue")
    is_correct = True
    score += 1
    replit.clear()
    print(art.logo)
    print(f"You are correct. Current score: {score}")
    fetch_random_data()
  else:
    is_correct = False
    replit.clear()
    print(art.logo)
    print("Sorry that's wrong answer. Game over!")
    print(f"You scored {score}")

fetch_random_data()
