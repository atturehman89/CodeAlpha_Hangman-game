import random

# --- 1. DATA: our word bank ---
words = ["python", "rocket", "jungle", "bridge", "castle"]

# --- 2. SETUP ---
word = random.choice(words)          # pick a surprise word
guessed_letters = []                 # track what the player has tried
lives = 6                            # wrong guesses allowed

def give_hint(word, guessed_letters):
    """Reveal 1-2 letters as a starting hint, avoiding first/last positions."""
    
    # Pick middle letters only (not index 0 or last index)
    middle_letters = list(set(word[1:-1]))  # unique letters from the middle
    
    # How many hints based on word length
    hint_count = 1 if len(word) <= 5 else 2
    
    # Pick random letters from the middle to reveal
    hints = random.sample(middle_letters, min(hint_count, len(middle_letters)))
    
    for letter in hints:
        guessed_letters.append(letter)
    
    print(f"   💡 Hint: We've revealed {hint_count} letter(s) to get you started!")

give_hint(word, guessed_letters)
# --- 3. HELPER: build the display like  p _ t _ o n ---
def get_display(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# --- 4. MAIN GAME LOOP ---
print("\n🎮 Welcome to Hangman!")
print(f"   The word has {len(word)} letters.\n")

while lives > 0:
    print("words is :",get_display(word, guessed_letters))
    print(f"   Lives left: {lives}  |  Guessed: {', '.join(guessed_letters) or 'none'}")

    # Get input
    guess = input("\n   Guess a letter: ").lower().strip()

    # Validate: must be a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("   ⚠️  Please enter a single letter.")
        continue

    # Already guessed?
    if guess in guessed_letters:
        print(f"   You already tried '{guess}'. Pick another!")
        continue

    # Add to guessed list
    guessed_letters.append(guess)

    # Check if correct
    if guess in word:
        print(f"   ✅ Nice! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"   ❌ Nope! '{guess}' is not in the word.")

    # --- 5. WIN CHECK ---
    if all(letter in guessed_letters for letter in word):
        print(f"\n🎉 You won! The word was: {word.upper()}")
        break

# --- 6. LOSE CHECK ---
else:
    print(f"\n💀 Game over! The word was: {word.upper()}")


    