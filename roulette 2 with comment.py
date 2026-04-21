import hashlib

# Dictionary mapping each roulette number to its color
ROULETTE_COLORS = {
    0: "Green",
    1: "Red", 2: "Black", 3: "Red", 4: "Black", 5: "Red", 6: "Black",
    7: "Red", 8: "Black", 9: "Red", 10: "Black", 11: "Black", 12: "Red",
    13: "Black", 14: "Red", 15: "Black", 16: "Red", 17: "Black", 18: "Red",
    19: "Red", 20: "Black", 21: "Red", 22: "Black", 23: "Red", 24: "Black",
    25: "Red", 26: "Black", 27: "Red", 28: "Black", 29: "Black", 30: "Red",
    31: "Black", 32: "Red", 33: "Black", 34: "Red", 35: "Black", 36: "Red"
}

# Game constants
DEFAULT_BET = 100                 # Default amount bet per round
STARTING_BALANCE = 1000          # Starting currency
FREE_REDEEM_AMOUNT = 300         # Amount given if balance hits 0

# Combines the seeds and nonce into a single string for hashing
def get_combined_seed(client_seed, server_seed, nonce):
    return f"{client_seed}:{server_seed}:{nonce}"

# Hashes the combined seed and converts it into a number
def hash_seed_to_number(seed_string):
    hash_result = hashlib.sha256(seed_string.encode()).hexdigest()
    number = int(hash_result[:8], 16)  # Use the first 8 hex digits
    return number

# Spins the wheel using a provably fair hash method
def generate_spin_result(client_seed, server_seed, nonce):
    combined_seed = get_combined_seed(client_seed, server_seed, nonce)
    number = hash_seed_to_number(combined_seed)
    roulette_result = number % 37  # Valid roulette numbers: 0–36
    return roulette_result

# Returns the color associated with a roulette number
def get_color(number):
    return ROULETTE_COLORS.get(number, "Unknown")

# Displays the spin result in a user-friendly way
def display_result(number):
    color = get_color(number)
    print(f"\n🎯 The ball landed on: {number} ({color})")

# Asks if the player wants to continue playing
def ask_to_continue():
    choice = input("Do you want to spin again? (y/n): ").strip().lower()
    return choice == 'y'

# Offers the user free coins once if their balance is 0
def redeem_free_balance(balance, free_redeemed):
    if balance <= 0 and not free_redeemed:
        print("\n💸 You’re out of coins!")
        choice = input("Would you like to redeem 300 free coins? (y/n): ").strip().lower()
        if choice == 'y':
            print("✅ You've received 300 free coins.")
            return FREE_REDEEM_AMOUNT, True
    return 0, free_redeemed

# Displays bet options and gets the player's choice
def get_bet_choice():
    print("\n📍 Bet options (payouts):")
    print("1 - Odd (2x payout)")
    print("2 - Even (2x payout)")
    print("3 - Green (0) — 18x payout!")
    while True:
        choice = input("Place your bet (1/2/3): ").strip()
        if choice in ('1', '2', '3'):
            return choice
        print("❌ Invalid input. Try again.")

# Lets the player adjust their bet or use the default
def get_bet_amount(balance):
    print(f"\n💵 Current balance: {balance} coins")
    print(f"Default bet is {DEFAULT_BET} coins.")
    try:
        amount = input("Enter your bet amount or press Enter to use default: ").strip()
        if amount == "":
            return DEFAULT_BET
        amount = int(amount)
        if 0 < amount <= balance:
            return amount
        else:
            print("❌ Invalid amount. Using default.")
            return DEFAULT_BET
    except ValueError:
        print("❌ Invalid input. Using default.")
        return DEFAULT_BET

# Checks if the player won the round
def did_player_win(bet_choice, result):
    if bet_choice == '1':  # Odd
        return result != 0 and result % 2 == 1
    elif bet_choice == '2':  # Even
        return result != 0 and result % 2 == 0
    elif bet_choice == '3':  # Green
        return result == 0
    return False

# Calculates the amount of coins won based on the bet and outcome
def calculate_payout(bet_choice, bet_amount):
    if bet_choice == '3':  # Green pays 18x
        return bet_amount * 18
    return bet_amount * 2  # Odd/Even pays 2x

# Main game loop
def play_roulette():
    print("🎰 Welcome to Python Roulette with Client Seed + Adjustable Bets!")

    # Initial setup
    client_seed = input("🔐 Enter your client seed: ").strip()
    server_seed = "server-secret-seed"  # Could be hidden & revealed later
    nonce = 0
    balance = STARTING_BALANCE
    free_redeemed = False

    while True:
        print(f"\n💰 Your balance: {balance} coins")

        # Check if user can redeem coins
        if balance < 1:
            bonus, free_redeemed = redeem_free_balance(balance, free_redeemed)
            if bonus > 0:
                balance += bonus
            else:
                print("❌ No coins left and no more bonuses available. Game over.")
                break

        # Let player choose bet type and amount
        bet_choice = get_bet_choice()
        bet_amount = get_bet_amount(balance)

        # Deduct bet from balance
        balance -= bet_amount

        # Spin and show result
        result = generate_spin_result(client_seed, server_seed, nonce)
        display_result(result)
        nonce += 1  # Increase nonce for next round

        # Determine win/loss and update balance
        if did_player_win(bet_choice, result):
            winnings = calculate_payout(bet_choice, bet_amount)
            balance += winnings
            print(f"🎉 You won! +{winnings - bet_amount} coins profit!")
        else:
            print(f"😞 You lost your bet of {bet_amount} coins.")

        print(f"📊 New balance: {balance} coins")

        # Ask if player wants to keep playing
        if not ask_to_continue():
            print("👋 Thanks for playing! Final balance:", balance)
            break

# Run the game
if __name__ == "__main__":
    play_roulette()
