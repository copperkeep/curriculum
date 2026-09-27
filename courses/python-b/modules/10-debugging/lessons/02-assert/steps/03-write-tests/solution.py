def clamp(x, low, high):
    return max(low, min(x, high))

def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-3, 0, 10) == 0
    assert clamp(99, 0, 10) == 10

test_clamp()
