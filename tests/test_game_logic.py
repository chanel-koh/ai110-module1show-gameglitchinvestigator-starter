from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hard_mode_range():
    # Verify that hard mode has a range of 1 to 100
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_parse_guess_whitespace():
    # Whitespace-only input should fail
    ok, guess_int, err = parse_guess("   ")
    assert ok == False
    assert guess_int is None
    assert err == "That is not a number."

def test_parse_guess_infinity():
    # Infinity input should fail
    ok, guess_int, err = parse_guess("inf")
    assert ok == False
    assert guess_int is None
    assert err == "That is not a number."

def test_parse_guess_negative():
    # Negative numbers should be parsed successfully
    ok, guess_int, err = parse_guess("-5")
    assert ok == True
    assert guess_int == -5
    assert err is None


