import random

print("Consensus Mechanism Simulation\n")

# PoW: Proof of Work
print("Simulating PoW (Proof of Work)")
# Mock validators with random 'power'
pow_validators = {
    'Alice': random.randint(1, 100),
    'Bob': random.randint(1, 100),
    'Charlie': random.randint(1, 100)
}

# Select the one with highest power
pow_winner = max(pow_validators, key=pow_validators.get)
print(f"[PoW] : {pow_winner} wins with power: {pow_validators[pow_winner]}")
print("The validator with the 'highest computing power' is selected.\n")

# PoS: Proof of Stake
print("Simulating PoS (Proof of Stake)")
# Mock validators with random 'stake'
pos_validators = {
    'Alice': random.randint(1, 100),
    'Bob': random.randint(1, 100),
    'Charlie': random.randint(1, 100)
}

# Select the one with highest stake
pos_winner = max(pos_validators, key=pos_validators.get)
print(f"[PoS] : {pos_winner} wins with stake: {pos_validators[pos_winner]}")
print("The validator with the 'highest staked amount' is selected.\n")

# DPoS: Delegated Proof of Stake
print("Simulating DPoS (Delegated Proof of Stake)")
# Mock votes from 3 users for candidates
votes = {
    'Alice': 0,
    'Bob': 0,
    'Charlie': 0
}

# 3 random users vote
voters = ['User1', 'User2', 'User3']
candidates = list(votes.keys())

for voter in voters:
    vote_for = random.choice(candidates)
    votes[vote_for] += 1
    print(f"{voter} voted for {vote_for}")

# Select the one with most votes
dpos_winner = max(votes, key=votes.get)
print(f"\n[DPoS] : {dpos_winner} wins with {votes[dpos_winner]} votes")
print("Validators are 'voted by users', and the one with 'most votes' is selected.\n")
