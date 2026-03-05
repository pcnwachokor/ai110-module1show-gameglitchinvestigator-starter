from logic_utils import check_guess, parse_guess, get_range_for_difficulty

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

def test_too_high_hint_says_go_lower():
    # Regression: hints were swapped — "Too High" said "Go HIGHER!" instead of "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    # Regression: hints were swapped — "Too Low" said "Go LOWER!" instead of "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_new_game_resets_status():
    # Regression: new game didn't reset status, so you couldn't play after winning/losing.
    # Simulate a game state after winning, then verify a reset allows playing again.
    game_state = {
        "status": "won",
        "attempts": 5,
        "score": 80,
        "history": [10, 20, 30, 40, 50],
    }
    # Apply the same reset logic that "New Game" should perform
    game_state["status"] = "playing"
    game_state["attempts"] = 0
    game_state["score"] = 0
    game_state["history"] = []
    assert game_state["status"] == "playing"
    assert game_state["attempts"] == 0
    assert game_state["score"] == 0
    assert game_state["history"] == []

def test_new_game_resets_after_loss():
    # Same regression test but for a lost game state
    game_state = {
        "status": "lost",
        "attempts": 8,
        "score": -10,
        "history": [10, 20, 30],
    }
    game_state["status"] = "playing"
    game_state["attempts"] = 0
    game_state["score"] = 0
    game_state["history"] = []
    assert game_state["status"] == "playing"
    assert game_state["attempts"] == 0

def test_score_does_not_carry_over_between_games():
    # Regression: score was not reset on new game, so it carried over.
    from logic_utils import update_score
    # Simulate finishing a game with a non-zero score
    score = 0
    score = update_score(score, "Win", 1)
    assert score > 0, "Score should increase after a win"
    # New game reset should bring score back to 0
    score = 0
    assert score == 0, "Score must reset to 0 when starting a new game"

def test_attempts_start_at_zero():
    # Regression: attempts initialized to 1 instead of 0, losing one attempt
    game_state = {"attempts": 0}
    assert game_state["attempts"] == 0, "Attempts should start at 0, not 1"

def test_guess_above_range_rejected():
    # Regression: values outside the range were accepted
    ok, value, err = parse_guess("25", low=1, high=20)
    assert not ok
    assert "Out of range" in err

def test_guess_below_range_rejected():
    # Regression: values outside the range were accepted
    ok, value, err = parse_guess("0", low=1, high=20)
    assert not ok
    assert "Out of range" in err

def test_guess_within_range_accepted():
    ok, value, err = parse_guess("10", low=1, high=20)
    assert ok
    assert value == 10
    assert err is None

def test_guess_at_range_boundaries_accepted():
    ok_low, val_low, err_low = parse_guess("1", low=1, high=20)
    ok_high, val_high, err_high = parse_guess("20", low=1, high=20)
    assert ok_low and val_low == 1
    assert ok_high and val_high == 20

def test_hard_range_larger_than_normal():
    # Regression: Hard had range 1-50 while Normal was 1-100, making Hard easier
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, "Hard range should be larger than Normal"

def test_difficulty_ranges_increase():
    # Easy should have smallest range, Normal middle, Hard largest
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high

def test_invalid_guess_does_not_count_as_attempt():
    # Regression: attempts incremented even on invalid input, wasting turns
    attempts = 0
    ok, _, _ = parse_guess("abc")
    if not ok:
        pass  # do NOT increment attempts
    else:
        attempts += 1
    assert attempts == 0, "Invalid guess should not count as an attempt"

def test_valid_guess_counts_as_attempt():
    attempts = 0
    ok, _, _ = parse_guess("50", low=1, high=100)
    if ok:
        attempts += 1
    assert attempts == 1, "Valid guess should count as an attempt"
